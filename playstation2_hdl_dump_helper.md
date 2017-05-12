# Transfer Games to Playstation 2 Hard Drive on Linux
Add and delete games from our FAT PS2 IDE Hard Drive using HDL Dump Helper GUI

* tutorial video: [Link](https://www.youtube.com/watch?v=LpBYuCI0d8E)

### Hardware Requirements
- Modded/Softmodded PS2 (Modchip, FreeMcboot or FreeHDBoot)
- PS2 Network Adapter
- IDE to USB Adapter
- IDE Hard Drive already formatted to the PS2

### Software Requirements:
- java (search in the package manager for **jre** and install one of those e.g: **jre8-openjdk**)
- hdl_dump_helper
  - http://www.ps2-home.com/forum/viewtopic.php?t=2738)
  - http://www.theisozone.com/downloads/playstation/ps2-homebrew/hdl-dump-helper-gui-for-linux-windows/)

### HDL Dump Helper
    Extract hdl_dump_helper_gui_v2.3.rar
    
    # change permissions so it can run
    chmod +x launcher-linux.sh
    chmod +x hdl_dump_086
    chmod +x hdl_dump_090
    
    # start the program
    ./launcher-linux.sh

### Find Which is Your PS2 HDD

    # shows a list of storage device
    lsblk -o "KNAME,HOTPLUG,SIZE,FSTYPE,TYPE,LABEL,MOUNTPOINT,UUID,MODEL,SERIAL"

### Common Issue
    # Sometime it will fail to transfer because you have the same game name or similar e.g:
    WWE SMACKDOWN VS RAW 2007
    WWE SMACKDOWN VS RAW 2011
    
    # The Fix is to just rename it a little bit like add or removing one letter e.g:
    WWE SMACKDOWN VS RAW 2007
    WWE SMACKDOWN V RAW 2011
    
### references
- https://www.youtube.com/watch?v=LpBYuCI0d8E

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


