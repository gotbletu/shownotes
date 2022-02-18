#!/usr/bin/env sh
# Treat URL-like strings as links in all pages (convert text to url)
echo "W3m-control: SET_OPTION mark_all_pages=toggle"
echo "W3m-control: BACK"
echo "W3m-control: RELOAD"
