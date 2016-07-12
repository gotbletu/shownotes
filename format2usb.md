# Format2USB - Quick Way to Format USB/HDD/SDCards via Commandline
A couple of functions i created to format my drives. It will delete existing partitions and create just a single partitions that fills the whole drive, then formats it to whatever filesystem you choose. 

I could of used just mkfs to format but from my experience linux likes to have at least one partition so that is why we used fdisk to create a partition before we format with mkfs.

* tutorial video: [Link](https://www.youtube.com/watch?v=ypKjq5KIxSk)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

### install requirements
    mkfs fdisk

### configuration
add to ~/.bashrc or ~/.zshrc
    
    #-------- Color Code {{{
    #------------------------------------------------------
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
    #-------- Format USB Stick/HDD/SDCards {{{
    #------------------------------------------------------
    # Format USB Stick/Hard Drive
    # It will create a single partition that fills the whole drive space
    
    format2usb-fat32() {
      if [ $# -lt 2 ]; then
        echo -e "format and create a partition that fills up the whole device"
        echo -e "\nUsage: $0 <label> <device>"
        echo -e "Example: $0 MY_USB sdx"
        return 1
      fi
    
      # check if the device is mounted
      mount_status=$(mount | grep /dev/"$2" | wc -l)
      if [ "$mount_status" -ne 0 ]
      then
        lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$2"
        echo -e "${Red}/dev/$2 is mounted. You have to unmount /dev/$2 ${Color_Off}"
        return 1
      fi
    
      # show the device info that is going to be formatted
      sudo fdisk -l /dev/"$2"
    
      # warning message countdown
      echo -e "${Red}WARNING YOU ARE ABOUT TO FORMAT A DRIVE! ${Color_Off}"
      echo -e "${Red}You Have 15sec to hit CTRL+C To Cancle ${Color_Off}"
      for i in {15..1..1};do echo -n "$i." && sleep 1; done
    
      # delete existing partition then create new linux partition
      echo -e "d\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\no\nn\np\n1\n\n\nt\nb\nw" | sudo fdisk /dev/"$2"
    
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
    
      # fat32 likes the labels to be in uppercase
      label_name=$(echo "$1" | tr '[:lower:]' '[:upper:]')
    
      # format device
      sudo mkfs.fat -F 32 -n "$label_name" -I /dev/"$2"1
    }
    
    format2usb-ntfs() {
      if [ $# -lt 2 ]; then
        echo -e "format and create a partition that fills up the whole device"
        echo -e "\nUsage: $0 <label> <device>"
        echo -e "Example: $0 MY_USB sdx"
        return 1
      fi
    
      # check if the device is mounted
      mount_status=$(mount | grep /dev/"$2" | wc -l)
      if [ "$mount_status" -ne 0 ]
      then
        lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$2"
        echo -e "${Red}/dev/$2 is mounted. You have to unmount /dev/$2 ${Color_Off}"
        return 1
      fi
    
      # show the device info that is going to be formatted
      sudo fdisk -l /dev/"$2"
    
      # warning message countdown
      echo -e "${Red}WARNING YOU ARE ABOUT TO FORMAT A DRIVE! ${Color_Off}"
      echo -e "${Red}You Have 15sec to hit CTRL+C To Cancle ${Color_Off}"
      for i in {15..1..1};do echo -n "$i." && sleep 1; done
    
      # delete existing partition then create new linux partition
      echo -e "d\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\no\nn\np\n1\n\n\nt\n7\nw" | sudo fdisk /dev/"$2"
    
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
    
      # format device
      sudo mkfs.ntfs -f -L "$1" /dev/"$2"1
    }
    
    format2usb-ext2() {
      if [ $# -lt 2 ]; then
        echo -e "format and create a partition that fills up the whole device"
        echo -e "\nUsage: $0 <label> <device>"
        echo -e "Example: $0 MY_USB sdx"
        return 1
      fi
    
      # check if the device is mounted
      mount_status=$(mount | grep /dev/"$2" | wc -l)
      if [ "$mount_status" -ne 0 ]
      then
        lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$2"
        echo -e "${Red}/dev/$2 is mounted. You have to unmount /dev/$2 ${Color_Off}"
        return 1
      fi
    
      # show the device info that is going to be formatted
      sudo fdisk -l /dev/"$2"
    
      # warning message countdown
      echo -e "${Red}WARNING YOU ARE ABOUT TO FORMAT A DRIVE! ${Color_Off}"
      echo -e "${Red}You Have 15sec to hit CTRL+C To Cancle ${Color_Off}"
      for i in {15..1..1};do echo -n "$i." && sleep 1; done
    
      # delete existing partition then create new linux partition
      echo -e "d\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\no\nn\np\n1\n\n\nw" | sudo fdisk /dev/"$2"
    
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
    
      # format device
      echo -e "y\n" | sudo mkfs.ext2 -L "$1" /dev/"$2"1
    
      # set read/write permission
      mkdir -p /tmp/testmount
      sudo mount /dev/"$2"1 /tmp/testmount
      sudo chmod 777 /tmp/testmount
      sudo umount /tmp/testmount
      rmdir /tmp/testmount
    }
    
    format2usb-ext3() {
      if [ $# -lt 2 ]; then
        echo -e "format and create a partition that fills up the whole device"
        echo -e "\nUsage: $0 <label> <device>"
        echo -e "Example: $0 MY_USB sdx"
        return 1
      fi
    
      # check if the device is mounted
      mount_status=$(mount | grep /dev/"$2" | wc -l)
      if [ "$mount_status" -ne 0 ]
      then
        lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$2"
        echo -e "${Red}/dev/$2 is mounted. You have to unmount /dev/$2 ${Color_Off}"
        return 1
      fi
    
      # show the device info that is going to be formatted
      sudo fdisk -l /dev/"$2"
    
      # warning message countdown
      echo -e "${Red}WARNING YOU ARE ABOUT TO FORMAT A DRIVE! ${Color_Off}"
      echo -e "${Red}You Have 15sec to hit CTRL+C To Cancle ${Color_Off}"
      for i in {15..1..1};do echo -n "$i." && sleep 1; done
    
      # delete existing partition then create new linux partition
      echo -e "d\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\no\nn\np\n1\n\n\nw" | sudo fdisk /dev/"$2"
    
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
    
      # format device
      echo -e "y\n" | sudo mkfs.ext3 -L "$1" /dev/"$2"1
    
      # set read/write permission
      mkdir -p /tmp/testmount
      sudo mount /dev/"$2"1 /tmp/testmount
      sudo chmod 777 /tmp/testmount
      sudo umount /tmp/testmount
      rmdir /tmp/testmount
    }
    
    format2usb-ext4() {
      if [ $# -lt 2 ]; then
        echo -e "format and create a partition that fills up the whole device"
        echo -e "\nUsage: $0 <label> <device>"
        echo -e "Example: $0 MY_USB sdx"
        return 1
      fi
    
      # check if the device is mounted
      mount_status=$(mount | grep /dev/"$2" | wc -l)
      if [ "$mount_status" -ne 0 ]
      then
        lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$2"
        echo -e "${Red}/dev/$2 is mounted. You have to unmount /dev/$2 ${Color_Off}"
        return 1
      fi
    
      # show the device info that is going to be formatted
      sudo fdisk -l /dev/"$2"
    
      # warning message countdown
      echo -e "${Red}WARNING YOU ARE ABOUT TO FORMAT A DRIVE! ${Color_Off}"
      echo -e "${Red}You Have 15sec to hit CTRL+C To Cancle ${Color_Off}"
      for i in {15..1..1};do echo -n "$i." && sleep 1; done
    
      # delete existing partition then create new linux partition
      echo -e "d\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\nd\n\no\nn\np\n1\n\n\nw" | sudo fdisk /dev/"$2"
    
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
    
      # format device
      echo -e "y\n" | sudo mkfs.ext4 -L "$1" /dev/"$2"1
    
      # set read/write permission
      mkdir -p /tmp/testmount
      sudo mount /dev/"$2"1 /tmp/testmount
      sudo chmod 777 /tmp/testmount
      sudo umount /tmp/testmount
      rmdir /tmp/testmount
    }
    
    # }}}



### contact

                 _   _     _      _         
      __ _  ___ | |_| |__ | | ___| |_ _   _ 
     / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
    | (_| | (_) | |_| |_) | |  __/ |_| |_| |
     \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
     |___/                                  

- http://www.youtube.com/user/gotbletu
- https://twitter.com/gotbletu
- https://plus.google.com/+gotbletu
- https://github.com/gotbletu
- gotbletu@gmail.com


