#!/bin/bash
#             _   _     _      _         
#  __ _  ___ | |_| |__ | | ___| |_ _   _ 
# / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
#| (_| | (_) | |_| |_) | |  __/ |_| |_| |
# \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
# |___/                                  
#       http://gotbletu.blogspot.com/ | http://www.youtube.com/user/gotbletu
#
#	description: search mp3skull.com from command line, then streams music using mplayer
#	useage: mp3skull-cli <search term>
#	requires: mplayer lynx (wget for download)
#	date: March 12, 2013
        keyword="$(echo "http://mp3skull.com/mp3/$@.html" | sed 's/ /\_/g')"
	music_url=$(lynx -source "$keyword" | awk '/href/ && /\.mp3/' \
		| cut -d\" -f4 | sed 's/ /\%20/g' | awk '!x[$0]++' |tac)

# Set to endless loop
while true
do
        # Set the prompt for the select command
        PS3="Type a number to play or 'Ctrl+C' to quit: "

        # Create a list of files to display
        fileList=$(echo $music_url)

        # Show a menu and ask for input. If the user entered a valid choice,
        # then invoke the player on that file
        select fileName in $fileList; do
                if [ -n "$fileName" ]; then
			mplayer "${fileName}" 

			# if you want to download instead
			#wget -c "${fileName}" 
                fi
                break
        done
	clear && clear
done
