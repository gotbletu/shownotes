#!/bin/bash
#             _   _     _      _         
#  __ _  ___ | |_| |__ | | ___| |_ _   _ 
# / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
#| (_| | (_) | |_| |_) | |  __/ |_| |_| |
# \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
# |___/                                  
#       https://www.youtube.com/user/gotbletu
#       https://twitter.com/gotbletu
#       https://plus.google.com/+gotbletu
#       https://github.com/gotbletu
#       gotbleu@gmail.com

# Tutorial video: https://www.youtube.com/watch?v=4LouA5E76FM
# Custom Actions that can be used on any File Manager with Custom Actions Support
# This script is to resize images to different resolution
# Requirements: imagemagick zenity

# thunar custom actions
# command: /path/to/script %N
# note: %N is the selected filenames (without paths)
# conditions: image files


PICKSIZE=$(zenity --list --radiolist --height "255" --text "<b>Please</b> make a selection:" --hide-header --column "Pick" --column "Item" FALSE "96x96" FALSE "128x128" FALSE "640x480" FALSE "800x600" TRUE "1024x768" FALSE "1280x720" FALSE "1280x960" FALSE "1920x1080")

myArray=( "$@" )
for arg in "${myArray[@]}"; do
	convert "$arg" -resize "$PICKSIZE" "${arg%.*}"_"$PICKSIZE"_resized."${arg##*.}"
done

