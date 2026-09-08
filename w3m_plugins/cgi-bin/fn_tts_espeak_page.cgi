#!/usr/bin/env sh
echo "w3m-control: BACK"
echo "w3m-control: READ_SHELL killall espeak-ng"
echo "w3m-control: BACK"
echo "w3m-control: READ_SHELL rm /tmp/espeak-ng.txt"
echo "w3m-control: BACK"
echo "w3m-control: PRINT /tmp/espeak-ng.txt"
echo "w3m-control: READ_SHELL espeak-ng -f /tmp/espeak-ng.txt &"
echo "w3m-control: BACK"
