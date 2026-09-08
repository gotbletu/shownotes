#!/usr/bin/env sh
echo "W3m-control: BACK"
echo "W3m-control: READ_SHELL readable $W3M_URL -p html-title,html-content 2>/dev/null"
echo "W3m-control: VIEW"
echo "W3m-control: DELETE_PREVBUF"

