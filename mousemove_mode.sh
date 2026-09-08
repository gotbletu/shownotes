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

# description: move mouse cursor around, mouse clicks and drag using just the keyboard (vim style, wasd, numpad, or arrow keys)
# requirements: xdotool xterm wmctrl

# note: if you want to use this script by itself then bind commmand to a hotkey:
# xterm -geometry 0x0+0+0 -e /path/to/mousemove_mode.sh

# references:
# https://bbs.archlinux.org/viewtopic.php?pid=1106808#p1106808
# http://stackoverflow.com/a/10680015
# http://stackoverflow.com/a/11759139
# http://www.bbc.co.uk/accessibility/guides/keyboard_mouse/computer/linux/gnome/

# use to set always on top and refocusing
title="mousemove_mode.sh"

# Always on top: check if terminal script window is focus or not, if not then refocus it
refocus_window() {
  while :
  do
    detect_focus_window=$(xdotool getwindowfocus getwindowname)
    if [[ "$detect_focus_window" != "$title" ]]; then
      wmctrl -a "$title"
    fi
  done
}
# background the process
refocus_window &

# movemouse/mouse clicks using xdotools (using vim, wasd, numpad or arrow keys)
while read -rsn1 key        # 1 char (not delimiter), silent, dont need to hit enter key
do

  # catch multi-char special key sequences
  # allows special arrow keys to work
  read -sN1 -t 0.0001 k1
  read -sN1 -t 0.0001 k2
  read -sN1 -t 0.0001 k3
  key+=${k1}${k2}${k3}

  case "$key" in
    h|a|4|$'\e[D') xdotool mousemove_relative -- -15 0 ;; # move left
    j|s|5|$'\e[B') xdotool mousemove_relative 0 15 ;;     # move down
    k|w|8|$'\e[A') xdotool mousemove_relative -- 0 -15 ;; # move up
    l|d|6|$'\e[C') xdotool mousemove_relative 15 0 ;;     # move right
    u|e|7|'/') xdotool click 1 ;;                         # primary click
    o|q|9|'-') sleep 0.2 && xdotool click 3 ;;            # secondary click (menu click)
    i|r|'*'|',') xdotool click 2 ;;                       # middle click
    n|z|0) xdotool mousedown 1 ;;                         # highlight | drag&drop mode (begin)
    m|x|'.') xdotool mouseup 1 ;;                         # highlight | drag&drop mode (end)
    $'\e'|';'|'+') break ;;                               # quit
  esac

done
