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

# info: script to grab media links from w3m page and open with nvlc that will spawn a new tmux window

output_playlist=/tmp/playlist.m3u

# create playlist from http links (via xclip)
# w3m -dump "$(xclip -selection clipboard -o)" | awk '/http/ {print $2}' | grep -iE '.(mp4|avi|mpg|mpeg|m4v|mkv|mp3|wma|m4a|ogg|wav)$' > "${output_playlist}"

# create playlist from http links (via tmux clipboard)
w3m -dump "$(tmux show-buffer)" | awk '/http/ {print $2}' | grep -iE '.(mp4|avi|mpg|mpeg|m4v|mkv|mp3|wma|m4a|ogg|wav)$' > "${output_playlist}"

# append instead of overwrite
# lynx -dump "$(xclip -selection clipboard -o)" | awk '/http/ {print $2}' | grep -E '(.mp3$|.wma$|.m4a$|.ogg$|.wav$)' >> "${output_playlist}"

# open in new tmux window
tmux new-window -n w3mplay
tmux send-keys -t w3mplay "nvlc "${output_playlist}" && tmux kill-pane" 'Enter'
