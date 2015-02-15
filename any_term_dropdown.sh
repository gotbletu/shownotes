#!/bin/bash
# any_term_dropdown.sh - turns any terminal into a dropdown terminal
# tutorial video: https://www.youtube.com/watch?v=mVw2gD9iiOg
#             _   _     _      _         
#  __ _  ___ | |_| |__ | | ___| |_ _   _ 
# / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
#| (_| | (_) | |_| |_) | |  __/ |_| |_| |
# \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
# |___/                                  
#       http://www.youtube.com/user/gotbletu
#       https://twitter.com/gotbletu
#       https://www.facebook.com/gotbletu
#       https://plus.google.com/+gotbletu
#       https://github.com/gotbletu

# requires:
# 	xdotool
# 	wmutils https://github.com/wmutils/core
#		https://aur.archlinux.org/packages/wmutils-git/ 

# get screen resolution width and height
ROOT=$(lsw -r)
width=$(wattr w $ROOT)
height=$(wattr h $ROOT)

# option 1: set terminal emulator manually
# my_term=urxvt
# my_term=xterm
# my_term=terminator
# my_term=gnome-terminal

# option 2: auto detect terminal emulator (note: make sure to only open one)
my_term="urxvt|xterm|uxterm|termite|sakura|lxterminal|terminator|mate-terminal|pantheon-terminal|konsole|gnome-terminal|xfce4-terminal"

# get terminal emulator pid ex: 44040485
pid=$(xdotool search --class "$my_term" | tail -n1)

# get windows id from pid ex: 0x2a00125%
wid=$(printf 0x%x "$pid")

# maximize terminal emulator
wrs "$width" "$height" "$wid"

# toggle show/hide terminal emulator
mapw -t "$wid"	

