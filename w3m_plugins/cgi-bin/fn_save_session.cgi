#!/usr/bin/env sh
# demo: https://www.youtube.com/watch?v=qYhNJ3itqWw
echo "W3m-control: BACK"
saving_session="$HOME/.w3m/RestoreSession.txt"
echo "W3m-control: EXTERN echo %s > $saving_session"
# loop save URL of all tabs
n=0
while [ "$n" -lt 30 ]; do
  n=$(( n + 1 ))
  echo "W3m-control: NEXT_TAB"
  echo "W3m-control: EXTERN echo %s >> $saving_session"
done
# generate a script; run 'w3mlastsession' command in terminal to restore session
echo "W3m-control: READ_SHELL ~/.w3m/cgi-bin/restore_session.cgi"
echo "W3m-control: BACK"
echo "W3m-control: QUIT"
