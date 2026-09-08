#!/usr/bin/env sh
w3m_fnx_clipboard="$(cat /tmp/w3m_fnx_clipboard.txt)"
case "$w3m_fnx_clipboard" in
  *.cgi)  echo "W3m-control: GOTO file:/cgi-bin/$w3m_fnx_clipboard" ;;
  http://*|https://*|www.*|gopher://*|gemini://*)  echo "W3m-control: TAB_GOTO $w3m_fnx_clipboard" ;;
  /*|\~/*)  echo "W3m-control: TAB_GOTO $w3m_fnx_clipboard" ;;
  *)  echo "W3m-control: $w3m_fnx_clipboard" ;;
esac
