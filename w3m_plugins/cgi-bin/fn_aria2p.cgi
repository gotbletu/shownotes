#!/usr/bin/env sh
# requires: aria2p (https://github.com/pawamoy/aria2p)
# EXTERN_LINK / $W3M_CURRENT_LINK = under cursor
# EXTERN / $W3M_URL               = current page
echo "W3m-control: BACK"
echo "W3m-control: READ_SHELL aria2p"
echo "W3m-control: BACK"
