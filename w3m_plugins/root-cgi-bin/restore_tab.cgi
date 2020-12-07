#!/usr/bin/env sh
# AUTHOR: felipesaa (https://github.com/felipesaa)
# DESC:   restore a closed tab in w3m
# DEMO:   https://youtu.be/e5_q3-r6PAU
# DEPEND: coreutils
# REFF:   https://github.com/felipesaa/A-vim-like-firefox-like-configuration-for-w3m
#         http://w3m.sourceforge.net/MANUAL#LocalCGI
# RQMTS:  1. allow executable permissions and put this script in /usr/lib/w3m/cgi-bin/
#         2. vim ~/.w3m/keymap
#               keymap  d      COMMAND     "EXTERN 'echo %s >> ~/.w3m/RestoreTab.txt' ; CLOSE_TAB"
#               keymap  u      TAB_GOTO    /usr/lib/w3m/cgi-bin/restore_tab.cgi

#Open the last closed tab
last_tab=$(tail -n 1 ~/.w3m/RestoreTab.txt);
#limit of tabs stored
limit=$(tail -n 20 ~/.w3m/RestoreTab.txt);
other_tabs=$(printf "%s" "$limit" | head -n -1);
printf "%s\r\n" "$other_tabs" > ~/.w3m/RestoreTab.txt;
printf "%s\r\n" "W3m-control: GOTO $last_tab";
printf "W3m-control: DELETE_PREVBUF\r\n"
