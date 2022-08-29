#!/usr/bin/env sh
QUERY_STRING="${QUERY_STRING//+/%20}"
echo "w3m-control: BACK"
echo "w3m-control: TAB_GOTO https://thepiratebay10.org/search/$QUERY_STRING"
