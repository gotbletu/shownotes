#!/usr/bin/env sh
# AUTHOR: felipesaa (https://github.com/felipesaa)
# DESC:   restore a closed tab in w3m
# DEMO:   https://youtu.be/e5_q3-r6PAU
# RQMTS:  1. chmod +x ~/.w3m/cgi-bin/restore_tab.cgi
#         2. sed -i 's@cgi_bin.*@cgi_bin ~/.w3m/cgi-bin:/usr/lib/w3m/cgi-bin:/usr/local/libexec/w3m/cgi-bin@g' ~/.w3m/config
#         3. $EDITOR ~/.w3m/keymap
#               keymap  d      COMMAND     "EXTERN 'echo %s >> ~/.w3m/RestoreTab.txt' ; CLOSE_TAB"
#               keymap  u      TAB_GOTO    file:/cgi-bin/restore_tab.cgi

#Open the last closed tab
last_tab=$(tail -n 1 ~/.w3m/RestoreTab.txt);
#limit of tabs stored
limit=$(tail -n 20 ~/.w3m/RestoreTab.txt);
other_tabs=$(printf "%s" "$limit" | head -n -1);
printf "%s\r\n" "$other_tabs" > ~/.w3m/RestoreTab.txt;
printf "%s\r\n" "W3m-control: GOTO $last_tab";
printf "W3m-control: DELETE_PREVBUF\r\n"
