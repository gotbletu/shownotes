#!/bin/bash
#             _   _     _      _         
#  __ _  ___ | |_| |__ | | ___| |_ _   _ 
# / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
#| (_| | (_) | |_| |_) | |  __/ |_| |_| |
# \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
# |___/                                  
#       http://gotbletu.blogspot.com/ | http://www.youtube.com/user/gotbletu
#
#	description: search empflix.com from command line, then streams video using mplayer
#	useage: skeet-empflix <search term>
#	requires: mplayer lynx quvi
#	date: March 09, 2013
        keyword="$(echo "&what=$@&sort=relevance&su=anytime&sd=all" | sed 's/ /\%20/g')"
	pagenum=3
	pagenum_to_url=$(for num in $(seq 1 "$pagenum"); do echo "http://www.empflix.com/search.php?page=$num$keyword"; done )
	videourl=$(echo "$pagenum_to_url" | while read line; do lynx -dump "$line" \
	| awk '/empflix\.com\/videos/ {print $2}' | awk '!x[$0]++' | tac ; done)

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
		quvi --exec "mplayer %u" "${fileName}" 
                fi
                break
        done
	clear && clear
done
