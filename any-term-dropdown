#!/usr/bin/env bash
# AUTHOR: gotbletu (@gmail|twitter|youtube|github|lbry)
#         https://www.youtube.com/user/gotbletu
# DESC:   turn any terminal into a dropdown terminal
# DEMO:   https://www.youtube.com/watch?v=mVw2gD9iiOg
# DEPEND: coreutils xdotool wmutils (https://github.com/wmutils/core | https://aur.archlinux.org/packages/wmutils-git/)
# CLOG:   2021-02-10   use comm to match window name and class, this avoids terminal windows with different names
#         2015-02-15   0.1

# get screen resolution width and height
ROOT=$(lsw -r)
width=$(wattr w "$ROOT")
height=$(wattr h "$ROOT")

# option 1: set terminal emulator manually
# my_term=urxvt
# my_term=sakura
my_term="xterm"
# my_term="alacritty"
# my_term=terminator
# my_term=gnome-terminal

# option 2: auto detect terminal emulator (note: make sure to only open one)
# my_term="urxvt|xterm|uxterm|termite|sakura|lxterminal|terminator|mate-terminal|pantheon-terminal|konsole|gnome-terminal|xfce4-terminal"

# get terminal emulator pid ex: 44040485
# pid=$(xdotool search --class "$my_term" | tail -n1)

# get terminal emulator and matching name pid ex: 44040485 
pid=$(comm -12 <(xdotool search --name "$my_term" | sort) <(xdotool search --class "$my_term" | sort))

# get windows id from pid ex: 0x2a00125%
wid=$(printf 0x%x "$pid")

# maximize terminal emulator
wrs "$width" "$height" "$wid"

# toggle show/hide terminal emulator
mapw -t "$wid"
