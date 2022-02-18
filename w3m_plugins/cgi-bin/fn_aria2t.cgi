#!/usr/bin/env sh
# requires: aria2t (https://github.com/zsugabubus/aria2t)
# EXTERN_LINK / $W3M_CURRENT_LINK = under cursor
# EXTERN / $W3M_URL               = current page
echo "W3m-control: BACK"
echo "W3m-control: READ_SHELL aria2t"
echo "W3m-control: BACK"
