#!/usr/bin/env sh
# AUTHOR: gotbletu (@gmail|twitter|youtube|github|lbry)

helpmsg() {
  printf "%s\n" "desc: reset usb device without unplugging"
  printf "%s\n" "demo: https://youtu.be/SiupVru0I1s"
  printf "%s\n" "depend: usbreset (https://github.com/jkulesza/usbreset"
  printf "%s\n" "                 (https://marc.info/?l=linux-usb&m=121459435621262&w=2)"
  printf "%s\n" "                 (https://askubuntu.com/a/661)"
  printf "%s\n" "        fzf      (optional)"
  printf "\n"
  printf "%s\n" "fzfmode: ${0##*/}"
  printf "%s\n" "usage: ${0##*/} <BUS_NUM> <DEVICE_NUM>"
  printf "\n"
  printf "%s\n" "  $ lsusb"
  printf "%s\n" "      Bus 006 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub"
  printf "%s\n" "      Bus 011 Device 003: ID 0a5c:21e8 Broadcom Corp. BCM20702A0 Bluetooth 4.0"
  printf "%s\n" "      Bus 011 Device 005: ID 04d9:2519 Holtek Semiconductor, Inc. Shenzhen LogoTech 2.4GHz receiver"
  printf "\n"
  printf "%s\n" "  $ ${0##*/} 011 005"
}

if [ $# -lt 1 ]; then
  # fzf mode
  USBHW=$(lsusb | fzf)
  [ -z "$USBHW" ] && exit
  BUS=$(printf "%s" "$USBHW" | awk '{print $2}')
  DEVICE=$(printf "%s" "$USBHW" | awk '{print $4}' | sed 's/://g')
  sudo usbreset /dev/bus/usb/"$BUS"/"$DEVICE"
elif [ $# -lt 2 ] || [ "$1" = -h ] || [ "$1" = --help ]; then
  helpmsg
  exit
else
  # commandline mode
  BUS="$1"
  DEVICE="$2"
  sudo usbreset /dev/bus/usb/"$BUS"/"$DEVICE"
fi
