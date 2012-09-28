# This is the old school aero snap script for linux
# make sure to install wmctrl & xdpyinfo (included in 'x11-utils' package on ubuntu)
# Just make 3 script and make it executable, then make keybinding for each

#--------- Left

#!/bin/bash
WIDTH=`xdpyinfo | grep 'dimensions:' | cut -f 2 -d ':' | cut -f 1 -d 'x' `&& HALF=$(($WIDTH/2)) && wmctrl -r :ACTIVE: -b add,maximized_vert && wmctrl -r :ACTIVE: -e 0,0,0,$HALF,-1

#--------- Right

#!/bin/bash
WIDTH=`xdpyinfo | grep 'dimensions:' | cut -f 2 -d ':' | cut -f 1 -d 'x' `&& HALF=$(($WIDTH/2)) && wmctrl -r :ACTIVE: -b add,maximized_vert && wmctrl -r :ACTIVE: -e 0,$HALF,0,$HALF,-1

#--------- Top

#!/bin/bash
wmctrl -r :ACTIVE: -b add,maximized_vert,maximized_horz
