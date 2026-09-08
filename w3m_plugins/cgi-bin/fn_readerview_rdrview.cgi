#!/usr/bin/env sh
echo "W3m-control: BACK"
echo "W3m-control: READ_SHELL rdrview -H $W3M_URL 2>/dev/null"
echo "W3m-control: VIEW"
echo "W3m-control: DELETE_PREVBUF"
