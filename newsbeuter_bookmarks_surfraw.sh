#!/bin/sh
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

# info: newsbeuter script to save bookmarks directly to surfraw
# demo video: https://www.youtube.com/watch?v=rHVfgGTTtNQ
# references: https://newsbeuter.wordpress.com/2007/08/27/bookmarking/
# config: 
#   vim ~/.newsbeuter/config
#     bookmark-cmd "~/.scripts/newsbeuter_bookmarks_surfraw.sh"
# hotkey:
#   Ctrl+B to bookmark an article url
#   Ctrl+G to cancel


url="$1"            # url
title="$2"          # tags
description="$3"    # nickname (single word only, no spaces)
echo -e "${description}\t${url}\t;; newsbeuter ${title}" >> ~/.config/surfraw/bookmarks

