#!/usr/bin/env sh
echo "w3m-control: BACK"
echo "w3m-control: READ_SHELL killall festival"
echo "w3m-control: BACK"
echo "w3m-control: READ_SHELL rm /tmp/festival.txt"
echo "w3m-control: BACK"
echo "w3m-control: PRINT /tmp/festival.txt"
echo "w3m-control: READ_SHELL festival --tts /tmp/festival.txt &"
echo "w3m-control: BACK"
