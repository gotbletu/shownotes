#!/usr/bin/env sh
# AUTHOR: gotbletu (@gmail|twitter|youtube|github|lbry)
#         https://www.youtube.com/user/gotbletu
# DESC:   paste and go feature for w3m web browser using system clipboard (aka ctrl+v)
# DEMO:   https://youtu.be/p5NZb8f8AHA | updated https://youtu.be/0j3pUfZjCeQ
# REQD:   1. chmod +x ~/.w3m/cgi-bin/goto_clipboard.cgi
#         2. sed -i 's@cgi_bin.*@cgi_bin ~/.w3m/cgi-bin:/usr/lib/w3m/cgi-bin:/usr/local/libexec/w3m/cgi-bin@g' ~/.w3m/config
#         3. sed -i 's@default_url.*@default_url 1@g' ~/.w3m/config
#         4. $EDITOR ~/.w3m/keymap
#              keymap  pp      GOTO        file:/cgi-bin/goto_clipboard.cgi
#              keymap  PP      TAB_GOTO    file:/cgi-bin/goto_clipboard.cgi

# REFF:   https://github.com/felipesaa/A-vim-like-firefox-like-configuration-for-w3m
# CLOG:   2021-05-22 version 0.3 new instructions, no longer required root path for cgi scripts
#         2021-02-05 version 0.2 reset url back to 1 (aka edit current url)
#         2020-04-26 version 0.1

# set open-url value to zero (aka empty url line)
printf "%s\r\n" "W3m-control: SET_OPTION default_url=0"

#GOTO url in clipboard in current page. If the clipboard has a 
#"non url string/nothing" an blank page is shown.
printf "%s\r\n" "W3m-control: GOTO $(xsel -ob)"

#delete the buffer (element in history) created between the current page and 
#the searched page by calling this script.
printf "%s\r\n" "W3m-control: DELETE_PREVBUF"

# set default open-url value to one (aka current url)
printf "%s\r\n" "W3m-control: SET_OPTION default_url=1"
