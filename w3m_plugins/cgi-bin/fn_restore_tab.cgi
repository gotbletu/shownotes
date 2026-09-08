#!/usr/bin/env sh
# demo: https://www.youtube.com/watch?v=e5_q3-r6PAU
echo "W3m-control: BACK"
FILE="$HOME/.w3m/RestoreTab.txt"
LAST_TAB=$(tail -n 1 "$FILE")                   # Open the last closed tab
LIMIT=$(tail -n 20 "$FILE")                     # Limit of tabs stored
OTHER_TABS=$(printf "%s" "$LIMIT" | head -n -1)
echo "$OTHER_TABS" > "$FILE"
echo "W3m-control: TAB_GOTO $LAST_TAB"
echo "W3m-control: DELETE_PREVBUF"
