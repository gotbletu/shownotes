#!/usr/bin/env bash
# author: gotbletu (@youtube|github|odysee)
#         https://www.youtube.com/user/gotbletu
# desc:   a script to download random wallpaper and delete old wallpaper at the sametime (wallhaven.cc)
# demo:   https://www.youtube.com/watch?v=cDtVEXjiKTw
# depend: curl grep sed findutils coreutils wget

# Variable (you can change any of these to your liking)
savedir=~/Pictures/Wallpapers
tempdir=/tmp/wallpaper_wallhaven
expire_date=30

# create folders
mkdir -p $savedir	
mkdir -p $tempdir

cd $tempdir || exit

# change the url if you need different resolutions
curl -f -L 'https://wallhaven.cc/search?categories=111&purity=100&resolutions=1920x1080&sorting=random&order=desc&ai_art_filter=1' | grep -Eo "https?://\S+?\"" | grep small | cut -d '"' -f1 | sed -e 's@//th@//w@g' -e 's/small/full/g' -e 's@/@/wallhaven-@5' | while read -r link ; do wget --timestamping "$link" || wget --timestamping  "${link//.jpg/.png}" ; done


# # get links of images and download it
# get_random_url=$(lynx -listonly -nonumbers -dump "https://wallhaven.cc/random" | grep '/w/')
# get_images_url=$(echo "$get_random_url" | while read -r line; do lynx -source "$line" | grep -Po '<img id="wallpaper" src="\K[^"]+' ; done )
# echo "$get_images_url" | while read -r line; do wget -N "$line" ; done

# delete any file under 200k in size (to avoid shitty thumnbails or crap quality)
find . -type f -iname "*.jp*g" -size -200k -exec rm {} \;
find . -type f -iname "*.png" -size -200k -exec rm {} \;

# change the downloaded wallpaper metadata (modified date to todays date)
#  this makes it easy to see which files are older to delete later on
find . -type f -iname "*.jp*g" -exec touch -m {} \;
find . -type f -iname "*.png" -exec touch -m {} \;

# now that everything is cleaned and filter
#  send the downloaded images to the wallpaper folder 
find . -type f -iname "*.jp*g" -exec mv {} $savedir \;
find . -type f -iname "*.png" -exec mv {} $savedir \;

#  delete wallpaper image older then X days and remove temp folder
rm -rf $tempdir
find $savedir -mtime +$expire_date -exec rm {} \;

