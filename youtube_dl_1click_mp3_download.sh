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

# tutorial video: https://www.youtube.com/watch?v=nGSGlc9bTAg
# a script to copy link and convert youtube videos to mp3
# just create a shortcut launcher on the panel and click on it while on the youtube page you want to download the mp3 from

# requires: ffmpeg wmctrl xclip xdotool youtube-dl

# browser to focus; show list using wmctrl -l
BROWSER_FOCUS=Chromium
# set / create save location
DOWNLOAD_DIR_MP3=~/Downloads/youtube_music
# image to use
IMAGE_LOGO=~/.logo/youtube.png


# focus browser on top
wmctrl -a "$BROWSER_FOCUS"

# copy link to clipboard
sleep 0.5
xdotool key ctrl+l
sleep 0.5
xdotool key ctrl+c

mkdir -p "$DOWNLOAD_DIR_MP3"
cd "$DOWNLOAD_DIR_MP3"

notify-send -i "$IMAGE_LOGO" 'Downloading to MP3' 'Starting ...' -t 5000

# download (prevents downloading all playlist)
youtube-dl -c --restrict-filenames --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" "$(xclip -selection clipboard -o | cut -d\& -f1)"

notify-send -i "$IMAGE_LOGO" 'Downloading to MP3' 'Completed !!!' -t 5000

