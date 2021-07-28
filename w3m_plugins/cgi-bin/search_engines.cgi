#!/usr/bin/env sh
# AUTHOR: gotbletu (@gmail|twitter|youtube|github|lbry|odysee)
#         https://www.youtube.com/user/gotbletu
# DESC:   w3m search engine alias (aka omnibar smart keywords search)
# DEMO:   https://youtu.be/bWlPpacFPlI
#         W3M Playlist https://www.youtube.com/playlist?list=PLqv94xWU9zZ35Yv0s6zMID5JoS8qu19Kh
# REFF:   https://github.com/felipesaa/A-vim-like-firefox-like-configuration-for-w3m/blob/master/cgi-bin/search_engines.cgi
#         https://github.com/felipesaa/A-vim-like-firefox-like-configuration-for-w3m/blob/master/documentation/search_engines.txt
#         https://github.com/felipesaa/A-vim-like-firefox-like-configuration-for-w3m/blob/master/urimethodmap
#         frakswe search surfraw urimethodmap https://pastebin.com/raw/TUcRgu9y
#         https://rubikitch.hatenadiary.org/entry/20070830/searchengine
# REQD:   1. touch ~/.w3m/urimethodmap
#         2. $EDITOR ~/.w3m/urimethodmap
#             # search engine alias
#             # note: no trailing space after %s
#             1x: file:/cgi-bin/search_engines.cgi?%s
#             dd: file:/cgi-bin/search_engines.cgi?%s
#             gg: file:/cgi-bin/search_engines.cgi?%s
#             gs: file:/cgi-bin/search_engines.cgi?%s
#             pb: file:/cgi-bin/search_engines.cgi?%s
#             rd: file:/cgi-bin/search_engines.cgi?%s
#             wi: file:/cgi-bin/search_engines.cgi?%s
#             v2: file:/cgi-bin/search_engines.cgi?%s
#             ya: file:/cgi-bin/search_engines.cgi?%s
#             yt: file:/cgi-bin/search_engines.cgi?%s
#         3. chmod +x ~/.w3m/cgi-bin/search_engines.cgi
#         4. sed -i 's@cgi_bin.*@cgi_bin ~/.w3m/cgi-bin:/usr/lib/w3m/cgi-bin:/usr/local/libexec/w3m/cgi-bin@g' ~/.w3m/config
#         5. sed -i 's@urimethodmap.*@urimethodmap ~/.w3m/urimethodmap, /usr/etc/w3m/urimethodmap@g' ~/.w3m/config
#         6. sed -i 's@space_autocomplete.*@space_autocomplete 0@g' ~/.w3m/config
# USAGE:  <SearchEngine>:<Keywords>
#         1. $ w3m -v
#         2. press Shift-u (the default GOTO key) to access the addressbar
#         3. press Ctrl-u to clear addressbar
#         4. to search duckduckgo type in dd:cool linux wallpapers
#         5. to search google type in gg:cool anime wallpapers
# CLI:    $ w3m dd:archlinux
#         $ w3m ya:debian,stable,iso
#         $ w3m "gg:linux mint iso download"
# CLOG:   
#         2021-07-28 add comma as space holder for cli (eg $ w3m ya:debian,stable,iso )
#         2021-07-24 remove semicolon requirements, use spaces instead by enabling (space_autocomplete 0)
#                    add optional direct cli usage info
#         2021-05-24 turn @felipesaa script into posix, use case statement looks prettier

# search engine alias
PREFIX=$(echo "$QUERY_STRING" | cut -d ':' -f1)

# user input keywords
INPUT=$(echo "$QUERY_STRING" | cut -d ':' -f2- | sed 's/,/%20/g')

# check if w3m version has native gopher support
GOPHER_PROTOCOL_ENABLE=$(w3m -version | grep -c "gopher")

case $PREFIX in
  1x)
    echo "W3m-control: GOTO https://1337x.to/search/$INPUT/1/"
    ;;
  dd)
    echo "W3m-control: GOTO https://lite.duckduckgo.com/lite/?q=$INPUT&kf=-1&kz=-1&kq=-1&kv=-1&k1=-1&kp=-2&kaf=1&kd=-1&kf=-1&kz=-1&kq=-1&kv=-1"
    ;;
  gg)
    echo "W3m-control: GOTO https://www.google.com/search?q=$INPUT"
    ;;
  gs)
    echo "W3m-control: GOTO https://portal.mozz.us/gemini/geminispace.info/search%3F$INPUT"
    ;;
  pb)
    echo "W3m-control: GOTO https://thepiratebay10.org/search/$INPUT"
    ;;
  rd) # goto a subreddit by name
    echo "W3m-control: GOTO https://www.reddit.com/r/$INPUT/.mobile"
    ;;
  wi)
    echo "W3m-control: GOTO https://en.wikipedia.org/w/index.php?search=$INPUT&title=Special%3ASearch&profile=default&fulltext=1&ns0=1"
    ;;
  v2) # veronica-2 search gopherspace (use web proxy if no native support)
    if [ "$GOPHER_PROTOCOL_ENABLE" = 0 ] ; then
      echo "W3m-control: GOTO https://gopher.floodgap.com/gopher/gw?ss=gopher%3A%2F%2Fgopher.floodgap.com%2F7%2Fv2%2Fvs&sq=$INPUT"
    else
      echo "W3m-control: GOTO gopher://gopher.floodgap.com/7/v2/vs?$INPUT"
    fi
    ;;
  ya)
    echo "W3m-control: GOTO https://search.yahoo.com/search?p=$INPUT"
    ;;
  yt) # youtube via invidious (more instances @ https://redirect.invidious.io )
    echo "W3m-control: GOTO https://yewtu.be/search?q=$INPUT"
    ;;
esac

# delete temp buffer
echo "W3m-control: DELETE_PREVBUF"
