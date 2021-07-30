#!/usr/bin/env sh
# AUTHOR: gotbletu (@gmail|twitter|youtube|github|lbry)
#         https://www.youtube.com/user/gotbletu
# DESC:   gemini proxy to connect over http with w3m web browser
# DEMO:   https://youtu.be/mfnCqn4qhL0
# DEPEND: iputils coreutils
# REQD:   1. touch ~/.w3m/urimethodmap
#         2. echo "gemini: file:/cgi-bin/gemini.cgi?%s" >> ~/.w3m/urimethodmap
#         3. chmod +x ~/.w3m/cgi-bin/gemini.cgi
#         4. sed -i 's@cgi_bin.*@cgi_bin ~/.w3m/cgi-bin:/usr/lib/w3m/cgi-bin:/usr/local/libexec/w3m/cgi-bin@g' ~/.w3m/config
#         5. sed -i 's@urimethodmap.*@urimethodmap ~/.w3m/urimethodmap, /usr/etc/w3m/urimethodmap@g' ~/.w3m/config

# gemini://gempaper.strangled.net/mirrorlist/
# gemini://simplynews.metalune.xyz
# gemini://geminispace.info/search?tmux

# remove gemini:// header
QUERY_STRING=$(echo "$QUERY_STRING" | cut -d '/' -f3-)

# skip to next proxy if slow or test fails
if [ "$(timeout 1 ping -c 1 proxy.vulpes.one > /dev/null && echo $? )" = 0 ]; then
  echo "W3m-control: GOTO https://proxy.vulpes.one/gemini/$QUERY_STRING"
elif [ "$(timeout 1 ping -c 1 gemproxy.koyu.space > /dev/null && echo $? )" = 0 ]; then
  echo "W3m-control: GOTO https://gemproxy.koyu.space/$QUERY_STRING"
else
  echo "W3m-control: GOTO https://portal.mozz.us/gemini/$QUERY_STRING"
fi
