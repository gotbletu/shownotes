#!/usr/bin/env sh
# AUTHOR: gotbletu (@gmail|twitter|youtube|github|lbry)
#         https://www.youtube.com/user/gotbletu
# DESC:   remove all duckduckgo redirect links
# DEMO:   https://youtu.be/rM5vBRfwwzc
# REFF:   grep string between two words https://stackoverflow.com/a/13245961
# REQD:   1. $EDITOR ~/.w3m/siteconf
#               url m@^https?://duckduckgo.com/l/\?uddg@
#               substitute_url "file:///cgi-bin/redirect_duckduckgo.cgi?"
#         2. chmod +x ~/.w3m/cgi-bin/redirect_duckduckgo.cgi
#         3. sed -i 's@cgi_bin.*@cgi_bin ~/.w3m/cgi-bin:/usr/lib/w3m/cgi-bin:/usr/local/libexec/w3m/cgi-bin@g' ~/.w3m/config

W3M_CURRENT_LINK="$(printf "%s" "$W3M_CURRENT_LINK" | grep -oP '(?<=duckduckgo.com\/l\/\?uddg=).*(?=&)' | sed -e "s/%\([0-9A-F][0-9A-F]\)/\\\\\x\1/g" | xargs -0 echo -e)"
printf "%s\r\n" "W3m-control: GOTO $W3M_CURRENT_LINK"
printf "%s\r\n" "W3m-control: DELETE_PREVBUF"

