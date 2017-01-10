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

# DESC: Toggle redshift on and off
# DEMO: https://www.youtube.com/watch?v=c8v84LRTeUw
# Requirements: redshift, notify-send (libnotify)

# check if process is running ( 0 = off, 1 = on )
STATUS="$(ps -ef | grep -w '[r]edshift' | wc -l)"
# if off then turn on
if [[ "${STATUS}" == 0 ]]; then
  notify-send -t 1 --icon=info "RedShift" "On"
  redshift >/dev/null 2>&1 & disown
# else if on then turn off
elif [[ "${STATUS}" == 1 ]]; then
  notify-send -t 1 --icon=info "RedShift" "Off"
  redshift -x && killall redshift
fi


