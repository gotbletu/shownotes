#!/usr/bin/env sh
# AUTHOR: gotbletu (@gmail|twitter|youtube|github|lbry)
#         https://www.youtube.com/user/gotbletu
# DESC:   send magnet links to your torrent client (for W3M Web Browser)
# DEMO:   https://youtu.be/T74FqHMHjN0
# REQD:   1. touch ~/.w3m/urimethodmap
#         2. echo "magnet: file:/cgi-bin/magnet.cgi?%s" >> ~/.w3m/urimethodmap
#         3. chmod +x ~/.w3m/cgi-bin/magnet.cgi
#         4. sed -i 's@cgi_bin.*@cgi_bin ~/.w3m/cgi-bin:/usr/lib/w3m/cgi-bin:/usr/local/libexec/w3m/cgi-bin@g' ~/.w3m/config
#         5. sed -i 's@urimethodmap.*@urimethodmap ~/.w3m/urimethodmap, /usr/etc/w3m/urimethodmap@g' ~/.w3m/config

transmission-remote --add "$QUERY_STRING"
printf "%s\r\n" "W3m-control: BACK"
