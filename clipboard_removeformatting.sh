#!/bin/bash
#             _   _     _      _         
#  __ _  ___ | |_| |__ | | ___| |_ _   _ 
# / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
#| (_| | (_) | |_| |_) | |  __/ |_| |_| |
# \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
# |___/                                  
#       http://www.youtube.com/user/gotbletu
#       https://twitter.com/gotbletu
#       https://plus.google.com/+gotbletu
#       https://github.com/gotbletu
#       gotbleu@gmail.com

# Useful when copying from websites
# This will paste in plain text without formatting.

# tutorial video: https://www.youtube.com/watch?v=YY3hRhrUjOQ
# requires: xclip xdotool

xclip -selection clipboard -o | xclip -selection clipboard
sleep 0.5
xdotool key ctrl+v

# if you are using a clipboard manager also then you can uncomment theses
# sleep 0.5
# killall xclip
