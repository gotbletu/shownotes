#!/usr/bin/env sh
echo "W3m-control: READ_SHELL curl -s dict://dict.org/d:$W3M_CURRENT_WORD"
echo "W3m-control: DELETE_PREVBUF"
echo "W3m-control: REDRAW"
