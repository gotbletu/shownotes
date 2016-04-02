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

# This script is to mount archives such as zip,rar,tar,tar.gz...etc
# It can also work with some standard iso

# Requirements: gvfs-mount

# thunar custom actions
# command: /path/to/script %N
# note: %N is the selected filenames (without paths)
# conditions: Other files

myArray=( "$@" )
for arg in "${myArray[@]}"; do

    gvfs-mount "archive://$( ( echo -n 'file://' ; readlink -f "$arg" ; ) | perl -MURI::Escape -lne 'print uri_escape($_)')"

done


