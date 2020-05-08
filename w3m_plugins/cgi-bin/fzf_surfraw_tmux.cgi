#!/usr/bin/env bash
###             _   _     _      _         
###  __ _  ___ | |_| |__ | | ___| |_ _   _ 
### / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
###| (_| | (_) | |_| |_) | |  __/ |_| |_| |
### \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
### |___/                                  
###       https://www.youtube.com/user/gotbletu
###       https://lbry.tv/@gotbletu
###       https://twitter.com/gotbletu
###       https://github.com/gotbletu
###       gotbletu@gmail.com
###
### Author          : gotbletu
### Name            : fzf_surfraw_tmux.cgi
### Version         : 0.2
### Date            : 2020-04-27
### Description     : interactive surfraw smart prefix search engine (mainly use within w3m web browser)
### Depends On      : surfraw  fzf  tmux  gawk  coreutils  grep  procps-ng
### Video Demo      : https://youtu.be/p5NZb8f8AHA
### References      : https://github.com/felipesaa/A-vim-like-firefox-like-configuration-for-w3m

### Setup
#     vim ~/.w3m/keymap
#     keymap  xs      COMMAND       "SHELL ~/.w3m/cgi-bin/fzf_surfraw_tmux.cgi ; GOTO /usr/lib/w3m/cgi-bin/goto_tmux_clipboard.cgi"
#     keymap  XS      COMMAND       "SHELL ~/.w3m/cgi-bin/fzf_surfraw_tmux.cgi ; TAB_GOTO /usr/lib/w3m/cgi-bin/goto_tmux_clipboard.cgi"

clear

# select your elvi
PREFIX=$(surfraw -elvi | grep -v 'LOCAL\|GLOBAL'| fzf -e | awk '{print $1}')

# exit script if no elvi is selected (e.g hit ESC)
if [ "$PREFIX" = "" ]; then exit; fi

# get user input
read -r -e -p "  $PREFIX >> Enter Your Search Keyword: " INPUT

# print proper url and copy to primary clipboard (aka highlighted clipboard) and tmux clipboard
# surfraw -p "$PREFIX" "$INPUT" | xsel -p
pidof tmux >/dev/null && tmux set-buffer "$(surfraw -p "$PREFIX" "$INPUT")"
