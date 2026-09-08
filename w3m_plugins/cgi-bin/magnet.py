#!/usr/bin/env python2
# Author: Alexandre Boeglin
# Info: send magnet links to your torrent client
# Source: http://boeglin.org/blog/index.php?entry=Handling-magnet-URIs-with-w3m

########## SETUP ##########################
# 1. touch ~/.w3m/urimethodmap
# 2. echo "magnet: file:/cgi-bin/magnet.py?%s" >> ~/.w3m/urimethodmap
# 3. chmod +x ~/.w3m/cgi-bin/magnet.py
# 4. sed -i 's@cgi_bin.*@cgi_bin ~/.w3m/cgi-bin:/usr/lib/w3m/cgi-bin:/usr/local/libexec/w3m/cgi-bin@g' ~/.w3m/config
# 5. sed -i 's@urimethodmap.*@urimethodmap ~/.w3m/urimethodmap, /usr/etc/w3m/urimethodmap@g' ~/.w3m/config
# 6. edit below ==> cmd_list = ("transmission-remote", "-a", uri)
###########################################

# coding=utf-8
import sys
import os
import subprocess

uri = os.environ.get('QUERY_STRING')
referer = os.environ.get('HTTP_REFERER')

if not uri:
    print
    print "Error: No URI"
    sys.exit()

cmd_list = ("transmission-remote", "-a", uri)

subprocess.call(cmd_list)

if referer:
    print "HTTP/1.1 303 See Other"
    print "Location: %s" % referer

