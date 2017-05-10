#!/usr/bin/env bash
# author: unknown
# sentby: MoreChannelNoise (https://www.youtube.com/user/MoreChannelNoise)
# editby: gotbletu (https://www.youtube.com/user/gotbletu)

# demo: https://www.youtube.com/watch?v=kxJClZIXSnM
# info: this is a script to launch other rofi scripts,
#       saves us the trouble of binding multiple hotkeys for each script,
#       when we can just use one hotkey for everything.

declare -A LABELS
declare -A COMMANDS

###
# List of defined 'bangs'

# launch programs
COMMANDS["apps"]="rofi -combi-modi window,drun -show combi"
LABELS["apps"]=""

# open bookmarks
COMMANDS["bookmarks"]="~/.scripts/rofi-scripts-collection/rofi-surfraw-bookmarks.sh"
LABELS["bookmarks"]=""

# search local files
COMMANDS["locate"]="~/.scripts/rofi-scripts-collection/rofi-locate.sh"
LABELS["locate"]=""

# open custom web searches
COMMANDS["websearch"]="~/.scripts/rofi-scripts-collection/rofi-surfraw-websearch.sh"
LABELS["websearch"]=""

# show clipboard history
# source: https://bitbucket.org/pandozer/rofi-clipboard-manager/overview
# COMMANDS["clipboard"]='rofi -modi "clipboard:~/.bin/rofi-clipboard-manager/mclip.py menu" -show clipboard && ~/.bin/rofi-clipboard-manager/mclip.py paste'
# LABELS["clipboard"]=""

# references --------------------------
# COMMANDS[";sr2"]="chromium 'wikipedia.org/search-redirect.php?search=\" \${input}\""
# LABELS[";sr2"]=""

# COMMANDS[";piratebay"]="chromium --disk-cache-dir=/tmp/cache http://thepiratebay.org/search/\" \${input}\""
# LABELS[";piratebay"]=""

# COMMANDS[".bin"]="spacefm -r '/home/dka/bin'"
# LABELS[".bin"]=".bin"

# COMMANDS["#screenshot"]='/home/dka/bin/screenshot-scripts/myscreenshot.sh'
# LABELS["#screenshot"]="screenshot"

################################################################################
# do not edit below
################################################################################
##
# Generate menu
##
function print_menu()
{
    for key in ${!LABELS[@]}
    do
  echo "$key    ${LABELS}"
     #   echo "$key    ${LABELS[$key]}"
     # my top version just shows the first field in labels row, not two words side by side
    done
}
##
# Show rofi.
##
function start()
{
    # print_menu | rofi -dmenu -p "?=>" 
    print_menu | sort | rofi -dmenu -mesg ">>> launch your collection of rofi scripts" -i -p "rofi-bangs: "

}


# Run it
value="$(start)"

# Split input.
# grab upto first space.
choice=${value%%\ *}
# graph remainder, minus space.
input=${value:$((${#choice}+1))}

##
# Cancelled? bail out
##
if test -z ${choice}
then
    exit
fi

# check if choice exists
if test ${COMMANDS[$choice]+isset}
then
    # Execute the choice
    eval echo "Executing: ${COMMANDS[$choice]}"
    eval ${COMMANDS[$choice]}
else
 eval  $choice | rofi
 # prefer my above so I can use this same script to also launch apps like geany or leafpad etc (DK) 
 #   echo "Unknown command: ${choice}" | rofi -dmenu -p "error"
fi
