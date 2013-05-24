#!/bin/bash
# video demo at: http://www.youtube.com/watch?v=90xoathBYfk

# written by "mhwombat": https://bbs.archlinux.org/viewtopic.php?id=71938&p=2
# Based on "snippy" by "sessy" 
# (https://bbs.archlinux.org/viewtopic.php?id=71938)
#
# This version may be more convenient for people who only need 
# one-line snippets, because all your snippets can go in one file.
#
# You will also need "dmenu", "xsel" and "xdotool". Get them from your linux
# distro in the usual way.
#
# To use:
# 1. Create a file in your home directory called ".snippyrc".
#
# 2. The format of the file is shown below:
#
#        [tag] text_to_paste
#
#    Where "[tag]" starts in column 1. For example:
#
#        [hw] Hello, world!
#        [wombatSmilie] [img]http://nualeargais.ie/pictiuir/emoticons/wombatSmilie.gif[/img]
#
# 3. Bind a convenient key combination to this script.
#
#    TIP: If you're using XMonad, add something like this to xmonad.hs
#      ((mod4Mask, xK_s), spawn "/path/to/snippy")
#
CONFIG=${HOME}/.snippyrc
DMENU_ARGS="-b"
#DMENU_ARGS="-b -p gotbletu$ -fn 10x20"
XSEL_ARGS="--clipboard --input"

# Display the menu and get the selection
SELECTION=`sed 's/\].*/]/' ${CONFIG} | /usr/bin/dmenu ${DMENU_ARGS}`

# Strip out the square brackets...
PATTERN=`echo ${SELECTION} | tr -d "[]"`

# ...and put them back in, escaped with a backslash.
# Get the text associated with the selection.
TEXT=`grep "\[${PATTERN}\]" ~/.snippyrc | sed "s/\[${PATTERN}\] //"`

if [ "${TEXT}" ]; then
  # Put the selected string (without the trailing newline) into the paste buffer.
  echo -n ${TEXT} | xsel ${XSEL_ARGS}
  # Paste into the current application.
  xdotool key ctrl+v		#gui paste
#  xdotool key ctrl+shift+v	#cli
fi
