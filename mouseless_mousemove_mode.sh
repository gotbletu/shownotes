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

# tutorial video playlist: https://www.youtube.com/playlist?list=PLqv94xWU9zZ1cXfg3ED24G6RSt4NbFBfO

# description: start mouseless (Grid) then wait for it to exit to start mousemove mode
# requires: mouselesss.py, mousemove_mode.sh and this script (mouseless_mousemove_mode.sh) to be in the same folder

# bind this script (mouseless_mousemove_mode.sh) to hotkeys examples
# Left Hand:    Ctrl+Shift+A or Hyper_L + A (Capslock + A)
# Right Hand:   Alt_R + Semicolon
# Numpad:       Pause/Break key

# kill existing script
wmctrl -F -c "mouseless"
sleep 0.1
wmctrl -F -c "mousemove_mode.sh"

# start script
DIR=$(dirname "$0")
"$DIR"/mouseless.py && xterm -geometry 0x0+0+0 -e "$DIR"/mousemove_mode.sh

