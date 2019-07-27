#!/usr/bin/env bash
###             _   _     _      _         
###  __ _  ___ | |_| |__ | | ___| |_ _   _ 
### / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
###| (_| | (_) | |_| |_) | |  __/ |_| |_| |
### \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
### |___/                                  
###       https://www.youtube.com/user/gotbletu
###       https://twitter.com/gotbletu
###       https://github.com/gotbletu
###       gotbletu@gmail.com
###
### Author          : gotbletu
### Name            : mountjutsu
### Version         : 0.2
### Date            : 20190626
### Description     : menu interface to mount, unmount, eject, clone, exactcopy, format, LUKS encryption
### Depends On      : bash  sudo  grep  gawk  coreutils  udisks2  util-linux
###                   gptfdisk  dosfstools  ntfs-3g  hfsprogs  exfat-utils  e2fsprogs
###                   cryptsetup  clonezilla  partclone  partimage  vlc  cdw  f3  smartmontools
###                   dvdbackup  libdvdread  libdvdcss  cdrdao  cdrtools(or cdrkit)
### Video Demo      : https://www.youtube.com/watch?v=jipILuNW5Ks

#-------- Bash Color Code {{{
#------------------------------------------------------
# DESC: color code for bash compatible shell
# LINK: https://wiki.archlinux.org/index.php?title=Bash/Prompt_customization&oldid=419076#List_of_colors_for_prompt_and_Bash

# Reset
Color_Off='\e[0m'       # Text Reset

# Regular Colors
Black='\e[0;30m'        # Black
Red='\e[0;31m'          # Red
Green='\e[0;32m'        # Green
Yellow='\e[0;33m'       # Yellow
Blue='\e[0;34m'         # Blue
Purple='\e[0;35m'       # Purple
Cyan='\e[0;36m'         # Cyan
White='\e[0;37m'        # White

