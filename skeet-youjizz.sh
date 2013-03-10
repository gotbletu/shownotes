#!/bin/bash
#             _   _     _      _         
#  __ _  ___ | |_| |__ | | ___| |_ _   _ 
# / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
#| (_| | (_) | |_| |_) | |  __/ |_| |_| |
# \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
# |___/                                  
#       http://gotbletu.blogspot.com/ | http://www.youtube.com/user/gotbletu
#
#	description: search youjizz.com from command line, then streams video using mplayer
#	useage: skeet-youjizz <search term>
#	requires: mplayer lynx youtube-dl
#	date: 2/17/2013
        keyword="$(echo "http://www.youjizz.com/search/$@" | sed 's/ /\-/g')"
	pagenum=5
	pagenum_to_url=$(for num in $(seq 1 "$pagenum"); do echo "$keyword-$num".html""; done )
	videourl=$(echo "$pagenum_to_url" | while read line; do lynx -dump "$line" \
	| awk '/\.com\/videos/ {print $2}' | awk '!x[$0]++' | tac ; done)
#	newlink=$(lynx --dump "$keyword" | awk '/\.com\/videos/ {print $2}' | awk '!x[$0]++')

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
			mplayer $( youtube-dl -g "${fileName}" )
                fi
                break
        done
	clear && clear
done
