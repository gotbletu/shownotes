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

# Tutorial video: https://www.youtube.com/watch?v=bJkDGWoACtk
# Custom Actions that can be used on any File Manager with Custom Actions Support

# This script is to mount standard disc image files such as iso|bin|nrg|mdf|img without sudo permissions

# Requirements: fuseiso

# thunar custom actions
# command: /path/to/script %N
# alternative command: bash /path/to/script %N
# note: %N is the selected filenames (without paths)
# conditions: Other files
# file pattern: *.iso;*.ISO;*.bin;*.BIN;*.nrg;*.NRG;*.mdf;*.MDF;*.img;*.IMG

myArray=( "$@" )
for arg in "${myArray[@]}"; do

    fuseiso -n -p "$arg" "/tmp/$arg"
    xdg-open "/tmp/$arg"

done

