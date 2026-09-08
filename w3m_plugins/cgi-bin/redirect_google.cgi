#!/usr/bin/env sh
# AUTHOR: gotbletu (@gmail|twitter|youtube|github|lbry)
#         https://www.youtube.com/user/gotbletu
# DESC:   remove all google redirect links
# DEMO:   https://youtu.be/rM5vBRfwwzc
# REQD:   1. $EDITOR ~/.w3m/siteconf
#               url m@^https?://(.*\.)google.com/url@
#               substitute_url "file:///cgi-bin/redirect_google.cgi?"
#         2. chmod +x ~/.w3m/cgi-bin/redirect_google.cgi
#         3. sed -i 's@cgi_bin.*@cgi_bin ~/.w3m/cgi-bin:/usr/lib/w3m/cgi-bin:/usr/local/libexec/w3m/cgi-bin@g' ~/.w3m/config

W3M_CURRENT_LINK="$(printf "%s" "$W3M_CURRENT_LINK" | grep -oP '(?<=google.com\/url\?q=)[^&]*(?=&)' | sed -e "s/%\([0-9A-F][0-9A-F]\)/\\\\\x\1/g" | xargs -0 echo -e)"
printf "%s\r\n" "W3m-control: GOTO $W3M_CURRENT_LINK"
printf "%s\r\n" "W3m-control: DELETE_PREVBUF"

