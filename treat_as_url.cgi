#!/bin/bash
# by: hola mundo (https://www.youtube.com/channel/UCK9HlJ89BzNYzf7VwwMnv1w)
# reference: http://w3m.sourceforge.net/MANUAL#LocalCGI
# video demo by gotbletu: https://www.youtube.com/watch?v=0Xhvd8ISO8g
# description: make w3m treat all plain text urls as real clickable urls (aka auto mark url)
# note: this script has to be located in the root path /usr/lib/w3m/cgi-bin/treat_as_url.cgi
# install:
#           chmod +x treat_as_url.cgi 
#           sudo cp treat_as_url.cgi /usr/lib/w3m/cgi-bin
#
# newsboat:
#           vim ~/.newsboat/config
#             pager "w3m /usr/lib/w3m/cgi-bin/treat_as_url.cgi %f"
#
# w3m auto mark url in regular files:
#           w3m /usr/lib/w3m/cgi-bin/treat_as_url.cgi filename.txt
#
# w3m auto mark url from websites:
#           w3m /usr/lib/w3m/cgi-bin/treat_as_url.cgi <url>
#
# alias for ~/.bashrc or ~/.zshrc:
# if [ -f "/usr/lib/w3m/cgi-bin/treat_as_url.cgi" ] ; then
#     alias w3m="w3m /usr/lib/w3m/cgi-bin/treat_as_url.cgi"
# fi

printf "%s\r\n" "W3m-control: PREV";
printf "%s\r\n" "W3m-control: MARK_URL"

