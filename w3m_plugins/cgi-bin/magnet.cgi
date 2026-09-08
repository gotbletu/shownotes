#!/usr/bin/env sh
# AUTHOR: gotbletu (@gmail|twitter|youtube|github|lbry)
#         https://www.youtube.com/user/gotbletu
# DESC:   send magnet links to your torrent client (for W3M Web Browser)
# DEMO:   https://youtu.be/T74FqHMHjN0
# REFF:   decodingurl https://sodocumentation.net/bash/topic/10895/decoding-url
# REQD:   1. touch ~/.w3m/urimethodmap
#         2. echo "magnet: file:/cgi-bin/magnet.cgi?%s" >> ~/.w3m/urimethodmap
#         3. chmod +x ~/.w3m/cgi-bin/magnet.cgi
#         4. sed -i 's@cgi_bin.*@cgi_bin ~/.w3m/cgi-bin:/usr/lib/w3m/cgi-bin:/usr/local/libexec/w3m/cgi-bin@g' ~/.w3m/config
#         5. sed -i 's@urimethodmap.*@urimethodmap ~/.w3m/urimethodmap, /usr/etc/w3m/urimethodmap@g' ~/.w3m/config

# CLOG:   2021-05-22 0.2 decode any encoded url (e.g gopherbay on floodgap web proxy)
#         2021-05-15 0.1 all w3m-control

QUERY_STRING="$(printf "%s" "$QUERY_STRING" | sed -e "s/%\([0-9A-F][0-9A-F]\)/\\\\\x\1/g" | xargs -0 echo -e)"
transmission-remote --add "$QUERY_STRING"
printf "%s\r\n" "W3m-control: BACK"
