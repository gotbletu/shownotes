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

if [ $# -lt 1 ]; then
  echo -e "Add Links To Podboat, Use Podboat As A TUI Download Manager"
  echo -e "\nUsage: $0 <url>"
  echo -e "\nExample:\n$0 http://abcxyz.com/filename.mp3"
else
  URL="$1"
  SAVE_PATH=~/Downloads
  GET_FILENAME="$(echo "$1" | rev | cut -d\/ -f1 | rev | sed -e 's@\%20@\_@g' )"
  
  echo "$URL" "$SAVE_PATH/$GET_FILENAME" >> ~/.newsboat/queue
fi


