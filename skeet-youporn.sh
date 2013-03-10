#!/bin/bash
#             _   _     _      _         
#  __ _  ___ | |_| |__ | | ___| |_ _   _ 
# / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
#| (_| | (_) | |_| |_) | |  __/ |_| |_| |
# \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
# |___/                                  
#       http://gotbletu.blogspot.com/ | http://www.youtube.com/user/gotbletu
#
#	description: search youporn.com from command line, then streams video using mplayer
#	useage: skeet-youporn <search term>
#	requires: mplayer lynx 
	grepmatch=$(echo "$@" | sed 's/ /.*/g')
        keyword="$(echo "http://www.youporn.com/search?query=$@&type=straight" | sed 's/ /\+/g')"
	pagenum=3
	pagenum_to_url=$(for num in $(seq 1 "$pagenum"); do echo "$keyword&page=$num"; done )
	videourl=$(echo "$pagenum_to_url" | while read line; do lynx -dump "$line" \
	| awk '/watch/ {print $2}' | cut -d\/ -f1-6 | grep -iE $grepmatch | awk '!x[$0]++' | tac ; done)

# Set to endless loop
while true
do
        # Set the prompt for the select command
        PS3="Type a number to play or 'Ctrl+C' to quit: "

        # Create a list of files to display
        fileList=$(echo $videourl)

        # Show a menu and ask for input. If the user entered a valid choice,
        # then invoke the player on that file
        select fileName in $fileList; do
                if [ -n "$fileName" ]; then
			mplayer $( lynx -dump ${fileName} | awk '/mp4/ {print $2}' | head -1)
                fi
                break
        done
	clear && clear
done
