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
#       gotbletu@gmail.com

# Tutorial video: https://www.youtube.com/watch?v=bJkDGWoACtk
# Custom Actions that can be used on any File Manager with Custom Actions Support

# This script is to unmount disc images that was mounted by fuseiso

# Requirements: fuse

# thunar custom actions
# command: /path/to/script %N
# alternative command: bash /path/to/script %N
# note: %N is the selected filenames (without paths)
# conditions: Directory files
# file pattern: *.iso;*.ISO;*.bin;*.BIN;*.nrg;*.NRG;*.mdf;*.MDF;*.img;*.IMG

myArray=( "$@" )
for arg in "${myArray[@]}"; do

    fusermount -u "$arg"

done

