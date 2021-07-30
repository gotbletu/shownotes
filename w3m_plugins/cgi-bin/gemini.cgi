#!/usr/bin/env sh
# AUTHOR: gotbletu (@gmail|twitter|youtube|github|lbry)
#         https://www.youtube.com/user/gotbletu
# DESC:   gemini proxy to connect over http with w3m web browser
# DEMO:   https://youtu.be/mfnCqn4qhL0
# DEPEND: coreutils curl grep
# REQD:   1. touch ~/.w3m/urimethodmap
#         2. echo "gemini: file:/cgi-bin/gemini.cgi?%s" >> ~/.w3m/urimethodmap
#         3. chmod +x ~/.w3m/cgi-bin/gemini.cgi
#         4. sed -i 's@cgi_bin.*@cgi_bin ~/.w3m/cgi-bin:/usr/lib/w3m/cgi-bin:/usr/local/libexec/w3m/cgi-bin@g' ~/.w3m/config
#         5. sed -i 's@urimethodmap.*@urimethodmap ~/.w3m/urimethodmap, /usr/etc/w3m/urimethodmap@g' ~/.w3m/config
# CLOG:
#         2021-07-30 use curl instead of ping

# gemini://gempaper.strangled.net/mirrorlist/
# gemini://simplynews.metalune.xyz
# gemini://geminispace.info/search?tmux

# remove gemini:// header
QUERY_STRING=$(echo "$QUERY_STRING" | cut -d '/' -f3-)

if [ "$(curl --connect-timeout 1 -s -I "https://portal.mozz.us/about" | head -n1 | grep 200 > /dev/null && echo $? )" = 0 ]; then
  echo "W3m-control: GOTO https://portal.mozz.us/gemini/$QUERY_STRING"
elif [ "$(curl --connect-timeout 1 -s -I "https://proxy.vulpes.one" | head -n1 | grep 200 > /dev/null && echo $? )" = 0 ]; then
  echo "W3m-control: GOTO https://proxy.vulpes.one/gemini/$QUERY_STRING"
else
  echo "W3m-control: GOTO https://gemproxy.koyu.space/$QUERY_STRING"
fi
