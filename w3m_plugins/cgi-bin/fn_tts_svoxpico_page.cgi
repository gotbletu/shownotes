#!/usr/bin/env sh
echo "w3m-control: BACK"
echo "w3m-control: READ_SHELL killall picospeaker"
echo "w3m-control: BACK"
echo "w3m-control: READ_SHELL rm /tmp/picospeaker.txt"
echo "w3m-control: BACK"
echo "w3m-control: PRINT /tmp/picospeaker.txt"
echo "w3m-control: READ_SHELL picospeaker < /tmp/picospeaker.txt 2>/dev/null &"
echo "w3m-control: BACK"