# }}}
#-------- Mount Device (udisksctl) {{{
#------------------------------------------------------
mount-udisksctl() {
  if [ $# -lt 1 ]; then
    echo -e "mount device like most GUI file manager"
    echo -e "\nUsage: $0 <device|partition>"
    echo -e "Example: $0 sdx"
    echo -e "         $0 sdx1"
    echo -e "Multiple:$0 sdx sdy sdz"
    echo -e "         $0 sdx*"
    return 1
  fi
  myArray=( "$@" )
  for arg in "${myArray[@]}"; do
    udisksctl mount -b /dev/"$arg"
  done
}

unmount-udisksctl() {
  if [ $# -lt 1 ]; then
    echo -e "mount device like most GUI file manager"
    echo -e "\nUsage: $0 <device|partition>"
    echo -e "Example: $0 sdx"
    echo -e "         $0 sdx1"
    echo -e "Multiple:$0 sdx sdy sdz"
    echo -e "         $0 sdx*"
    return 1
  fi
  myArray=( "$@" )
  for arg in "${myArray[@]}"; do
    udisksctl unmount --force -b /dev/"$arg"
  done
}
# }}}
#-------- Mount LUKS {{{
#------------------------------------------------------
mount-udisksctl-luks() {
  if [ $# -lt 1 ]
  then
    echo -e "mount LUKS encrypted device like most GUI file manager"
    echo -e "\nUsage: $0 <luks-device|partition>"
    echo -e "Example: $0 sdx"
    echo -e "         $0 sdx1"
    echo -e "Multiple:$0 sdx sdy sdz"
    echo -e "         $0 sdx*"
    return 1
  fi
  myArray=( "$@" )
  for arg in "${myArray[@]}"; do
    udisksctl unlock -b /dev/"$arg"
    sleep 0.1
    dm_mountpoint=$(lsblk -o "KNAME,NAME" | grep -A 1 "$arg" | tail -1 | awk '{print $1}')
    udisksctl mount -b /dev/"$dm_mountpoint"
  done
}

unmount-udisksctl-luks() {
  if [ $# -lt 1 ]
  then
    echo -e "unmount LUKS encrypted device like most GUI file manager"
    echo -e "\nUsage: $0 <luks-device|partition>"
    echo -e "Example: $0 sdx"
    echo -e "         $0 sdx1"
    echo -e "Multiple:$0 sdx sdy sdz"
    echo -e "         $0 sdx*"
    return 1
  fi
  myArray=( "$@" )
  for arg in "${myArray[@]}"; do
    dm_mountpoint=$(lsblk -o "KNAME,NAME" | grep -A 1 "$arg" | tail -1 | awk '{print $1}')
    udisksctl unmount --force -b /dev/"$dm_mountpoint"
    udisksctl lock -b /dev/"$arg"
  done
}

mount-luks() {
  if [ $# -lt 1 ]; then
    echo -e "mount LUKS disk encrypted device"
    echo -e "\nUsage: $0 <luks-device|partition>"
    echo -e "Example: $0 sdX"
    echo -e "         $0 sdX1"
    echo -e "Multiple:$0 sdx sdy sdz"
    echo -e "         $0 sdx*"
    return 1
  fi
  myArray=( "$@" )
  for arg in "${myArray[@]}"; do
    mappername="$arg"
    sudo cryptsetup luksOpen /dev/"$arg" "$mappername"
    mkdir -p /tmp/"$arg"
    sudo mount /dev/mapper/"$mappername" /tmp/"$arg"
  done
}

unmount-luks() {
  if [ $# -lt 1 ]; then
    echo -e "unmount LUKS disk encrypted device"
    echo -e "\nUsage: $0 <luks-device|partition>"
    echo -e "Example: $0 sdX"
    echo -e "         $0 sdX1"
    echo -e "Multiple:$0 sdx sdy sdz"
    echo -e "         $0 sdx*"
    return 1
  fi
  myArray=( "$@" )
  for arg in "${myArray[@]}"; do
    mappername="$arg"
    sudo umount /tmp/"$arg"
    sudo cryptsetup luksClose "$mappername"
    rmdir "/tmp/$arg"
  done
}

# }}}
#-------- Eject Device {{{
#------------------------------------------------------
eject-udisksctl() {
  if [ $# -lt 1 ]
  then
    echo -e "mount using gvfs"
    echo -e "\nUsage:\n$0 <disc_image>"
    echo -e "\nExample:\n$0 disc_image.iso"
    echo -e "$0 disc_image.iso disc_image2.bin disc_image3.mdf"
    echo -e "$0 *.iso"
    return 1
  fi
  myArray=( "$@" )
  for arg in "${myArray[@]}"; do
    udisksctl power-off -b /dev/"$arg"
  done
}

# }}}
#-------- Format USB v4 (MBR 2TB Max) [last updated February 03, 2018]  {{{
#------------------------------------------------------
# DEMO: https://www.youtube.com/watch?v=7txO1cdNJsQ
# DESC: format USB and create a single partition

format2usb-ext() {
  if [ $# -lt 3 ]; then
    echo -e "format and create a partition that fills up the whole device"
    echo -e "\nUsage: $0 <filesystem:ext2|ext3|ext4> <device_label> <device_name>"
    echo -e "Example: $0 ext2 MY_USB sdx"
    echo -e "         $0 ext3 MY_USB sdx"
    echo -e "         $0 ext4 MY_USB sdx"
    return 1
  fi
  FSTYPE="$1"
  DEVICE_LABEL="$2"
  DEVICE_NAME="$3"
  echo -e "${Yellow}>>>Checking if device is mounted ${Color_Off}"
    MOUNT_STATUS=$(mount | grep /dev/"$DEVICE_NAME" | wc -l)
    if [ "$MOUNT_STATUS" -ne 0 ]
    then
      lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$DEVICE_NAME"
      echo -e "${Red}>>>/dev/$DEVICE_NAME is mounted. You have to unmount the device and all of its partitions then try again ${Color_Off}"
      return 1
    fi
  echo -e "${Yellow}>>>Please double check the device you are about to FORMAT ${Color_Off}"
    lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep --color -E "$DEVICE_NAME|$"
  echo -ne "${Red}>>>WARNING: You are about to FORMAT a device at /dev/$DEVICE_NAME. Do you want to continue? [y/n] ${Color_Off}"
    read REPLY
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
      echo -e "${Green}>>>You chose to continue ${Color_Off}"
    else
      return 1
    fi
  echo -e "${Red}>>>Delete any existing partition then create a new single partition ${Color_Off}"
    echo -e "d\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\no\nn\np\n1\n\n\nw" | sudo fdisk /dev/"$DEVICE_NAME"
    # delete partiton x8 using d\n\n
    # d    delete a partition
    #      default, partition
    # o    create a new empty DOS partition table
    # n    add a new partition
    # p    print the partition table
    # 1    partition number 1
    #      default, start immediately after preceding partition
    #      default, extend partition to end of disk
    # w    write table to disk and exit
  echo -e "${Red}>>>Formatting the device ${Color_Off}"
    echo -e "y\n" | sudo mkfs."$FSTYPE" -L "$DEVICE_LABEL" /dev/"$DEVICE_NAME"1
  echo -e "${Yellow}>>>Changing permission of the filesystem ${Color_Off}"
    mkdir -p -v /tmp/testmount
    sudo mount /dev/"$DEVICE_NAME"1 /tmp/testmount
    sudo chmod -R 777 /tmp/testmount
  echo -e "${Green}>>>Change EXT filesystem 5% reserved space to 0% (increase storage space) ${Color_Off}"
    MOUNTED_TESTMOUNT=$(df | awk '/testmount/ {print $1}')
    sudo tune2fs -m 0 "$MOUNTED_TESTMOUNT"
    sudo tune2fs -l "$MOUNTED_TESTMOUNT" | grep --color=auto 'Reserved block count'
  echo -e "${Red}>>>Unmounting and cleanup ${Color_Off}"
    sudo umount /tmp/testmount
    rmdir -v /tmp/testmount
}

format2usb-fat32-32kbcluster() {
  if [ $# -lt 2 ]; then
    echo -e "format device to work with wii & gamecube games using FAT32 with 32KB cluster"
    echo -e "FAT32 label max is 11 character and is all uppercase"
    echo -e "(512 bytes per sector * 64 sectors per cluster)/ 1024 Bytes = 32KB clusters (32768 Bytes)"
    echo -e "more info: https://gist.github.com/joshenders/4376942"
    echo -e "\nUsage: $0 <label> <device>"
    echo -e "Example: $0 MY_USB sdx"
    return 1
  fi
  # fat32 likes the labels to be in uppercase
  DEVICE_LABEL=$(echo "$1" | tr '[:lower:]' '[:upper:]')
  DEVICE_NAME="$2"
  echo -e "${Yellow}>>>Checking if device is mounted ${Color_Off}"
    MOUNT_STATUS=$(mount | grep /dev/"$DEVICE_NAME" | wc -l)
    if [ "$MOUNT_STATUS" -ne 0 ]
    then
      lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$DEVICE_NAME"
      echo -e "${Red}>>>/dev/$DEVICE_NAME is mounted. You have to unmount the device and all of its partitions then try again ${Color_Off}"
      return 1
    fi
  echo -e "${Yellow}>>>Please double check the device you are about to FORMAT ${Color_Off}"
    lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep --color -E "$2|$"
  echo -ne "${Red}>>>WARNING: You are about to FORMAT a device at /dev/$DEVICE_NAME. Do you want to continue? [y/n] ${Color_Off}"
    read REPLY
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
      echo -e "${Green}>>>You chose to continue ${Color_Off}"
    else
      return 1
    fi
  echo -e "${Red}>>>Delete any existing partition then create a new single partition ${Color_Off}"
    echo -e "d\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\no\nn\np\n1\n\n\nt\nb\nw" | sudo fdisk /dev/"$DEVICE_NAME"
    # delete partiton x8 using d\n\n
    # d    delete a partition
    #      default, partition
    # o    create a new empty DOS partition table
    # n    add a new partition
    # p    print the partition table
    # 1    partition number 1
    #      default, start immediately after preceding partition
    #      default, extend partition to end of disk
    # t    change a partition type (L to list all types)
    # b    W95 FAT32
    # w    write table to disk and exit
  echo -e "${Red}>>>Formatting the device ${Color_Off}"
    sudo mkfs.fat -S 512 -s 64 -F 32 -n "$DEVICE_LABEL" -I /dev/"$DEVICE_NAME"1
  echo -e "${Red}>>>Changing permission of the filesystem ${Color_Off}"
    mkdir -p -v /tmp/testmount
    sudo mount /dev/"$DEVICE_NAME"1 /tmp/testmount
    sudo chmod -R 777 /tmp/testmount
    sudo umount /tmp/testmount
    rmdir -v /tmp/testmount
}

format2usb-fat32-64kbcluster() {
  if [ $# -lt 2 ]; then
    echo -e "format device to work with few gaming consoles using FAT32 with 64KB cluster"
    echo -e "FAT32 label max is 11 character and is all uppercase"
    echo -e "(512 bytes per sector * 128 sectors per cluster) / 1024 Bytes  = 64KB clusters (65536 Bytes)"
    echo -e "more info: https://gist.github.com/joshenders/4376942"
    echo -e "https://askubuntu.com/a/190033"
    echo -e "\nUsage: $0 <label> <device>"
    echo -e "Example: $0 MY_USB sdx"
    return 1
  fi
  # fat32 likes the labels to be in uppercase
  DEVICE_LABEL=$(echo "$1" | tr '[:lower:]' '[:upper:]')
  DEVICE_NAME="$2"
  echo -e "${Yellow}>>>Checking if device is mounted ${Color_Off}"
    MOUNT_STATUS=$(mount | grep /dev/"$DEVICE_NAME" | wc -l)
    if [ "$MOUNT_STATUS" -ne 0 ]
    then
      lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$DEVICE_NAME"
      echo -e "${Red}>>>/dev/$DEVICE_NAME is mounted. You have to unmount the device and all of its partitions then try again ${Color_Off}"
      return 1
    fi
  echo -e "${Yellow}>>>Please double check the device you are about to FORMAT ${Color_Off}"
    lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep --color -E "$2|$"
  echo -ne "${Red}>>>WARNING: You are about to FORMAT a device at /dev/$DEVICE_NAME. Do you want to continue? [y/n] ${Color_Off}"
    read REPLY
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
      echo -e "${Green}>>>You chose to continue ${Color_Off}"
    else
      return 1
    fi
  echo -e "${Red}>>>Delete any existing partition then create a new single partition ${Color_Off}"
    echo -e "d\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\no\nn\np\n1\n\n\nt\nb\nw" | sudo fdisk /dev/"$DEVICE_NAME"
    # delete partiton x8 using d\n\n
    # d    delete a partition
    #      default, partition
    # o    create a new empty DOS partition table
    # n    add a new partition
    # p    print the partition table
    # 1    partition number 1
    #      default, start immediately after preceding partition
    #      default, extend partition to end of disk
    # t    change a partition type (L to list all types)
    # b    W95 FAT32
    # w    write table to disk and exit
  echo -e "${Red}>>>Formatting the device ${Color_Off}"
    sudo mkfs.fat -S 512 -s 128 -F 32 -n "$DEVICE_LABEL" -I /dev/"$DEVICE_NAME"1
  echo -e "${Red}>>>Changing permission of the filesystem ${Color_Off}"
    mkdir -p -v /tmp/testmount
    sudo mount /dev/"$DEVICE_NAME"1 /tmp/testmount
    sudo chmod -R 777 /tmp/testmount
    sudo umount /tmp/testmount
    rmdir -v /tmp/testmount
}

format2usb-exfat() {
  if [ $# -lt 2 ]; then
    echo -e "format and create a partition that fills up the whole device"
    echo -e "exFAT label max is 15 character and is all uppercase"
    echo -e "\nUsage: $0 <label> <device>"
    echo -e "Example: $0 MY_USB sdx"
    return 1
  fi
  # exFat likes the labels to be in uppercase
  DEVICE_LABEL=$(echo "$1" | tr '[:lower:]' '[:upper:]')
  DEVICE_NAME="$2"
  echo -e "${Yellow}>>>Checking if device is mounted ${Color_Off}"
    MOUNT_STATUS=$(mount | grep /dev/"$DEVICE_NAME" | wc -l)
    if [ "$MOUNT_STATUS" -ne 0 ]
    then
      lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$DEVICE_NAME"
      echo -e "${Red}>>>/dev/$DEVICE_NAME is mounted. You have to unmount the device and all of its partitions then try again ${Color_Off}"
      return 1
    fi
  echo -e "${Yellow}>>>Please double check the device you are about to FORMAT ${Color_Off}"
    lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep --color -E "$2|$"
  echo -ne "${Red}>>>WARNING: You are about to FORMAT a device at /dev/$DEVICE_NAME. Do you want to continue? [y/n] ${Color_Off}"
    read REPLY
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
      echo -e "${Green}>>>You chose to continue ${Color_Off}"
    else
      return 1
    fi
  echo -e "${Red}>>>Delete any existing partition then create a new single partition ${Color_Off}"
    echo -e "d\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\no\nn\np\n1\n\n\nt\n7\nw" | sudo fdisk /dev/"$DEVICE_NAME"
    # delete partiton x8 using d\n\n
    # d    delete a partition
    #      default, partition
    # o    create a new empty DOS partition table
    # n    add a new partition
    # p    print the partition table
    # 1    partition number 1
    #      default, start immediately after preceding partition
    #      default, extend partition to end of disk
    # t    change a partition type (L to list all types)
    # 7    HPFS/NTFS/exFAT
    # w    write table to disk and exit
  echo -e "${Red}>>>Formatting the device ${Color_Off}"
    sudo mkfs.exfat -n "$DEVICE_LABEL" /dev/"$DEVICE_NAME"1
  echo -e "${Red}>>>Changing permission of the filesystem ${Color_Off}"
    mkdir -p -v /tmp/testmount
    sudo mount /dev/"$DEVICE_NAME"1 /tmp/testmount
    sudo chmod -R 777 /tmp/testmount
    sudo umount /tmp/testmount
    rmdir -v /tmp/testmount
}

format2usb-fat16() {
  if [ $# -lt 2 ]; then
    echo -e "format and create a partition that fills up the whole device"
    echo -e "FAT16 label max is 11 character and is all uppercase"
    echo -e "\nUsage: $0 <label> <device>"
    echo -e "Example: $0 MY_USB sdx"
    return 1
  fi
  # fat32 likes the labels to be in uppercase
  DEVICE_LABEL=$(echo "$1" | tr '[:lower:]' '[:upper:]')
  DEVICE_NAME="$2"
  echo -e "${Yellow}>>>Checking if device is mounted ${Color_Off}"
    MOUNT_STATUS=$(mount | grep /dev/"$DEVICE_NAME" | wc -l)
    if [ "$MOUNT_STATUS" -ne 0 ]
    then
      lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$DEVICE_NAME"
      echo -e "${Red}>>>/dev/$DEVICE_NAME is mounted. You have to unmount the device and all of its partitions then try again ${Color_Off}"
      return 1
    fi
  echo -e "${Yellow}>>>Please double check the device you are about to FORMAT ${Color_Off}"
    lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep --color -E "$2|$"
  echo -ne "${Red}>>>WARNING: You are about to FORMAT a device at /dev/$DEVICE_NAME. Do you want to continue? [y/n] ${Color_Off}"
    read REPLY
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
      echo -e "${Green}>>>You chose to continue ${Color_Off}"
    else
      return 1
    fi
  echo -e "${Red}>>>Delete any existing partition then create a new single partition ${Color_Off}"
    echo -e "d\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\no\nn\np\n1\n\n\nt\ne\nw" | sudo fdisk /dev/"$DEVICE_NAME"
    # delete partiton x8 using d\n\n
    # d    delete a partition
    #      default, partition
    # o    create a new empty DOS partition table
    # n    add a new partition
    # p    primary
    # 1    partition number 1
    #      default, first sector
    #      default, last sector
    # t    change a partition type (L to list all types)
    # e    W95 FAT16
    # w    write table to disk and exit
  echo -e "${Red}>>>Formatting the device ${Color_Off}"
    sudo mkfs.fat -F 16 -n "$DEVICE_LABEL" -I /dev/"$DEVICE_NAME"1
  echo -e "${Red}>>>Changing permission of the filesystem ${Color_Off}"
    mkdir -p -v /tmp/testmount
    sudo mount /dev/"$DEVICE_NAME"1 /tmp/testmount
    sudo chmod -R 777 /tmp/testmount
    sudo umount /tmp/testmount
    rmdir -v /tmp/testmount
}

format2usb-fat32() {
  if [ $# -lt 2 ]; then
    echo -e "format and create a partition that fills up the whole device"
    echo -e "FAT32 label max is 11 character and is all uppercase"
    echo -e "\nUsage: $0 <label> <device>"
    echo -e "Example: $0 MY_USB sdx"
    return 1
  fi
  # fat32 likes the labels to be in uppercase
  DEVICE_LABEL=$(echo "$1" | tr '[:lower:]' '[:upper:]')
  DEVICE_NAME="$2"
  echo -e "${Yellow}>>>Checking if device is mounted ${Color_Off}"
    MOUNT_STATUS=$(mount | grep /dev/"$DEVICE_NAME" | wc -l)
    if [ "$MOUNT_STATUS" -ne 0 ]
    then
      lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$DEVICE_NAME"
      echo -e "${Red}>>>/dev/$DEVICE_NAME is mounted. You have to unmount the device and all of its partitions then try again ${Color_Off}"
      return 1
    fi
  echo -e "${Yellow}>>>Please double check the device you are about to FORMAT ${Color_Off}"
    lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep --color -E "$2|$"
  echo -ne "${Red}>>>WARNING: You are about to FORMAT a device at /dev/$DEVICE_NAME. Do you want to continue? [y/n] ${Color_Off}"
    read REPLY
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
      echo -e "${Green}>>>You chose to continue ${Color_Off}"
    else
      return 1
    fi
  echo -e "${Red}>>>Delete any existing partition then create a new single partition ${Color_Off}"
    echo -e "d\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\no\nn\np\n1\n\n\nt\nb\nw" | sudo fdisk /dev/"$DEVICE_NAME"
    # delete partiton x8 using d\n\n
    # d    delete a partition
    #      default, partition
    # o    create a new empty DOS partition table
    # n    add a new partition
    # p    print the partition table
    # 1    partition number 1
    #      default, start immediately after preceding partition
    #      default, extend partition to end of disk
    # t    change a partition type (L to list all types)
    # b    W95 FAT32
    # w    write table to disk and exit
  echo -e "${Red}>>>Formatting the device ${Color_Off}"
    sudo mkfs.fat -F 32 -n "$DEVICE_LABEL" -I /dev/"$DEVICE_NAME"1
  echo -e "${Red}>>>Changing permission of the filesystem ${Color_Off}"
    mkdir -p -v /tmp/testmount
    sudo mount /dev/"$DEVICE_NAME"1 /tmp/testmount
    sudo chmod -R 777 /tmp/testmount
    sudo umount /tmp/testmount
    rmdir -v /tmp/testmount
}

format2usb-ntfs() {
  if [ $# -lt 2 ]; then
    echo -e "format and create a partition that fills up the whole device"
    echo -e "\nUsage: $0 <label> <device>"
    echo -e "Example: $0 MY_USB sdx"
    return 1
  fi
  DEVICE_LABEL="$1"
  DEVICE_NAME="$2"
  echo -e "${Yellow}>>>Checking if device is mounted ${Color_Off}"
    MOUNT_STATUS=$(mount | grep /dev/"$DEVICE_NAME" | wc -l)
    if [ "$MOUNT_STATUS" -ne 0 ]
    then
      lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$DEVICE_NAME"
      echo -e "${Red}>>>/dev/$DEVICE_NAME is mounted. You have to unmount the device and all of its partitions then try again ${Color_Off}"
      return 1
    fi
  echo -e "${Yellow}>>>Please double check the device you are about to FORMAT ${Color_Off}"
    lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep --color -E "$DEVICE_NAME|$"
  echo -ne "${Red}>>>WARNING: You are about to FORMAT a device at /dev/$DEVICE_NAME. Do you want to continue? [y/n] ${Color_Off}"
    read REPLY
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
      echo -e "${Green}>>>You chose to continue ${Color_Off}"
    else
      return 1
    fi
  echo -e "${Red}>>>Delete any existing partition then create a new single partition ${Color_Off}"
    echo -e "d\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\no\nn\np\n1\n\n\nt\n7\nw" | sudo fdisk /dev/"$DEVICE_NAME"
    # delete partiton x8 using d\n\n
    # d    delete a partition
    #      default, partition
    # o    create a new empty DOS partition table
    # n    add a new partition
    # p    print the partition table
    # 1    partition number 1
    #      default, start immediately after preceding partition
    #      default, extend partition to end of disk
    # t    change a partition type (L to list all types)
    # 7    HPFS/NTFS/exFAT
    # w    write table to disk and exit
  echo -e "${Red}>>>Formatting the device ${Color_Off}"
    sudo mkfs.ntfs -f -L "$DEVICE_LABEL" /dev/"$DEVICE_NAME"1
  echo -e "${Red}>>>Changing permission of the filesystem ${Color_Off}"
    mkdir -p -v /tmp/testmount
    sudo mount /dev/"$DEVICE_NAME"1 /tmp/testmount
    sudo chmod -R 777 /tmp/testmount
    sudo umount /tmp/testmount
    rmdir -v /tmp/testmount
}

format2usb-hfsplus-nonjournal() {
  if [ $# -lt 2 ]; then
    echo -e "format and create a partition that fills up the whole device"
    echo -e "\nUsage: $0 <label> <device>"
    echo -e "Example: $0 MY_USB sdx"
    return 1
  fi
  DEVICE_LABEL="$1"
  DEVICE_NAME="$2"
  echo -e "${Yellow}>>>Checking if device is mounted ${Color_Off}"
    MOUNT_STATUS=$(mount | grep /dev/"$DEVICE_NAME" | wc -l)
    if [ "$MOUNT_STATUS" -ne 0 ]
    then
      lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$DEVICE_NAME"
      echo -e "${Red}>>>/dev/$DEVICE_NAME is mounted. You have to unmount the device and all of its partitions then try again ${Color_Off}"
      return 1
    fi
  echo -e "${Yellow}>>>Please double check the device you are about to FORMAT ${Color_Off}"
    lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep --color -E "$DEVICE_NAME|$"
  echo -ne "${Red}>>>WARNING: You are about to FORMAT a device at /dev/$DEVICE_NAME. Do you want to continue? [y/n] ${Color_Off}"
    read REPLY
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
      echo -e "${Green}>>>You chose to continue ${Color_Off}"
    else
      return 1
    fi
  echo -e "${Red}>>>Delete any existing partition then create a new single partition ${Color_Off}"
    echo -e "d\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\no\nn\np\n1\n\n\nt\naf\nw" | sudo fdisk /dev/"$DEVICE_NAME"
    # delete partiton x8 using d\n\n
    # d    delete a partition
    #      default, partition
    # o    create a new empty DOS partition table
    # n    add a new partition
    # p    primary
    # 1    partition number 1
    #      default, first sector
    #      default, last sector
    # t    change a partition type (L to list all types)
    # af   HFS / HFS+
    # w    write table to disk and exit
  echo -e "${Red}>>>Formatting the device ${Color_Off}"
    sudo mkfs.hfsplus -v "$DEVICE_LABEL" /dev/"$DEVICE_NAME"1
  echo -e "${Red}>>>Changing permission of the filesystem ${Color_Off}"
    mkdir -p -v /tmp/testmount
    sudo mount /dev/"$DEVICE_NAME"1 /tmp/testmount
    sudo chmod -R 777 /tmp/testmount
    sudo umount /tmp/testmount
    rmdir -v /tmp/testmount
}


# }}}
#-------- GPT Format USB (HDD Greater Than 2TB ) [last updated February 04, 2018]  {{{
#------------------------------------------------------
# DEMO: https://www.youtube.com/watch?v=7txO1cdNJsQ
# DESC: format USB and create a single partition
# REFF: https://www.funtoo.org/Partitioning_using_gdisk
#       https://matthew.komputerwiz.net/2015/12/13/formatting-universal-drive.html

#-------- gdisk Hex code GUID GPT {{{
#------------------------------------------------------
# o      create a new empty GUID partition table (GPT)
# y      yes, proceed
# n      add a new partition
# 1      partition number 1
#        default, first sector
#        default, last sector
# 0700   Hex code or GUID (0700 Microsoft basic data)
# w      write table to disk and exit
# y      yes, proceed

# Hex code or GUID (L to show codes, Enter = 8300): L
# 0700 Microsoft basic data  0c01 Microsoft reserved    2700 Windows RE
# 3000 ONIE boot             3001 ONIE config           3900 Plan 9
# 4100 PowerPC PReP boot     4200 Windows LDM data      4201 Windows LDM metadata
# 4202 Windows Storage Spac  7501 IBM GPFS              7f00 ChromeOS kernel
# 7f01 ChromeOS root         7f02 ChromeOS reserved     8200 Linux swap
# 8300 Linux filesystem      8301 Linux reserved        8302 Linux /home
# 8303 Linux x86 root (/)    8304 Linux x86-64 root (/  8305 Linux ARM64 root (/)
# 8306 Linux /srv            8307 Linux ARM32 root (/)  8400 Intel Rapid Start
# 8e00 Linux LVM             a000 Android bootloader    a001 Android bootloader 2
# a002 Android boot          a003 Android recovery      a004 Android misc
# a005 Android metadata      a006 Android system        a007 Android cache
# a008 Android data          a009 Android persistent    a00a Android factory
# a00b Android fastboot/ter  a00c Android OEM           a500 FreeBSD disklabel
# a501 FreeBSD boot          a502 FreeBSD swap          a503 FreeBSD UFS
# a504 FreeBSD ZFS           a505 FreeBSD Vinum/RAID    a580 Midnight BSD data
# a581 Midnight BSD boot     a582 Midnight BSD swap     a583 Midnight BSD UFS
# a584 Midnight BSD ZFS      a585 Midnight BSD Vinum    a600 OpenBSD disklabel
# a800 Apple UFS             a901 NetBSD swap           a902 NetBSD FFS
# a903 NetBSD LFS            a904 NetBSD concatenated   a905 NetBSD encrypted
# a906 NetBSD RAID           ab00 Recovery HD           af00 Apple HFS/HFS+
# af01 Apple RAID            af02 Apple RAID offline    af03 Apple label
# af04 AppleTV recovery      af05 Apple Core Storage    af06 Apple SoftRAID Statu
# af07 Apple SoftRAID Scrat  af08 Apple SoftRAID Volum  af09 Apple SoftRAID Cache
# b300 QNX6 Power-Safe       bc00 Acronis Secure Zone   be00 Solaris boot
# bf00 Solaris root          bf01 Solaris /usr & Mac Z  bf02 Solaris swap
# bf03 Solaris backup        bf04 Solaris /var          bf05 Solaris /home
# bf06 Solaris alternate se  bf07 Solaris Reserved 1    bf08 Solaris Reserved 2
# bf09 Solaris Reserved 3    bf0a Solaris Reserved 4    bf0b Solaris Reserved 5
# c001 HP-UX data            c002 HP-UX service         e100 ONIE boot
# e101 ONIE config           ea00 Freedesktop $BOOT     eb00 Haiku BFS
# ed00 Sony system partitio  ed01 Lenovo system partit  ef00 EFI System
# ef01 MBR partition scheme  ef02 BIOS boot partition   f800 Ceph OSD
# f801 Ceph dm-crypt OSD     f802 Ceph journal          f803 Ceph dm-crypt journa
# f804 Ceph disk in creatio  f805 Ceph dm-crypt disk i  fb00 VMWare VMFS
# fb01 VMWare reserved       fc00 VMWare kcore crash p  fd00 Linux RAID
# }}}

format2gpt-ext() {
  if [ $# -lt 3 ]; then
    echo -e "format and create a partition that fills up the whole device"
    echo -e "\nUsage: $0 <filesystem:ext2|ext3|ext4> <device_label> <device_name>"
    echo -e "Example: $0 ext2 MY_USB sdx"
    echo -e "         $0 ext3 MY_USB sdx"
    echo -e "         $0 ext4 MY_USB sdx"
    return 1
  fi
  FSTYPE="$1"
  DEVICE_LABEL="$2"
  DEVICE_NAME="$3"
  echo -e "${Yellow}>>>Checking if device is mounted ${Color_Off}"
    MOUNT_STATUS=$(mount | grep /dev/"$DEVICE_NAME" | wc -l)
    if [ "$MOUNT_STATUS" -ne 0 ]
    then
      lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$DEVICE_NAME"
      echo -e "${Red}>>>/dev/$DEVICE_NAME is mounted. You have to unmount the device and all of its partitions then try again ${Color_Off}"
      return 1
    fi
  echo -e "${Yellow}>>>Please double check the device you are about to FORMAT ${Color_Off}"
    lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep --color -E "$DEVICE_NAME|$"
  echo -ne "${Red}>>>WARNING: You are about to FORMAT a device at /dev/$DEVICE_NAME. Do you want to continue? [y/n] ${Color_Off}"
    read REPLY
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
      echo -e "${Green}>>>You chose to continue ${Color_Off}"
    else
      return 1
    fi
  echo -e "${Red}>>>Delete any existing partition then create a new single partition ${Color_Off}"
    echo -e "o\ny\nn\n1\n\n\n8300\nw\ny\n" | sudo gdisk /dev/"$DEVICE_NAME"
    # o      create a new empty GUID partition table (GPT) [Delete All Partition]
    # y      yes, proceed
    # n      add a new partition
    # 1      partition number 1
    #        default, first sector
    #        default, last sector
    # 8300   Hex code or GUID [8300 Linux filesystem]
    # w      write table to disk and exit
    # y      yes, proceed
  echo -e "${Red}>>>Formatting the device ${Color_Off}"
    echo -e "y\n" | sudo mkfs."$FSTYPE" -L "$DEVICE_LABEL" /dev/"$DEVICE_NAME"1
  echo -e "${Yellow}>>>Changing permission of the filesystem ${Color_Off}"
    mkdir -p -v /tmp/testmount
    sudo mount /dev/"$DEVICE_NAME"1 /tmp/testmount
    sudo chmod -R 777 /tmp/testmount
  echo -e "${Green}>>>Change EXT filesystem 5% reserved space to 0% (increase storage space) ${Color_Off}"
    MOUNTED_TESTMOUNT=$(df | awk '/testmount/ {print $1}')
    sudo tune2fs -m 0 "$MOUNTED_TESTMOUNT"
    sudo tune2fs -l "$MOUNTED_TESTMOUNT" | grep --color=auto 'Reserved block count'
  echo -e "${Red}>>>Unmounting and cleanup ${Color_Off}"
    sudo umount /tmp/testmount
    rmdir -v /tmp/testmount
}

format2gpt-exfat() {
  if [ $# -lt 2 ]; then
    echo -e "format and create a partition that fills up the whole device"
    echo -e "exFAT label max is 15 character and is all uppercase"
    echo -e "\nUsage: $0 <label> <device>"
    echo -e "Example: $0 MY_USB sdx"
    return 1
  fi
  # exFat likes the labels to be in uppercase
  DEVICE_LABEL=$(echo "$1" | tr '[:lower:]' '[:upper:]')
  DEVICE_NAME="$2"
  echo -e "${Yellow}>>>Checking if device is mounted ${Color_Off}"
    MOUNT_STATUS=$(mount | grep /dev/"$DEVICE_NAME" | wc -l)
    if [ "$MOUNT_STATUS" -ne 0 ]
    then
      lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$DEVICE_NAME"
      echo -e "${Red}>>>/dev/$DEVICE_NAME is mounted. You have to unmount the device and all of its partitions then try again ${Color_Off}"
      return 1
    fi
  echo -e "${Yellow}>>>Please double check the device you are about to FORMAT ${Color_Off}"
    lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep --color -E "$2|$"
  echo -ne "${Red}>>>WARNING: You are about to FORMAT a device at /dev/$DEVICE_NAME. Do you want to continue? [y/n] ${Color_Off}"
    read REPLY
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
      echo -e "${Green}>>>You chose to continue ${Color_Off}"
    else
      return 1
    fi
  echo -e "${Red}>>>Delete any existing partition then create a new single partition ${Color_Off}"
    echo -e "o\ny\nn\n1\n\n\n0700\nw\ny\n" | sudo gdisk /dev/"$DEVICE_NAME"
    # o      create a new empty GUID partition table (GPT) [Delete All Partition]
    # y      yes, proceed
    # n      add a new partition
    # 1      partition number 1
    #        default, first sector
    #        default, last sector
    # 0700   Hex code or GUID [0700 Microsoft basic data]
    # w      write table to disk and exit
    # y      yes, proceed
  echo -e "${Red}>>>Formatting the device ${Color_Off}"
    sudo mkfs.exfat -n "$DEVICE_LABEL" /dev/"$DEVICE_NAME"1
  echo -e "${Red}>>>Changing permission of the filesystem ${Color_Off}"
    mkdir -p -v /tmp/testmount
    sudo mount /dev/"$DEVICE_NAME"1 /tmp/testmount
    sudo chmod -R 777 /tmp/testmount
    sudo umount /tmp/testmount
    rmdir -v /tmp/testmount
}

format2gpt-fat32() {
  if [ $# -lt 2 ]; then
    echo -e "format and create a partition that fills up the whole device"
    echo -e "FAT32 label max is 11 character and is all uppercase"
    echo -e "\nUsage: $0 <label> <device>"
    echo -e "Example: $0 MY_USB sdx"
    return 1
  fi
  # fat32 likes the labels to be in uppercase
  DEVICE_LABEL=$(echo "$1" | tr '[:lower:]' '[:upper:]')
  DEVICE_NAME="$2"
  echo -e "${Yellow}>>>Checking if device is mounted ${Color_Off}"
    MOUNT_STATUS=$(mount | grep /dev/"$DEVICE_NAME" | wc -l)
    if [ "$MOUNT_STATUS" -ne 0 ]
    then
      lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$DEVICE_NAME"
      echo -e "${Red}>>>/dev/$DEVICE_NAME is mounted. You have to unmount the device and all of its partitions then try again ${Color_Off}"
      return 1
    fi
  echo -e "${Yellow}>>>Please double check the device you are about to FORMAT ${Color_Off}"
    lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep --color -E "$2|$"
  echo -ne "${Red}>>>WARNING: You are about to FORMAT a device at /dev/$DEVICE_NAME. Do you want to continue? [y/n] ${Color_Off}"
    read REPLY
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
      echo -e "${Green}>>>You chose to continue ${Color_Off}"
    else
      return 1
    fi
  echo -e "${Red}>>>Delete any existing partition then create a new single partition ${Color_Off}"
    echo -e "o\ny\nn\n1\n\n\n0700\nw\ny\n" | sudo gdisk /dev/"$DEVICE_NAME"
    # o      create a new empty GUID partition table (GPT) [Delete All Partition]
    # y      yes, proceed
    # n      add a new partition
    # 1      partition number 1
    #        default, first sector
    #        default, last sector
    # 0700   Hex code or GUID [0700 Microsoft basic data]
    # w      write table to disk and exit
    # y      yes, proceed
  echo -e "${Red}>>>Formatting the device ${Color_Off}"
    sudo mkfs.fat -F 32 -n "$DEVICE_LABEL" -I /dev/"$DEVICE_NAME"1
  echo -e "${Red}>>>Changing permission of the filesystem ${Color_Off}"
    mkdir -p -v /tmp/testmount
    sudo mount /dev/"$DEVICE_NAME"1 /tmp/testmount
    sudo chmod -R 777 /tmp/testmount
    sudo umount /tmp/testmount
    rmdir -v /tmp/testmount
}

format2gpt-ntfs() {
  if [ $# -lt 2 ]; then
    echo -e "format and create a partition that fills up the whole device"
    echo -e "\nUsage: $0 <label> <device>"
    echo -e "Example: $0 MY_USB sdx"
    return 1
  fi
  DEVICE_LABEL="$1"
  DEVICE_NAME="$2"
  echo -e "${Yellow}>>>Checking if device is mounted ${Color_Off}"
    MOUNT_STATUS=$(mount | grep /dev/"$DEVICE_NAME" | wc -l)
    if [ "$MOUNT_STATUS" -ne 0 ]
    then
      lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$DEVICE_NAME"
      echo -e "${Red}>>>/dev/$DEVICE_NAME is mounted. You have to unmount the device and all of its partitions then try again ${Color_Off}"
      return 1
    fi
  echo -e "${Yellow}>>>Please double check the device you are about to FORMAT ${Color_Off}"
    lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep --color -E "$DEVICE_NAME|$"
  echo -ne "${Red}>>>WARNING: You are about to FORMAT a device at /dev/$DEVICE_NAME. Do you want to continue? [y/n] ${Color_Off}"
    read REPLY
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
      echo -e "${Green}>>>You chose to continue ${Color_Off}"
    else
      return 1
    fi
  echo -e "${Red}>>>Delete any existing partition then create a new single partition ${Color_Off}"
    echo -e "o\ny\nn\n1\n\n\n0700\nw\ny\n" | sudo gdisk /dev/"$DEVICE_NAME"
    # o      create a new empty GUID partition table (GPT) [Delete All Partition]
    # y      yes, proceed
    # n      add a new partition
    # 1      partition number 1
    #        default, first sector
    #        default, last sector
    # 0700   Hex code or GUID [0700 Microsoft basic data]
    # w      write table to disk and exit
    # y      yes, proceed
  echo -e "${Red}>>>Formatting the device ${Color_Off}"
    sudo mkfs.ntfs -f -L "$DEVICE_LABEL" /dev/"$DEVICE_NAME"1
  echo -e "${Red}>>>Changing permission of the filesystem ${Color_Off}"
    mkdir -p -v /tmp/testmount
    sudo mount /dev/"$DEVICE_NAME"1 /tmp/testmount
    sudo chmod -R 777 /tmp/testmount
    sudo umount /tmp/testmount
    rmdir -v /tmp/testmount
}

# }}}
#-------- LUKS Disk Encryption (Linux Unified Key Setup) v2 (last update October 23, 2016) {{{
#------------------------------------------------------
# DEMO:
# DESC: setup password protection and disk encryption on storage media
# LINK: https://gitlab.com/cryptsetup/cryptsetup
luks-setup-ext() {
  if [ $# -lt 1 ]; then
    echo -e "format device and apply LUKS disk encryption (Linux Unified Key Setup)"
    echo -e "\nUsage: $0 <fstype:ext2/3/4> <device|partition>"
    echo -e "Example: $0 ext2 sdx"
    echo -e "         $0 ext4 sdx1"
    return 1
  fi
  FSTYPE="$1"
  DEVICE_NAME="$2"
  MAPPERNAME="$DEVICE_NAME"
  echo -e "${Yellow}>>>Checking if device is mounted ${Color_Off}"
    MOUNT_STATUS=$(mount | grep /dev/"$DEVICE_NAME" | wc -l)
    if [ "$MOUNT_STATUS" -ne 0 ]
    then
      lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$DEVICE_NAME"
      echo -e "${Red}>>>/dev/$DEVICE_NAME is mounted. You have to unmount the device then try again ${Color_Off}"
      return 1
    fi
  echo -e "${Yellow}>>>Please double check the device you are about to FORMAT ${Color_Off}"
    lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep --color -E "$DEVICE_NAME|$"
  echo -ne "${Red}>>>WARNING: You are about to FORMAT a device at /dev/$DEVICE_NAME. Do you want to continue? [y/n] ${Color_Off}"
    read REPLY
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
      echo -e "${Green}>>>You chose to continue ${Color_Off}"
    else
      return 1
    fi
  echo -e "${Yellow}>>>Setting up LUKS encryption ${Color_Off}"
    sudo cryptsetup -y -v luksFormat /dev/"$DEVICE_NAME"
    sudo cryptsetup luksOpen /dev/"$DEVICE_NAME" "$MAPPERNAME"
  echo -e "${Red}>>>Formatting device ${Color_Off}"
    sudo mkfs."$FSTYPE" /dev/mapper/"$MAPPERNAME"
  echo -e "${Yellow}>>>Changing permission of the filesystem ${Color_Off}"
    mkdir -p -v /tmp/testluks
    sudo mount /dev/mapper/"$MAPPERNAME" /tmp/testluks
    sudo chmod -R 777 /tmp/testluks
  echo -e "${Green}>>>Change EXT filesystem 5% reserved space to 0% (increase storage space) ${Color_Off}"
    MOUNTED_TESTLUKS=$(df | awk '/testluks/ {print $1}')
    sudo tune2fs -m 0 "$MOUNTED_TESTLUKS"
    sudo tune2fs -l "$MOUNTED_TESTLUKS" | grep --color=auto 'Reserved block count'
  echo -e "${Red}>>>Unmounting and cleanup ${Color_Off}"
    sudo umount /tmp/testluks
    sudo cryptsetup luksClose "$MAPPERNAME"
    rmdir -v /tmp/testluks
}

# }}}
#-------- Clonezilla CLI (Clone and Restore Image) {{{
#------------------------------------------------------
### Full Disk Clone and Restore
clonezilla-disk-cloning() {
  if [ $# -lt 3 ]; then
    echo -e "clone full disk to image"
    echo -e "\nUsage: $0 <output_file> <device> <path>"
    echo -e "\nExample: $0 mydesktop sdx /home/user"
    echo -e "\nNote: <output_file> will be saved to your current path"
    return 1
  fi
  OUTPUT_FILE="$1_clonezilla_disk_`date +'%Y_%m_%d'`"
  DEVICE_NAME="$2"
  OUTPUT_PATH="$3"
  echo -e "${Yellow}>>>Checking if device is mounted ${Color_Off}"
    MOUNT_STATUS=$(mount | grep /dev/"$DEVICE_NAME" | wc -l)
    if [ "$MOUNT_STATUS" -ne 0 ]
    then
      lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$DEVICE_NAME"
      echo -e "${Red}>>>/dev/$DEVICE_NAME is mounted. You have to unmount the device and all of its partitions then try again ${Color_Off}"
      return 1
    fi
  echo -e "${Blue}>>>Set current output path to $OUTPUT_PATH ${Color_Off}"
    sudo sed -i 's:ocsroot=.*:ocsroot='\""$OUTPUT_PATH"\"':g' /etc/drbl/drbl.conf
  echo -e "${Green}>>>Start full disk cloning process ${Color_Off}"
  echo -e "${Green}>>>$OUTPUT_FILE image will be saved to $OUTPUT_PATH ${Color_Off}"
    sudo ocs-sr -q2 -c -j2 -z1p -i 5000000 -sc -p true savedisk "$OUTPUT_FILE" "$DEVICE_NAME"
  echo -e "${Red}>>>Changing permission of $OUTPUT_FILE image ${Color_Off}"
    sudo chmod -R 777 "$OUTPUT_PATH/$OUTPUT_FILE"
}

clonezilla-disk-restore() {
  if [ $# -lt 2 ]; then
    echo -e "restore full disk image to device"
    echo -e "\nUsage: $0 <input_file> <device>"
    echo -e "\nExample: $0 mydesktop_clonezilla_disk_2016_07_02 sdx"
    return 1
  fi
  INPUT_FILE="$1"
  DEVICE_NAME="$2"
  echo -e "${Yellow}>>>Checking if device is mounted ${Color_Off}"
    MOUNT_STATUS=$(mount | grep /dev/"$DEVICE_NAME" | wc -l)
    if [ "$MOUNT_STATUS" -ne 0 ]
    then
      lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$DEVICE_NAME"
      echo -e "${Red}>>>/dev/$DEVICE_NAME is mounted. You have to unmount the device and all of its partitions then try again ${Color_Off}"
      return 1
    fi
  echo -e "${Green}>>>Start full disk restore process ${Color_Off}"
    sudo /usr/sbin/ocs-sr -g auto -e1 auto -e2 -c -r -j2 -p true restoredisk "$INPUT_FILE" "$DEVICE_NAME"
}

### Partition Clone and Restore
clonezilla-partition-cloning() {
  if [ $# -lt 3 ]; then
    echo -e "clone device partition to image"
    echo -e "\nUsage: $0 <output_file> <device> <path>"
    echo -e "\nExample: $0 mylaptop sdx2 /home/user"
    echo -e "\nNote: <output_file> will be saved to your current path"
    return 1
  fi
  OUTPUT_FILE="$1_clonezilla_part${PART_NUM}_`date +'%Y_%m_%d'`"
  DEVICE_NAME="$2"
  OUTPUT_PATH="$3"
  PART_NUM=$(echo "$2" | sed 's/[^0-9]*//g')
  echo -e "${Yellow}>>>Checking if device is mounted ${Color_Off}"
    MOUNT_STATUS=$(mount | grep /dev/"$DEVICE_NAME" | wc -l)
    if [ "$MOUNT_STATUS" -ne 0 ]
    then
      lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$DEVICE_NAME"
      echo -e "${Red}>>>/dev/$DEVICE_NAME is mounted. You have to unmount then try again ${Color_Off}"
      return 1
    fi
  echo -e "${Blue}>>>Set current output path to $OUTPUT_PATH ${Color_Off}"
    sudo sed -i 's:ocsroot=.*:ocsroot='\""$OUTPUT_PATH"\"':g' /etc/drbl/drbl.conf
  echo -e "${Green}>>>Start partition cloning process ${Color_Off}"
  echo -e "${Green}>>>$OUTPUT_FILE image will be saved to $OUTPUT_PATH ${Color_Off}"
    sudo /usr/sbin/ocs-sr -q2 -c -j2 -z1p -i 5000000 -sc -p true saveparts "$OUTPUT_FILE" "$DEVICE_NAME"
  echo -e "${Red}>>>Changing permission of $OUTPUT_FILE image ${Color_Off}"
    sudo chmod -R 777 "$OUTPUT_PATH/$OUTPUT_FILE"
}

clonezilla-partition-restore() {
  if [ $# -lt 2 ]; then
    echo -e "restore image to device partition"
    echo -e "\nUsage: $0 <input_file> <device>"
    echo -e "\nExample: $0 mylaptop_clonezilla_partition2_2016_07_02 sdx2"
    echo -e "\nNote: partition <device> usually have numbers at the end (sdx1)"
    return 1
  fi
  INPUT_FILE="$1"
  DEVICE_NAME="$2"
  echo -e "${Yellow}>>>Checking if device is mounted ${Color_Off}"
    MOUNT_STATUS=$(mount | grep /dev/"$DEVICE_NAME" | wc -l)
    if [ "$MOUNT_STATUS" -ne 0 ]
    then
      lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$DEVICE_NAME"
      echo -e "${Red}>>>/dev/$DEVICE_NAME is mounted. You have to unmount then try again ${Color_Off}"
      return 1
    fi
  echo -e "${Green}>>>Start partition restore process ${Color_Off}"
    sudo /usr/sbin/ocs-sr -g auto -e1 auto -e2 -c -r -j2 -k -p true restoreparts "$INPUT_FILE" "$DEVICE_NAME"
}


# }}}
#-------- Copying Disc Media CD / DVD / BluRay {{{
#------------------------------------------------------
# DEMO: https://www.youtube.com/watch?v=pWuBTxZbKw4
# LINK: http://dvdbackup.sourceforge.net/
# REFF: https://wiki.archlinux.org/index.php/dvdbackup
#       https://gist.github.com/pwood/462680
#       http://linuxcommando.blogspot.com/2014/04/backup-and-playback-dvd-from-hard-drive.html
#       https://github.com/joelbassett/ace-encode/blob/master/dvd-rip
#       http://joelbassett.github.io/ace-encode/
#       http://crunchbang.org/forums/viewtopic.php?id=18298
#       https://sourceforge.net/p/dvdauthor/mailman/message/8878064/


exactcopy-dvdmovie() {
  if [ $# -lt 1 ]; then
    echo -e "backup dvd video to iso, keeping dvd video menu and title in tack."
    echo -e "libdvdcss will be used to rip the dvd video if it has copyright protection on it."
    echo -e "\nUsage: $0 <save-path>"
    echo -e "\nExample:\n$0 ."
    echo -e "$0 /home/user/Videos"
    echo -e "\ndemo: https://www.youtube.com/watch?v=pWuBTxZbKw4"
    echo -e "dependencies: dvdbackup gawk libdvdread libdvdcss (cdrtools or cdrkit)"
    return 1
  fi
  # reference:

  # location to save dvd iso output
  cd "$1"

  DISC_TITLE=$(blkid -o value -s LABEL)
  DISC_DEVICE=$(blkid | awk -F':' '{print $1}')

  # backup DVD video and show progress bar
  # it will save in the current directory
  dvdbackup --progress --mirror --verbose --input="$DISC_DEVICE" --name="$DISC_TITLE"

  # create iso from dvdbackup files then cleanup temp files
  # note: -V TITLE_IN_CAPS_WO_SPACE is to name the dvdvideo else it will default to "CDROM" when it is mounted
  mkisofs -V "$DISC_TITLE" -dvd-video -udf -o "$DISC_TITLE".iso "$DISC_TITLE" \
    && rm -rfv "$DISC_TITLE"

  # eject dvd
  eject "$DISC_DEVICE"

  echo -e "${Green}>>> DVD ISO Outputed To: $PWD/$DISC_TITLE.iso ${Color_Off}"
}

# REFF: https://askubuntu.com/questions/147800/ripping-dvd-to-iso-accurately
#       https://linux.101hacks.com/unix/create-iso-file-from-cd-dvd/
#       https://www.cyberciti.biz/tips/linux-creating-cd-rom-iso-image.html
exactcopy-datadisc() {
  if [ $# -lt 1 ]; then
    echo -e "backup cd/dvd/bluray data disc to iso"
    echo -e "\nUsage: $0 <save-path>"
    echo -e "\nExample:\n$0 ."
    echo -e "$0 /home/user/ISO"
    echo -e "dependencies: util-linux gawk coreutils (cdrtools or cdrkit)"
    return 1
  fi
  DISC_TITLE=$(blkid -o value -s LABEL)
  DISC_DEVICE=$(blkid | awk -F':' '{print $1}')
  BLOCK_SIZE=$(isoinfo -d -i "$DISC_DEVICE" | awk -F: '/block size/ {print $2}' | awk '{$1=$1};1')
  VOLUME_SIZE=$(isoinfo -d -i "$DISC_DEVICE" | awk -F: '/Volume size/ {print $2}' | awk '{$1=$1};1')

  # location to save iso output
  cd "$1"

  # auto get disc location, title, blocksize, volume size... this might take a few minutes to gather information
  # then start copying disc to iso
  dd if="$DISC_DEVICE" of="$DISC_TITLE".iso bs="$BLOCK_SIZE" count="$VOLUME_SIZE" status=progress

  # eject disc
  eject "$DISC_DEVICE"

  echo -e "${Green}>>>ISO Outputed To: $PWD/$DISC_TITLE.iso ${Color_Off}"
}


# Avoid using ISO: Audio CD has multiple tracks, ISO is single track only, it cannot handle multiple tracks
# https://wiki.archlinux.org/index.php/Rip_Audio_CDs#Creating_bin.2Fcue_files_from_CD
# https://ubuntuforums.org/showthread.php?t=1287829&p=8084611#post8084611
# https://www.togaware.com/linux/survivor/Duplicate_Audio.html
# https://help.ubuntu.com/community/cdrdao#Doing_it_the_hard_way
exactcopy-audiocd() {
  if [ $# -lt 1 ]; then
    echo -e "backup cd/dvd/bluray data disc to iso"
    echo -e "\nUsage: $0 <save-path>"
    echo -e "\nExample:\n$0 ."
    echo -e "$0 /home/user/ISO"
    echo -e "dependencies: util-linux gawk coreutils (cdrtools or cdrkit)"
    return 1
  fi
  DISC_TITLE=$(blkid -o value -s LABEL)
  DISC_DEVICE=$(blkid | awk -F':' '{print $1}')
  BLOCK_SIZE=$(isoinfo -d -i "$DISC_DEVICE" | awk -F: '/block size/ {print $2}' | awk '{$1=$1};1')
  VOLUME_SIZE=$(isoinfo -d -i "$DISC_DEVICE" | awk -F: '/Volume size/ {print $2}' | awk '{$1=$1};1')

  # location to save iso output
  cd "$1"

  # auto get disc location, title, blocksize, volume size... this might take a few minutes to gather information
  # then start copying disc to iso
  # dd if="$DISC_DEVICE" of="$DISC_TITLE".iso bs="$BLOCK_SIZE" count="$VOLUME_SIZE" status=progress
  cdrdao read-cd --read-raw --datafile cdimage.bin cdimage.cue

  # eject disc
  eject "$DISC_DEVICE"

  echo -e "${Green}>>>BIN/CUE Image Outputed To: $PWD/$DISC_TITLE.iso ${Color_Off}"
}
# }}}
#-------- Smartctl - Check Hard Drive Health (last update March 27, 2017) {{{
#------------------------------------------------------
# S.M.A.R.T. is the abbreviation for "Self Monitoring And Reporting Technology"
# It is a standard interface protocol and set of the disk features that allows disk to check its status and report it to a host system
# references:
# https://www.smartmontools.org/browser/trunk/smartmontools/smartctl.8.in
# https://en.wikipedia.org/wiki/S.M.A.R.T.#ATA_S.M.A.R.T._attributes
# http://www.z-a-recovery.com/manual/smart.aspx
# https://ddumont.wordpress.com/2010/03/15/workaround-for-aborted-smart-test-for-seagate-disk/

smartctl-conveyancetest() {
  if [ $# -lt 1 ]; then
    echo -e "perform conveyance test to check hard drive health (usually 5mins)"
    echo -e "not all drives has this testing feature"
    echo -e "\nUsage: $0 <device>"
    echo -e "Example: $0 sdx"
    return 1
  fi
  sudo smartctl -t conveyance /dev/"$1"
}

smartctl-extendedtest() {
  if [ $# -lt 1 ]; then
    echo -e "perform long extended test to check hard drive health (usually 1hr+)"
    echo -e "\nUsage: $0 <device>"
    echo -e "Example: $0 sdx"
    return 1
  fi
  sudo smartctl -t long /dev/"$1"
}

smartctl-shorttest() {
  if [ $# -lt 1 ]; then
    echo -e "perform short test to check hard drive health (usually 2mins)"
    echo -e "\nUsage: $0 <device>"
    echo -e "Example: $0 sdx"
    return 1
  fi
  sudo smartctl -t short /dev/"$1"
}

smartctl-showprogress() {
  if [ $# -lt 1 ]; then
    echo -e "show the progress of your smartctl self test"
    echo -e "\nUsage: $0 <device>"
    echo -e "Example: $0 sdx"
    return 1
  fi
  sudo watch -n 10 "smartctl -l selftest /dev/$1 ; smartctl -c /dev/$1 | head -11 | tail -3"
}

smartctl-cancletest() {
  if [ $# -lt 1 ]; then
    echo -e "cancle a self test (short, conveyance, extended)"
    echo -e "\nUsage: $0 <device>"
    echo -e "Example: $0 sdx"
    return 1
  fi
  sudo smartctl -X /dev/"$1"
}

smartctl-enablesmart() {
  if [ $# -lt 1 ]; then
    echo -e "enable SMART on your hard drive"
    echo -e "\nUsage: $0 <device>"
    echo -e "Example: $0 sdx"
    return 1
  fi
  sudo smartctl -s on /dev/"$1"
}

smartctl-disablesmart() {
  if [ $# -lt 1 ]; then
    echo -e "disable SMART on your hard drive"
    echo -e "\nUsage: $0 <device>"
    echo -e "Example: $0 sdx"
    return 1
  fi
  sudo smartctl -s off /dev/"$1"
}

smartctl-keepalive() {
  if [ $# -lt 1 ]; then
    echo -e "Keep hard drive from going to sleep by creating a file every 60 seconds."
    echo -e 'Some external hard drive like Seagate will auto sleep on idle, thus we will get a "Aborted by host" in our self-test logs'
    echo -e "references: https://ddumont.wordpress.com/2010/03/15/workaround-for-aborted-smart-test-for-seagate-disk/"
    echo -e "\nUsage: $0 <path>"
    echo -e "Example: $0 ."
    echo -e "         cd /mnt/myseagatehdd && $0 ."
    return 1
  fi
  while true ; do echo "foo" >> test.txt; sleep 60; done
}

smartctl-info() {
  if [ $# -lt 1 ]; then
    echo -e 'Show S.M.A.R.T information of a device'
    echo -e "\nUsage: $0 <device>"
    echo -e "Example: $0 sdx"
    return 1
  fi
  sudo smartctl -a /dev/"$1" | grep -i --color='always' -E 'WARNING|Model Family|Device Model|SMART support is|User Capacity|SMART overall-health self-assessment test result|-fail|Short self-test routine|Extended self-test routine|Conveyance self-test routine|SMART Attributes Data Structure|Power_On_Hours|SMART Self-test log structure|ATA Error Count|FAILING_NOW|$'

  echo -e "${Red}=============References================${Color_Off}"
  echo -e "${Yellow}>>>ATTRIBUTE_NAME meaning: https://en.wikipedia.org/wiki/S.M.A.R.T.#ATA_S.M.A.R.T._attributes ${Color_Off}"
  echo -e "${Blue}>>>aborted by host (HDD sleep on idle): https://ddumont.wordpress.com/2010/03/15/workaround-for-aborted-smart-test-for-seagate-disk/ ${Color_Off}"
  echo -e "${Green}>>>If VALUE <= THRESH then the Attribute is said to have failed, then the "WHEN_FAILED" column will display FAILING_NOW.${Color_Off}"
  echo -e "${Green}>>>If the Attribute is a pre-failure Attribute, then disk failure is imminent. 'Pre-fail' does not mean that your disk is about to fail!${Color_Off}"
  echo -e "${Purple}=============HDD Hours=================${Color_Off}"
  echo "1000  hrs = 41 days"
  echo "8760  hrs = 1 year  (365  days)"
  echo "17520 hrs = 2 years (730  days)"
  echo "26280 hrs = 3 years (1095 days)"
  echo "35040 hrs = 4 years (1460 days)"
  echo "43800 hrs = 5 years (1825 days)"
  echo "52560 hrs = 6 years (2190 days)"
}
# }}}
#-------- F3 - Check Fake Drives {{{
#------------------------------------------------------
# DEMO: https://www.youtube.com/watch?v=jhv-2pNWfr4
# DESC: switch audio stream to different output (HDMI, Headphone, Speakers ...etc)
# REFF: http://askubuntu.com/a/18210
# LINK: http://quvi.sourceforge.net/

f3check() {
  if [ $# -lt 1 ]; then
    echo -e "check if usb flash drive/sd card is fake or real capacity"
    echo -e "\nUsage: $0 <mounted path>"
    echo -e "Example: $0 /run/media/user/FC30-3DA9/"
    return 1
  fi
  echo -e "${Green}>>>Writing .h2w test files to usb drive ${Color_Off}"
    f3write "$1"
  echo -e "${Yellow}>>>Reading .h2w test files from usb drive ${Color_Off}"
    f3read "$1"
  echo -ne "${Red}>>>Cleanup .h2w, do you want to delete these test files? [y/n] ${Color_Off}"
    read REPLY
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
      find "$1"/ -name "*.h2w" -type f -print0 | xargs -0 /bin/rm -vf 
    else
      echo -e "${Yellow}>>>You chose to skip removing test files ${Color_Off}"
    fi
}
# }}}
#-------- WoeUSB - Windows ISO to Live USB Boot  {{{
#------------------------------------------------------
# DEMO: https://www.youtube.com/watch?v=jhv-2pNWfr4
# DESC: switch audio stream to different output (HDMI, Headphone, Speakers ...etc)
# REFF: http://askubuntu.com/a/18210
# LINK: http://quvi.sourceforge.net/

f3check() {
  if [ $# -lt 1 ]; then
    echo -e "check if usb flash drive/sd card is fake or real capacity"
    echo -e "\nUsage: $0 <mounted path>"
    echo -e "Example: $0 /run/media/user/FC30-3DA9/"
    return 1
  fi
  echo -e "${Green}>>>Writing .h2w test files to usb drive ${Color_Off}"
    f3write "$1"
  echo -e "${Yellow}>>>Reading .h2w test files from usb drive ${Color_Off}"
    f3read "$1"
  echo -ne "${Red}>>>Cleanup .h2w, do you want to delete these test files? [y/n] ${Color_Off}"
    read REPLY
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
      find "$1"/ -name "*.h2w" -type f -print0 | xargs -0 /bin/rm -vf 
    else
      echo -e "${Yellow}>>>You chose to skip removing test files ${Color_Off}"
    fi
}
# }}}

### not working exactcopy-audiocd correctly

#-------- Main Program {{{
#------------------------------------------------------
main_list() {

MENU_FORMATDEVICE="
,${Green}m2|m3|m4|mx|mn|mh${Color_Off}, FORMAT MBR:, ext2 <=> ext3 <=> ext4 <=> exfat <=> ntfs <=> hfs+
,${Green}mt|mf|c3|c6${Color_Off}, FORMAT MBR:, fat16 <=> fat32 <=> fat32-32KB <=> fat32-64KB
,${Green}g2|g3|g4|gx|gn${Color_Off}, FORMAT GPT:, ext2 <=> ext3 <=> ext4 <=> exfat <=> ntfs
,${Green}l2|l3|l4${Color_Off}, FORMAT LUKS:, ext2 <=> ext3 <=> ext4
,${Green}cd|rd|cp|rp${Color_Off}, CLONING:, clone drive <=> restore drive <=> clone part <=> restore part
,${Green}di|ai|ci${Color_Off}, EXACT COPY:, dvdmovie <=> audiocd <=> datadisc
,${Green}pd|pa${Color_Off}, PLAYBACK:, dvdmovie <=> audiocd
,${Green}cdw${Color_Off}, BURNING:, cd/dvd/iso burning tool
,${Green}f3|fp${Color_Off}, FAKEUSB:, f3check (write & read) <=> f3probe (wipes all data)
,${Green}si|sc|se|sd${Color_Off}, HDD HEALTH:, info <=> enable smart <=> disable smart
,${Green}s1|s2|s3|sc${Color_Off}, HDD TEST:, short (2min) <=> conveyance (5m) <=> extended (1h) <=> cancle
,${Green}sp|sk${Color_Off}, HDD STATS:, show progress <=> keep alive
,${Green}wu${Color_Off}, USB CREATOR:, woeusb (windows)
,${Green}m|b|u|a${Color_Off}, MOUNTING:, mount <=> mount all <=> unmount <=> unmount all
,${Green}e|t${Color_Off}, EJECTING:, eject <=> toggle tray
,${Green}r|df|h|q${Color_Off}, OTHER:, refresh <=> list all drives <=> help <=> quit
"
HELP="
    ${Green}mountjutsu${Color_Off}: simple menu to mount, unmount, format, eject, restore, clone drives and many other features.

    dependencies: bash sudo grep gawk coreutils udisks2 util-linux
                  gptfdisk dosfstools ntfs-3g hfsprogs exfat-utils e2fsprogs
                  cryptsetup clonezilla partclone partimage vlc cdw f3 smartmontools
                  dvdbackup libdvdread libdvdcss cdrdao cdrtools(or cdrkit)

    FORMAT MBR: format drive ${Red}[util-linux dosfstools exfat-utils e2fsprogs ntfs-3g hfsprogs]${Color_Off}
                - FAT32 32KB Cluster (Wii, Gamecube, 3DS ...etc)
                - HFS+ (Mac OSX non-journal HFS+. Linux can write in HFS+ non-journaling mode only)
    FORMAT GPT: format drive GREATER THAN 2TB ${Red}[gptfdisk exfat-utils e2fsprogs ntfs-3g]${Color_Off}
    FORMAT LUKS: setup encryption and password, formats to different file systems ${Red}[cryptsetup e2fsprogs]${Color_Off}
    CLONING: clone/restore drive or partition image ${Red}[clonezilla partclone partimage ntfs-3g coreutils]${Color_Off}
    EXACT COPY DVDMovie: backup dvdmovie to ISO and bypass disc protection ${Red}[dvdbackup libdvdread libdvdcss]${Color_Off}
    EXACT COPY AudioCD: backup audiocd to BIN/CUE ${Red}[cdrdao]${Color_Off}
    EXACT COPY DATADisc: backup cd/dvd/bluray data disc to ISO (using dd) ${Red}[coreutils]${Color_Off}
    FAKEUSB: check if storage space is legit or fake ${Red}[f3]${Color_Off}
    BURNING: CD/DVD/ISO Ncurses Burning Tool ${Red}[cdw]${Color_Off}
    HDD HEALTH: display info, enable or disable S.M.A.R.T ${Red}[smartmontools]${Color_Off}
    HDD TEST: run a S.M.A.R.T test to check for Hard Drive Failures ${Red}[smartmontools]${Color_Off}
    HDD STATS: show progress of S.M.A.R.T test. keep Hard Drive alive from entering sleep mode${Red}[smartmontools]${Color_Off}
    MOUNTING: mount, unmount devices ${Red}[udisks2]${Color_Off}
    EJECTING: unmount and eject devices, toggle disc tray ${Red}[udisks2 util-linux]${Color_Off}
    PLAYBACK: play dvdmovie or audiocd (using cvlc and nvlc) ${Red}[vlc]${Color_Off}
    OTHER: list all drives (using df and lsblk) ${Red}[coreutils util-linux]${Color_Off}

    AUTHOR: gotbletu (gotbletu@gmail.com)
            https://github.com/gotbletu | https://www.youtube.com/user/gotbletu
    DEMO:   https://www.youtube.com/watch?v=jipILuNW5Ks
"
list-all-drive() {
  lsblk -o "tran,name,hotplug,size,fstype,type,label,mountpoint,uuid,model"
}
list-removable-drive() {
  lsblk -o "hotplug,kname,tran,size,fstype,type,label,mountpoint,uuid,model" | head -n1
  lsblk -o "hotplug,kname,tran,size,fstype,type,label,mountpoint,uuid,model" | awk '$1 == 1 || /rom/ || /usb/ || /crypt/ || /crypto_LUKS/ {print $0}'
}

while true; do
  clear
  pidof tmux >/dev/null && tmux clear-history
  printf '%s\n\n' '======================= LISTING REMOVABLE DEVICES ====================='
  list-removable-drive
  # printf '%s\n\n' '======================= LISTING ALL DEVICES ==========================='
  # list-all-drive
  printf '%s\n'
  printf '%s\n\n' '======================= OPTIONS ==============================='
  printf "$MENU_FORMATDEVICE" | column -t -s,
  printf '%s\n'
  echo -ne "${Green}[Mountjutsu]>>> Please make your choice: ${Color_Off}"
  read INPUT

  case $INPUT in
    wu) # woeusb for windows iso to live usb boot
      read -e -p "Input Your Source Windows Image Path? (e.g /home/user/windows7.iso): " FILEPATH
      echo -n "Your Target USB Device? (e.g sdx): "
      read DEVICE
      sudo woeusb -d "$FILEPATH" /dev/"$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    di)
      read -e -p "Input your save location (e.g /home/user/Videos): " LOCATION
      exactcopy-dvdmovie "$LOCATION"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    ci)
      read -e -p "Input your save location (e.g /home/user/Data): " LOCATION
      exactcopy-datadisc "$LOCATION"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    ai)
      read -e -p "Input your save location (e.g /home/user/Music): " LOCATION
      exactcopy-audiocd "$LOCATION"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    cdw)
      cdw
    ;;
    pd)
      cvlc /dev/cdrom
    ;;
    pa)
      nvlc cdda://
    ;;
    cd)
      echo -n "Which device do you want to clone? (e.g sdx): "
      read DEVICE
      echo -n "Give an output filename: (e.g myusbdrive) "
      read FILENAME
      read -e -p "Input your save location (e.g /home/user): " LOCATION
      clonezilla-disk-cloning "$FILENAME" "$DEVICE" "$LOCATION"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    cp)
      echo -n "Which partition do you want to clone? (e.g sdx1): "
      read DEVICE
      echo -n "Give an output filename: (e.g myusbpartition) "
      read FILENAME
      read -e -p "Input your save location (e.g /home/user): " LOCATION
      clonezilla-partition-cloning "$FILENAME" "$DEVICE" "$LOCATION"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    rd)
      echo -n "Which device do you want to restore? (e.g sdx): "
      read DEVICE
      read -e -p "Image location? (e.g /home/user/my_clonezilla_image): " FILENAME
      DIRNAME="$(dirname $FILENAME)"
      IMAGE_NAME="$(basename $FILENAME)"
      cd "$DIRNAME"
      clonezilla-disk-restore "$IMAGE_NAME" "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    rp)
      echo -n "Which partition do you want to restore? (e.g sdx1): "
      read DEVICE
      read -e -p "Image location? (e.g /home/user/my_clonezilla_image): " FILENAME
      DIRNAME="$(dirname $FILENAME)"
      IMAGE_NAME="$(basename $FILENAME)"
      cd "$DIRNAME"
      clonezilla-partition-restore "$IMAGE_NAME" "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    m2)
      echo -n "Which device do you want to format to EXT2 MBR? (e.g sdx): "
      read DEVICE
      echo -n "What label name do you want to assign to $DEVICE ? "
      read LABELNAME
      format2usb-ext ext2 "$LABELNAME" "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    m3)
      echo -n "Which device do you want to format to EXT3 MBR? (e.g sdx): "
      read DEVICE
      echo -n "What label name do you want to assign to $DEVICE ? "
      read LABELNAME
      format2usb-ext ext3 "$LABELNAME" "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    m4)
      echo -n "Which device do you want to format to EXT4 MBR? (e.g sdx): "
      read DEVICE
      echo -n "What label name do you want to assign to $DEVICE ? "
      read LABELNAME
      format2usb-ext ext4 "$LABELNAME" "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    c6)
      echo -n "Which device do you want to format to FAT32 64KB Cluster MBR? (e.g sdx): "
      read DEVICE
      echo -n "What label name do you want to assign to $DEVICE ? (11 char): "
      read LABELNAME
      format2usb-fat32-64kbcluster "$LABELNAME" "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    c3)
      echo -n "Which device do you want to format to FAT32 32KB Cluster MBR? (e.g sdx): "
      read DEVICE
      echo -n "What label name do you want to assign to $DEVICE ? (11 char): "
      read LABELNAME
      format2usb-fat32-32kbcluster "$LABELNAME" "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    mt)
      echo -n "Which device do you want to format to FAT16 MBR? (e.g sdx): "
      read DEVICE
      echo -n "What label name do you want to assign to $DEVICE ? (11 char): "
      read LABELNAME
      format2usb-fat16 "$LABELNAME" "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    mf)
      echo -n "Which device do you want to format to FAT32 MBR? (e.g sdx): "
      read DEVICE
      echo -n "What label name do you want to assign to $DEVICE ? (11 char): "
      read LABELNAME
      format2usb-fat32 "$LABELNAME" "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    mx)
      echo -n "Which device do you want to format to exFAT MBR? (e.g sdx): "
      read DEVICE
      echo -n "What label name do you want to assign to $DEVICE ? "
      read LABELNAME
      format2usb-exfat "$LABELNAME" "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    mn)
      echo -n "Which device do you want to format to NTFS MBR? (e.g sdx): "
      read DEVICE
      echo -n "What label name do you want to assign to $DEVICE ? "
      read LABELNAME
      format2usb-ntfs "$LABELNAME" "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    mh)
      echo -n "Which device do you want to format to HFS+ non-journal MBR? (e.g sdx): "
      read DEVICE
      echo -n "What label name do you want to assign to $DEVICE ? "
      read LABELNAME
      format2usb-hfsplus-nonjournal "$LABELNAME" "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    l2)
      echo -n "Which device do you want to setup LUKS encryption on and format to EXT2? (e.g sdx): "
      read DEVICE
      luks-setup-ext ext2 "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    l3)
      echo -n "Which device do you want to setup LUKS encryption on and format to EXT3? (e.g sdx): "
      read DEVICE
      luks-setup-ext ext3 "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    l4)
      echo -n "Which device do you want to setup LUKS encryption on and format to EXT4? (e.g sdx): "
      read DEVICE
      luks-setup-ext ext4 "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    g2)
      echo -n "Which device do you want to format to EXT2 GPT? (e.g sdx): "
      read DEVICE
      echo -n "What label name do you want to assign to $DEVICE ? "
      read LABELNAME
      format2gpt-ext ext2 "$LABELNAME" "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    g3)
      echo -n "Which device do you want to format to EXT3 GPT? (e.g sdx): "
      read DEVICE
      echo -n "What label name do you want to assign to $DEVICE ? "
      read LABELNAME
      format2gpt-ext ext3 "$LABELNAME" "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    g4)
      echo -n "Which device do you want to format to EXT4 GPT? (e.g sdx): "
      read DEVICE
      echo -n "What label name do you want to assign to $DEVICE ? "
      read LABELNAME
      format2gpt-ext ext4 "$LABELNAME" "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    gx)
      echo -n "Which device do you want to format to exFAT GPT? (e.g sdx): "
      read DEVICE
      echo -n "What label name do you want to assign to $DEVICE ? "
      read LABELNAME
      format2gpt-exfat "$LABELNAME" "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    gn)
      echo -n "Which device do you want to format to NTFS GPT? (e.g sdx): "
      read DEVICE
      echo -n "What label name do you want to assign to $DEVICE ? "
      read LABELNAME
      format2gpt-ntfs "$LABELNAME" "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    si)
      echo -n "Which storage device do you want information about? (e.g sdx): "
      read DEVICE
      smartctl-info "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    sp)
      echo -n "Which storage device do you want to show the current running health check progress? (e.g sdx): "
      read DEVICE
      smartctl-showprogress "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    se)
      echo -n "Which storage device do you want to enable S.M.A.R.T? (e.g sdx): "
      read DEVICE
      smartctl-enablesmart "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    sd)
      echo -n "Which storage device do you want to disable S.M.A.R.T? (e.g sdx): "
      read DEVICE
      smartctl-disablesmart "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    sk)
      echo -n "Which storage device do you want to keep alive to prevent sleeping during long health test? (e.g sdx): "
      read DEVICE
      smartctl-keepalive "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    sc)
      echo -n "Which storage device do you want to cancle test? (e.g sdx): "
      read DEVICE
      smartctl-cancletest "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    s1)
      echo -n "Which storage device do you to run a short health test on? (e.g sdx): "
      read DEVICE
      smartctl-shorttest "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    s2)
      echo -n "Note: Not All Device Has This Feature] Which storage device do you to run a conveyance health test on? (e.g sdx): "
      read DEVICE
      smartctl-conveyancetest "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    s3)
      echo -n "Which storage device do you to run a extended health test on? (e.g sdx): "
      read DEVICE
      smartctl-extendedtest "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    f3)
      read -e -p "Input your device location you want to test (e.g /run/media/user/5EBD-5C80/): " LOCATION
      f3check "$LOCATION"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    fp)
      echo -e "${Red}WARNING!!! THIS WILL DESTROY ANY PREVIOUSLY STORED DATA ON YOUR DISK ${Color_Off}"
      echo -n "Input the device you want to probe (e.g sdx): "
      read DEVICE
      sudo f3probe --destructive --time-ops /dev/"$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    s3)
      echo -n "Which storage device do you to run a extended health test on? (e.g sdx): "
      read DEVICE
      smartctl-extendedtest "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    s3)
      echo -n "Which storage device do you to run a extended health test on? (e.g sdx): "
      read DEVICE
      smartctl-extendedtest "$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    m)
      echo -n "Which device do you want to mount? (e.g sdx1): "
      read DEVICE
      udisksctl mount --block-device "/dev/$DEVICE"
        if [ $? -ne 0 ]; then
          mount-udisksctl-luks "$DEVICE"
        fi
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    u)
      echo -n "Which device do you want to unmount? (e.g sdx1): "
      read DEVICE
      udisksctl unmount --force --block-device "/dev/$DEVICE"
        if [ $? -ne 0 ]; then
          unmount-udisksctl-luks "$DEVICE"
        fi
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    b)
      echo -n "Which device do you want to mount all partitions? (e.g sdx): "
      read DEVICE

      # unmount all partitions/luks from a given device
      ALLPARTITION=$(lsblk -o "KNAME" | sed '1d' | grep $DEVICE | sed -n '1!G;h;$p')
      mount-udisksctl $ALLPARTITION
      mount-udisksctl-luks $ALLPARTITION
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    a)
      echo -n "Which device do you want to unmount all partitions? (e.g sdx): "
      read DEVICE

      # unmount all partitions/luks from a given device
      ALLPARTITION=$(lsblk -o "KNAME" | sed '1d' | grep $DEVICE | sed -n '1!G;h;$p')
      unmount-udisksctl $ALLPARTITION
      unmount-udisksctl-luks $ALLPARTITION
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    e)
      echo -n "Which device do you want to eject? (e.g sdx): "
      read DEVICE

      # unmount all partitions/luks from a given device
      ALLPARTITION=$(lsblk -o "KNAME" | sed '1d' | grep $DEVICE | sed -n '1!G;h;$p')
      unmount-udisksctl $ALLPARTITION
      unmount-udisksctl-luks $ALLPARTITION

      # eject safely remove tray/drives
      eject "/dev/$DEVICE"
      udisksctl power-off --block-device "/dev/$DEVICE"
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    t)
      echo -ne "Which dvdrom do you want to open/close? (e.g sr0)\n"
      echo -ne "hit Enter to toggle default drive: "
      read DEVICE
      eject -T "/dev/$DEVICE"
      # eject the default dvdrom if other options failed
        if [ $? -ne 0 ]; then
          eject -T
        fi
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    df)
      clear
      pidof tmux >/dev/null && tmux clear-history
      printf '%s\n' '====================== lsblk =========================='
      list-all-drive
      printf '%s\n'
      printf '%s\n' '======================== df ==========================='
      df -hT --total
      printf '%s\n'
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    r|R)
      main_list
    ;;
    q|Q)
      clear
      pidof tmux >/dev/null && tmux clear-history
      exit 0
    ;;
    \?|h|H)
      clear
      pidof tmux >/dev/null && tmux clear-history
      printf '%s\n' '======================== HELP ==========================='
      printf "$HELP"
      printf '%s\n\n'
      read -rsp $'Press any key to return to main menu\n' -n1 key
    ;;
    *) # All other user input results in an usage message
      clear
      pidof tmux >/dev/null && tmux clear-history
      echo -e "Please choose again"
      sleep 2
    ;;
  esac

done

}

# start the program
main_list

# }}}



