#!/usr/bin/env sh
###             _   _     _      _         
###  __ _  ___ | |_| |__ | | ___| |_ _   _ 
### / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
###| (_| | (_) | |_| |_) | |  __/ |_| |_| |
### \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
### |___/                                  
###       https://www.youtube.com/user/gotbletu
###       https://twitter.com/gotbletu
###       https://github.com/gotbletu
###       gotbletu@gmail.com
###
### Author          : gotbletu
### Name            : goto_clipboard_primary.cgi
### Version         : 0.1
### Date            : 2020-04-26
### Description     : paste and go feature for w3m web browser using system clipboard (primary aka shift+insert)
### Depends On      : w3m  xsel
### Video Demo      : https://youtu.be/p5NZb8f8AHA
### References      : https://github.com/felipesaa/A-vim-like-firefox-like-configuration-for-w3m
### Install         : put this script in /usr/lib/w3m/cgi-bin/

#GOTO url in clipboard in current page. If the clipboard has a 
#"non url string/nothing" an blank page is shown.
printf "%s\r\n" "W3m-control: GOTO $(xsel -op)";
#delete the buffer (element in history) created between the current page and 
#the searched page by calling this script.
printf "W3m-control: DELETE_PREVBUF\r\n"
