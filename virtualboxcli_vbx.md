# Virtualbox CLI Functions
couple of functions i created to spin up and shutdown virtualbox virtual machines (vm) because is faster for me
* tutorial video: [Link](https://www.youtube.com/watch?v=4pguqqygAd0)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

### install requirements
    virtualbox
    rdesktop

### vm requirements: enable remote desktop on each vm
- [How to rdesktop into linux machine via xrdp](https://www.youtube.com/watch?v=WMSU66zAb3k)
- [How to rdesktop into windows machine](https://www.youtube.com/watch?v=460l2ZN_WQY)


### configuration
    vim ~/.zshrc or vim ~/.bashrc
    
    
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
    
    vbx-list() {
      echo "===Available VM==="
      vboxmanage list vms
      echo "\n===Running VM====="
      vboxmanage list runningvms
    }
    
    vbx-start() {
      # Set to endless loop
      while true
      do
        # Set the prompt for the select command
        PS3="Type a number to select or 'Ctrl+C' to quit: "
    
        # Create a list to display on menu
        IFS=$'\n'
        fileList=($(vboxmanage list vms | cut -d '{' -f1 | sed 's/ *$//'))
        unset IFS
    
        # Show a menu and ask for input. If the user entered a valid choice then execute command
        select fileName in $fileList; do
          if [ -n "$fileName" ]; then
            # remove quotes from filename
            vm_name=($(echo "${fileName}" | sed 's:\"::g' ))
            vboxmanage startvm "$vm_name" --type headless
            echo -e "${Green} $vm_name Has Been Started ${Color_Off}"
          fi
          break
        done
      done
    }
    
    vbx-quit() {
      # Set to endless loop
      while true
      do
        # Set the prompt for the select command
        PS3="Type a number to select or 'Ctrl+C' to quit: "
    
        # Create a list to display on menu
        IFS=$'\n'
        fileList=($(vboxmanage list runningvms | cut -d '{' -f1 | sed 's/ *$//'))
        unset IFS
    
        # Show a menu and ask for input. If the user entered a valid choice then execute command
        select fileName in $fileList; do
          if [ -n "$fileName" ]; then
            # remove quotes from filename
            vm_name=($(echo "${fileName}" | sed 's:\"::g' ))
            vboxmanage controlvm "$vm_name" acpipowerbutton
            echo -e "${Yellow} $vm_name Is Shutting Down ${Color_Off}"
          fi
          break
        done
      done
    }
    
    vbx-forcequit() {
      # Set to endless loop
      while true
      do
        # Set the prompt for the select command
        PS3="Type a number to select or 'Ctrl+C' to quit: "
    
        # Create a list to display on menu
        IFS=$'\n'
        fileList=($(vboxmanage list runningvms | cut -d '{' -f1 | sed 's/ *$//'))
        unset IFS
    
        # Show a menu and ask for input. If the user entered a valid choice then execute command
        select fileName in $fileList; do
          if [ -n "$fileName" ]; then
            # remove quotes from filename
            vm_name=($(echo "${fileName}" | sed 's:\"::g' ))
            vboxmanage controlvm "$vm_name" poweroff
            echo -e "${Red} $vm_name Power Cable Has Been Pulled ${Color_Off}"
          fi
          break
        done
      done
    }

    rdesktop-winxp() {
      ipaddr=192.168.1.150
      port=3389
      username=gotbletu
      resolution=1920x1020
      echo "${Yellow}>>>Check if remote computer is alive at $ipaddr:$port ${Color_Off}"
        until nc -vzw 2 "$ipaddr" "$port"; do sleep 2; done
      echo "${Green}>>>Connecting to remote computer${Color_Off}"
        rdesktop -u "$username" -g "$resolution" "$ipaddr":"$port" -r sound:local
    }
    
    rdesktop-fedoramate64() {
      ipaddr=192.168.1.52
      port=3389
      username=gotbletu
      resolution=1920x1020
      echo "${Yellow}>>>Check if remote computer is alive at $ipaddr:$port ${Color_Off}"
        until nc -vzw 2 "$ipaddr" "$port"; do sleep 2; done
      echo "${Green}>>>Connecting to remote computer${Color_Off}"
        rdesktop -u "$username" -g "$resolution" "$ipaddr":"$port" -r sound:local
    }


### references
- https://www.howtoforge.com/tutorial/running-virtual-machines-with-virtualbox-5.1-on-a-headless-ubuntu-16.04-lts-server/
- http://serverfault.com/a/545408
- https://wiki.archlinux.org/index.php?title=Bash/Prompt_customization&oldid=419076#List_of_colors_for_prompt_and_Bash

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


