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
# This script is to rotate images clockwise to different degrees
# Requirements: imagemagick zenity

# thunar custom actions
# command: /path/to/script %N
# note: %N is the selected filenames (without paths)
# conditions: image files

DEGREE=$(zenity --list --radiolist --height "180" --text "<b>Please</b> make a selection:" --hide-header --column "Pick" --column "Item" TRUE "90" FALSE "180" FALSE "270")

myArray=( "$@" )
for arg in "${myArray[@]}"; do
	convert "$arg" -rotate "$DEGREE" "${arg%.*}"_rotated."${arg##*.}"
done

