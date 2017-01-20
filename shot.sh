#!/bin/bash
#####################################################################
#			Version: 1.5.9
#####################################################################
#
# This script takes screenshots of a movie
# Depends on mplayer and imagemagick
#
# Made by	Starlite	<http://starl1te.wordpress.com/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#####################################################################

usage="Type shot -h for help"

_help(){
echo -e "\nusage: shot [options] [file] ... [fileN]\n
 Options:
  -t <time> - Set time (in minutes) between screenshots; the number of screenshots is calculated automatically.
  -n <number> - Set a fixed number of screenshots to take.
  -m - Manual mode. Use arrows to FF/rewind. Press [S] to make screenshots. Quit mplayer to continue.
  -r <percent> - Change the size of the output image. Less than 40% is recommended.
  -s - Seed mode. Gives extra video and audio information. Removes spaces from filenames.
  -h - Display this help message\n

If you don't like screenshots run the script again.
This script depends on Mplayer and ImageMagic. Make sure you have them installed.\n
Usage example:
shot -n 25 -r 35% ~/films/film.avi\n"
}

shot(){
# Making screenshots...
for i in `seq 1 $shots_number`;
do
  randomiser=$RANDOM; let "randomiser %= 25"
  hop=`echo $[$shot_time*60*$i+$randomiser]`
  mplayer -ss $hop -noautosub -frames 1 -ao null -vo png "$file_path" &> /dev/null
  mv 00000001.png /tmp/shots/$i.png &> /dev/null
  echo -ne "Taking screenshot #${i} \r"
done
  echo "Taking screenshots...           [OK]"
}

# ====== first step is here! ^_^ ========
# Checking options...
while getopts ":t:n:mr:sh" option
	do
		case $option in
		t ) shot_time=$OPTARG; opt=_time;;
		n ) shots_number=$OPTARG; opt=_num;;
		m ) opt=_manual;;
		h ) _help; opt=1; exit 1;;
		s ) seed=1;;
		r ) res=$OPTARG;;
		: ) echo "No argument given"; opt=1; exit 1;;
		* ) echo "Unknown option"; echo $usage; opt=1; exit 1;;
		esac
	done

if [ "$res" == "" ]; then res=35%; fi
if [ "$opt" == "" ]; then echo "No options given!"; echo $usage; exit 1; fi
shift $(($OPTIND - 1))
if [ "$1" == "" ]; then echo "No file given!"; echo $usage; exit 1; fi
mkdir /tmp/shots

# Parsing files...
while [ "$1" != "" ]
do
  file_path=$1
  file_name_ext=${file_path##*/}
  file_name=`echo "$file_name_ext" | sed '$s/....$//'`
  randomiser=0
  quality=87
  testpath=`dirname "$file_path" | cut -c1`
	if [ "$testpath" == "." ]||[ "$testpath" != "/" ]; then
	file_path=`pwd`/$file_path
	fi
  path=`pwd`
  cd "$path"
echo -e "==> Processing file $file_name_ext..."

# Getting video info...
tmp="/tmp/shots/info"
inf=`mplayer "$file_path" -identify -frames 1 -ao null -vo null 2>/dev/null | tee $tmp`

length=`cat $tmp | grep LENGTH | sed -e 's/^.*=//' -e 's/[.].*//'`
if [ "$length" == "" ]; then echo "Error! Can't get the length of the movie."; exit 1; fi

# Calculating timing...
if [ "$opt" == "_time" ]; then
	shots_number=`echo $[$length/60/$shot_time]`
	shot
elif [ "$opt" == "_num" ]; then
	shot_time=`echo $[$length/$shots_number/60]`
	shot
elif [ "$opt" == "_manual" ]; then
	cd /tmp/shots
	echo "Press [S] to make screenshots."
	mplayer -ao null -vf screenshot -quiet "$file_path"
	echo "Taking screenshots...           [OK]"
fi

# Merging screenshots...
echo -n "Putting screenshots together..."
cd /tmp/shots/
montage -geometry +2+2 `ls *.png | sort -n` "$file_name".jpg
mogrify -resize $res "$file_name".jpg
echo " [OK]"
echo -n "Getting video info..."
size=`stat -c%s  "$file_path"`
size=`echo $[$size/1024/1024]`
format=`cat $tmp | grep VIDEO: | cut -d " " -f 5`
length=`echo $[$length/60]`

# It's a tricky code here, it adds some info about the movie to the output image.
echo -e "File name: $file_name_ext\nSize: $size Mb\nResolution: $format\nDuration: $length min." | convert -pointsize 16 -trim +repage text:- text.jpg
convert "$file_name".jpg -quality $quality -splice 0x80 -draw 'image over 5,5 0,0 text.jpg' "$path/$file_name".jpg
echo "           [OK]"
cd "$path"
# Extra info
    if [ "$seed" == "1" ]; then
	#====Video====
	width=`cat $tmp | grep VIDEO_WIDTH | sed -e 's/^.*=//'`
	height=`cat $tmp | grep VIDEO_HEIGHT | sed -e 's/^.*=//'`
	format=`cat $tmp | grep VIDEO_FORMAT | sed -e 's/^.*=//'`
	vcodec=`cat $tmp | grep VIDEO_CODEC | sed -e 's/^.*=//'`
	video="Format:  $format\nCodec:  $vcodec"
	size="Size:  $width*$height"
	#====Audio====
	rate=`cat $tmp | grep AUDIO_RATE | sed -e 's/^.*=//' | tail -n 1`
	acodec=`cat $tmp | grep afm: | sed -e 's/^.*: //'`
	lang1=`cat $tmp | grep ID_AID_0_LANG | sed -e 's/^.*=//'`
	lang2=`cat $tmp | grep ID_AID_1_LANG | sed -e 's/^.*=//'`
	audio="Audio:  $rate $acodec"
	lang="Dub:  1: $lang1  2: $lang2"
	echo -e "\n$video\n$size\n$audio\n$lang"
	#filenames trimming
	file_name_sp=`echo "$file_name" | sed 's/ /_/g'`
	mv "$file_name".jpg "$file_name_sp".jpg &> /dev/null
    fi
rm /tmp/shots/*
echo
shift
done

rm -r /tmp/shots
echo "Done"
