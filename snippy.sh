#!/bin/bash
# video demo at: http://www.youtube.com/watch?v=90xoathBYfk

# written by "mhwombat": https://bbs.archlinux.org/viewtopic.php?id=71938&p=2
# Based on "snippy" by "sessy" 
# (https://bbs.archlinux.org/viewtopic.php?id=71938)
#
# You will also need "dmenu", "xsel" and "xdotool". Get them from your linux
# distro in the usual way.
#
# To use:
# 1. Create the directory ~/.snippy
#
# 2. Create a file in that directory for each snippet that you want.
#    The filename will be used as a menu item, so you might want to
#    omit the file extension when you name the file. 
#
#    TIP: If you have a lot of snippets, you can organise them into 
#    subdirectories under ~/.snippy.
#
#    TIP: The contents of the file will be pasted asis, so if you 
#    don't want a newline at the end when the text is pasted, don't
#    put one in the file.
#
# 3. Bind a convenient key combination to this script.
#
#    TIP: If you're using XMonad, add something like this to xmonad.hs
#      ((mod4Mask, xK_s), spawn "/path/to/snippy")
#
DIR=${HOME}/.snippy
DMENU_ARGS="-b"
#DMENU_ARGS="-b -p gotbletu$ -fn 10x20"
XSEL_ARGS="--clipboard --input"

cd ${DIR}

# Use the filenames in the snippy directory as menu entries.
# Get the menu selection from the user.
FILE=`find .  -type f | grep -v '^\.$' | sed 's!\.\/!!' | /usr/bin/dmenu ${DMENU_ARGS}`

if [ -f ${DIR}/${FILE} ]; then
  # Put the contents of the selected file into the paste buffer.
  xsel ${XSEL_ARGS} < ${DIR}/${FILE}
  # Paste into the current application.
  xdotool key ctrl+v		#gui paste
#  xdotool key ctrl+shift+v	#cli
fi
