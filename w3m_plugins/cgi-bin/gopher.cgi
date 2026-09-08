#!/usr/bin/env sh
# AUTHOR: gotbletu (@gmail|twitter|youtube|github|lbry|odysee)
#         https://www.youtube.com/user/gotbletu
# DESC:   gopher web proxy to connect over http
# DEMO:   https://youtu.be/5zDZm6hvbQ8
# REQD:   1. touch ~/.w3m/urimethodmap
#         2. echo "gopher: file:/cgi-bin/gopher.cgi?%s" >> ~/.w3m/urimethodmap
#         3. chmod +x ~/.w3m/cgi-bin/gopher.cgi
#         4. sed -i 's@cgi_bin.*@cgi_bin ~/.w3m/cgi-bin:/usr/lib/w3m/cgi-bin:/usr/local/libexec/w3m/cgi-bin@g' ~/.w3m/config
#         5. sed -i 's@urimethodmap.*@urimethodmap ~/.w3m/urimethodmap, /usr/etc/w3m/urimethodmap@g' ~/.w3m/config
#         6. touch ~/.w3m/siteconf
#         7. echo 'url m!^gopher?://!' >> ~/.w3m/siteconf
#         8. echo 'substitute_url "file:/cgi-bin/gopher.cgi?"' >> ~/.w3m/siteconf

# gopher://bitreich.org/1/lawn
# gopher://hngopher.com/
# gopher://bay.parazy.de:666

proxycheck() { curl --connect-timeout 1 -s -I "$1" | head -n1 | grep 200 > /dev/null && echo $? ;}

if [ "$(proxycheck "https://gopher.floodgap.com/gopher/")" = 0 ]; then
  echo "W3m-control: GOTO https://gopher.floodgap.com/gopher/gw?$QUERY_STRING"
else
  echo "W3m-control: GOTO https://gopherproxy.meulie.net/$QUERY_STRING"
fi
