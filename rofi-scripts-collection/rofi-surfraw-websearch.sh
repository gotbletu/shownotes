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

# info: rofi-surfraw-websearch is a script to do internet searches from different websites, all from the rofi launcher
# requirements: rofi surfraw
# playlist: rofi      https://www.youtube.com/playlist?list=PLqv94xWU9zZ0LVP1SEFQsLEYjZC_SUB3m
#           surfraw   https://www.youtube.com/playlist?list=PLqv94xWU9zZ2e-lDbmBpdASA6A6JF4Nyz

# set your browser (uncomment if needed, some GUI does not detect browser variable)
# BROWSER=firefox

surfraw -browser=$BROWSER $(sr -elvi | awk -F'-' '{print $1}' | sed '/:/d' | awk '{$1=$1};1' | rofi -kb-row-select "Tab" -kb-row-tab "Control+space" -dmenu -mesg ">>> Tab = Autocomplete" -i -p "rofi-surfraw-websearch: ")

