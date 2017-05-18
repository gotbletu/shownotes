# Clonezilla CLI to Clone and Restore
A few commandline functions to do clonezilla cloning or restoring on linux.
Works with single partitions or full disk. Supports EXT, FAT, NTFS ...etc.
Check the clonezilla site for other supported filesystems else it will use the dd command.

* tutorial video: [Link](https://www.youtube.com/watch?v=z0WBIOtj5Fo)
* offical website: [Link](http://clonezilla.org/)

### install requirements
    clonezilla

### configuration
    vim ~/.zshrc or vim ~/.bashrc
    
    
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
    
    # Bold
    BBlack='\e[1;30m'       # Black
    BRed='\e[1;31m'         # Red
    BGreen='\e[1;32m'       # Green
    BYellow='\e[1;33m'      # Yellow
    BBlue='\e[1;34m'        # Blue
    BPurple='\e[1;35m'      # Purple
    BCyan='\e[1;36m'        # Cyan
    BWhite='\e[1;37m'       # White
    
    # Underline
    UBlack='\e[4;30m'       # Black
    URed='\e[4;31m'         # Red
    UGreen='\e[4;32m'       # Green
    UYellow='\e[4;33m'      # Yellow
    UBlue='\e[4;34m'        # Blue
    UPurple='\e[4;35m'      # Purple
    UCyan='\e[4;36m'        # Cyan
    UWhite='\e[4;37m'       # White
    
    # Background
    On_Black='\e[40m'       # Black
    On_Red='\e[41m'         # Red
    On_Green='\e[42m'       # Green
    On_Yellow='\e[43m'      # Yellow
    On_Blue='\e[44m'        # Blue
    On_Purple='\e[45m'      # Purple
    On_Cyan='\e[46m'        # Cyan
    On_White='\e[47m'       # White
    
    # High Intensity
    IBlack='\e[0;90m'       # Black
    IRed='\e[0;91m'         # Red
    IGreen='\e[0;92m'       # Green
    IYellow='\e[0;93m'      # Yellow
    IBlue='\e[0;94m'        # Blue
    IPurple='\e[0;95m'      # Purple
    ICyan='\e[0;96m'        # Cyan
    IWhite='\e[0;97m'       # White
    
    # Bold High Intensity
    BIBlack='\e[1;90m'      # Black
    BIRed='\e[1;91m'        # Red
    BIGreen='\e[1;92m'      # Green
    BIYellow='\e[1;93m'     # Yellow
    BIBlue='\e[1;94m'       # Blue
    BIPurple='\e[1;95m'     # Purple
    BICyan='\e[1;96m'       # Cyan
    BIWhite='\e[1;97m'      # White
    
    # High Intensity backgrounds
    On_IBlack='\e[0;100m'   # Black
    On_IRed='\e[0;101m'     # Red
    On_IGreen='\e[0;102m'   # Green
    On_IYellow='\e[0;103m'  # Yellow
    On_IBlue='\e[0;104m'    # Blue
    On_IPurple='\e[10;95m'  # Purple
    On_ICyan='\e[0;106m'    # Cyan
    On_IWhite='\e[0;107m'   # White
    
    # }}}

    #-------- Clonezilla CLI (Clone and Restore Image) {{{
    #------------------------------------------------------
    ### Full Disk Clone and Restore
    clonezilla-disk-cloning() {
      if [ $# -lt 2 ]; then
        echo -e "clone full disk to image"
        echo -e "\nUsage: $0 <output_file> <device>"
        echo -e "\nExample: $0 mydesktop sdx"
        echo -e "\nNote: <output_file> will be saved to your current path"
        return 1
      fi
      OUTPUT_FILE="$1_clonezilla_disk_`date +'%Y_%m_%d'`"
      DEVICE_NAME="$2"
      echo "${Yellow}>>>Checking if device is mounted ${Color_Off}"
        MOUNT_STATUS=$(mount | grep /dev/"$DEVICE_NAME" | wc -l)
        if [ "$MOUNT_STATUS" -ne 0 ]
        then
          lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$DEVICE_NAME"
          echo "${Red}>>>/dev/$DEVICE_NAME is mounted. You have to unmount the device and all of its partitions then try again ${Color_Off}"
          return 1
        fi
      echo "${Blue}>>>Set current output path to $PWD ${Color_Off}"
        sudo sed -i 's:ocsroot=.*:ocsroot='\""$PWD"\"':g' /etc/drbl/drbl.conf
      echo "${Green}>>>Start full disk cloning process ${Color_Off}"
      echo "${Green}>>>$OUTPUT_FILE image will be saved to $PWD ${Color_Off}"
        sudo ocs-sr -q2 -c -j2 -z1p -i 5000000 -sc -p true savedisk "$OUTPUT_FILE" "$DEVICE_NAME"
      echo "${Red}>>>Changing permission of $OUTPUT_FILE image ${Color_Off}"
        sudo chmod -R 777 "$OUTPUT_FILE"
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
      echo "${Yellow}>>>Checking if device is mounted ${Color_Off}"
        MOUNT_STATUS=$(mount | grep /dev/"$DEVICE_NAME" | wc -l)
        if [ "$MOUNT_STATUS" -ne 0 ]
        then
          lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$DEVICE_NAME"
          echo "${Red}>>>/dev/$DEVICE_NAME is mounted. You have to unmount the device and all of its partitions then try again ${Color_Off}"
          return 1
        fi
      echo "${Green}>>>Start full disk restore process ${Color_Off}"
        sudo /usr/sbin/ocs-sr -g auto -e1 auto -e2 -c -r -j2 -p true restoredisk "$INPUT_FILE" "$DEVICE_NAME"
    }
    
    ### Partition Clone and Restore
    clonezilla-partition-cloning() {
      if [ $# -lt 2 ]; then
        echo -e "clone device partition to image"
        echo -e "\nUsage: $0 <output_file> <device>"
        echo -e "\nExample: $0 mylaptop sdx2"
        echo -e "\nNote: <output_file> will be saved to your current path"
        return 1
      fi
      OUTPUT_FILE="$1_clonezilla_part${PART_NUM}_`date +'%Y_%m_%d'`"
      DEVICE_NAME="$2"
      PART_NUM=$(echo "$2" | sed 's/[^0-9]*//g')
      echo "${Yellow}>>>Checking if device is mounted ${Color_Off}"
        MOUNT_STATUS=$(mount | grep /dev/"$DEVICE_NAME" | wc -l)
        if [ "$MOUNT_STATUS" -ne 0 ]
        then
          lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$DEVICE_NAME"
          echo "${Red}>>>/dev/$DEVICE_NAME is mounted. You have to unmount then try again ${Color_Off}"
          return 1
        fi
      echo "${Blue}>>>Set current output path to $PWD ${Color_Off}"
        sudo sed -i 's:ocsroot=.*:ocsroot='\""$PWD"\"':g' /etc/drbl/drbl.conf
      echo "${Green}>>>Start partition cloning process ${Color_Off}"
      echo "${Green}>>>$OUTPUT_FILE image will be saved to $PWD ${Color_Off}"
        sudo /usr/sbin/ocs-sr -q2 -c -j2 -z1p -i 5000000 -sc -p true saveparts "$OUTPUT_FILE" "$DEVICE_NAME"
      echo "${Red}>>>Changing permission of $OUTPUT_FILE image ${Color_Off}"
        sudo chmod -R 777 "$OUTPUT_FILE"
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
      echo "${Yellow}>>>Checking if device is mounted ${Color_Off}"
        MOUNT_STATUS=$(mount | grep /dev/"$DEVICE_NAME" | wc -l)
        if [ "$MOUNT_STATUS" -ne 0 ]
        then
          lsblk -o "NAME,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID" | grep "$DEVICE_NAME"
          echo "${Red}>>>/dev/$DEVICE_NAME is mounted. You have to unmount then try again ${Color_Off}"
          return 1
        fi
      echo "${Green}>>>Start partition restore process ${Color_Off}"
        sudo /usr/sbin/ocs-sr -g auto -e1 auto -e2 -c -r -j2 -k -p true restoreparts "$INPUT_FILE" "$DEVICE_NAME"
    }
    
    # }}}

### other commands

    alias df='df -hT --total'       # human readable, print filetype, and total
    alias lsblk='lsblk -o "KNAME,HOTPLUG,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID,MODEL,SERIAL"'

### usage

    ## Make sure you have enough space to save the image
    ## Image will be saved to the current shell path
    
    # backup
    df
    mkdir mysaveddata
    cd mysaveddata
    lsblk
    clonezilla-disk-cloning myusbdrive sdd
    

    ## The device/partition has to be equal or greater in order for you to restore to it

    # restore
    cd mysaveddata
    lsblk
    clonezilla-disk-restore myusbdrive_clonezilla_disk_2017_05_18 sdd



### common error
- Use **fsck** command to check and repair if you get this type of error
----


    # Partclone fail, please check /var/log/partclone.log
    # Failed to use partclone program to save or restore an image!
    cat /var/log/partclone.log
    
    Partclone v0.2.89 http://partclone.org
    Starting to clone device (/dev/sdd1) to image (-)
    Reading Super Block
    extfsclone.c: FS has been mounted 20 times without being checked
    
    # Force check
    lsblk
    sudo fsck.ext3 /dev/sdd1


### references
- https://www.youtube.com/watch?v=z0WBIOtj5Fo
- **format2usb** tutorial https://www.youtube.com/watch?v=7txO1cdNJsQ
- http://clonezilla.org/

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


