#!/usr/bin/env sh
# AUTHOR: gotbletu (@gmail|twitter|youtube|github|lbry)
#         https://www.youtube.com/user/gotbletu
# DESC:   remove all hURL gopher header links (for W3M Web Browser with native gopher support)
# DEMO:   https://youtu.be/rM5vBRfwwzc
# REQD:   1. $EDITOR ~/.w3m/siteconf
#               url m@^gopher?://(.*)hURL:@
#               substitute_url "file:///cgi-bin/redirect_gopher.cgi?"
#         2. chmod +x ~/.w3m/cgi-bin/redirect_gopher.cgi
#         3. sed -i 's@cgi_bin.*@cgi_bin ~/.w3m/cgi-bin:/usr/lib/w3m/cgi-bin:/usr/local/libexec/w3m/cgi-bin@g' ~/.w3m/config

# Note: check if you have native gopher protocol support
# $ w3m -version
# $ w3m gopher://bitreich.org/1/lawn

# remove gopher hURL header link
# e.g gopher://gopher.floodgap.com/hURL:http://www.floodgap.com/ --> http://www.floodgap.com/
QUERY_STRING=$(printf "%s" "$QUERY_STRING" | sed 's@^gopher.*hURL:@@')
printf "%s\r\n" "W3m-control: GOTO $QUERY_STRING"
printf "%s\r\n" "W3m-control: DELETE_PREVBUF"
