#!/bin/bash
#             _   _     _      _         
#  __ _  ___ | |_| |__ | | ___| |_ _   _ 
# / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
#| (_| | (_) | |_| |_) | |  __/ |_| |_| |
# \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
# |___/                                  
#       https://www.youtube.com/user/gotbletu
#       https://twitter.com/gotbletu
#       https://plus.google.com/+gotbletu
#       https://github.com/gotbletu
#       gotbletu@gmail.com


# demo: https://www.youtube.com/watch?v=pWuBTxZbKw4
# info: a script to backup dvd video to ISO, keeping dvd video menu and such in tack.
#       It will use libdvdcss to rip the dvd video if it has copyright protection on it.
# dependencies: dvdbackup libdvdread libdvdcss (cdrtools or cdrkit)

# reference:
# https://wiki.archlinux.org/index.php/dvdbackup
# https://gist.github.com/pwood/462680
# http://linuxcommando.blogspot.com/2014/04/backup-and-playback-dvd-from-hard-drive.html
# https://github.com/joelbassett/ace-encode/blob/master/dvd-rip
# http://joelbassett.github.io/ace-encode/
# http://crunchbang.org/forums/viewtopic.php?id=18298
# https://sourceforge.net/p/dvdauthor/mailman/message/8878064/

DVD_TITLE=$(blkid -o value -s LABEL)
DVD_DEVICE=$(blkid | awk -F':' '{print $1}')

# backup DVD video and show progress bar
# it will save in the current directory
dvdbackup -p -M -v -i "$DVD_DEVICE" -n "$DVD_TITLE"

# create iso from dvdbackup files then cleanup temp files
# note: -V TITLE_IN_CAPS_WO_SPACE is to name the dvdvideo else it will default to "CDROM" when it is mounted
mkisofs -V "$DVD_TITLE" -dvd-video -udf -o "$DVD_TITLE".iso "$DVD_TITLE" \
  && rm -rfv "$DVD_TITLE"


