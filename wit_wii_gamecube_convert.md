# wit - Convert Wii ISO -> WBFS and Gamecube ISO -> CISO - Linux CLI
convert wii iso to wbfs with auto split at 4GB. convert gamecube iso to ciso (compress iso). Make both of them work inside usbloadergx on a modded wii console. Quick conversion from the commandline.

* tutorial video: [Link](https://www.youtube.com/watch?v=_vcdofAUcPI)
* offical website: [Link](https://wit.wiimm.de/)

### wii requirements
    homebrew channel
    nintendont v4.428 or higher     # this plays gamecube games
    usbloadergx                     # this plays wii games

### linux install requirements
    wit

### configuration
    $EDITOR ~/.zshrc or $EDITOR ~/.bashrc


    #-------- Wit - Nintendo Wii/GameCube Roms Manager {{{
    #------------------------------------------------------
    # DEMO: https://www.youtube.com/watch?v=_vcdofAUcPI
    # DESC: Convert Wii or Gamecube games to compatible formats to work on Softmodded/Modded Nintendo Wii Console
    # REFF: https://gist.github.com/openback/1138763
    #       Wii Backup Fusion GUI https://www.youtube.com/watch?v=8B2JOnFE5kM
    #       https://sourceforge.net/projects/usbloadergx/
    #       https://github.com/FIX94/Nintendont
    #       https://sourceforge.net/projects/wiibafu/
    #       http://wiki.gbatemp.net/wiki/Nintendont_Compatibility_List
    #       https://github.com/FIX94/Nintendont
    #       Format FAT32 32KB cluster https://gist.github.com/joshenders/4376942
    # LINK: http://wit.wiimm.de/
    
    convert-to-game-nintendont() {
      if [ $# -lt 1 ]; then
        echo -e "convert gamecube iso games to ciso (compress iso, ignore usused blocks)."
        echo -e "works with nintendont v4.428+ and usbloadergx on a modded wii console."
        echo -e "Note: after conversion the ciso will be renamed to iso to make it work under usbloadergx"
        echo -e "\nUsage: $0 <filename>"
        echo -e "\nExample:\n$0 Melee.iso"
        echo -e "$0 Melee.iso DoubleDash.iso WindWaker.iso"
        echo -e "$0 *.iso"
        echo -e "\nNintendont uses these paths:"
        echo -e "USB:/games/"
        echo -e "USB:/games/Name of game [GameID]/game.iso"
        echo -e "USB:/games/Legend of Zelda the Wind Waker (USA) [GZLP01]/game.iso"
        echo -e "\nMultiple Gamecube Disc Example:"
        echo -e "USB:/games/Resident Evil 4 (USA) [G4BE08]/game.iso"
        echo -e "USB:/games/Resident Evil 4 (USA) [G4BE08]/disc2.iso"
        return 1
      fi
      myArray=( "$@" )
      for arg in "${myArray[@]}"; do
        FILENAME="${arg%.*}"
        REGION=$(wit lll -H "$arg" | awk '{print $4}')
        GAMEID=$(wit lll -H "$arg" | awk '{print $1}')
        TITLE=$(wit lll -H "$arg" | awk '{ print substr($0, index($0,$5)) }' | awk '{$1=$1};1' )
        DIR_FILENAME="$FILENAME [$GAMEID]"
        DIR_TITLENAME="$TITLE ($REGION) [$GAMEID]"
    
        ## no conversion; only generate folder base on title inside the rom, move iso to folder
        # mkdir -pv "$DIR_TITLENAME"
        # mv -v "$arg" "$DIR_TITLENAME"/game.iso
    
        ## no conversion; only generate folder base on filename, move iso to folder
        # mkdir -pv "$DIR_FILENAME"
        # mv -v "$arg" "$DIR_FILENAME"/game.iso
    
        ## convert to ciso; generate folder base on title inside the rom; move ciso to folder
        ## rename ciso to iso ; this will make it compatible with both nintendont and usbloadergx
        # mkdir -pv "$DIR_TITLENAME"
        # wit copy --ciso "$arg" "$DIR_TITLENAME"/game.iso
    
        ## convert to ciso; generate folder base on filename; move ciso to folder
        ## rename ciso to iso ; this will make it compatible with both nintendont and usbloadergx
        mkdir -pv "$DIR_FILENAME"
        wit copy --ciso "$arg" "$DIR_FILENAME"/game.iso
      done
    }
    
    convert-to-game-usbloadergx() {
      if [ $# -lt 1 ]; then
        echo -e "convert wii iso games to wbfs that will works with usbloadergx on a modded wii console"
        echo -e "\nUsage: $0 <filename>"
        echo -e "\nExample:\n$0 WiiSports.iso"
        echo -e "$0 MarioKart.iso Zelda.iso DonkeyKong.iso"
        echo -e "$0 *.iso"
        echo -e "\nUSBLoaderGX uses these paths:"
        echo -e "USB:/wbfs/"
        echo -e "USB:/wbfs/Name of game [GameID]/GameID.wbfs"
        echo -e "USB:/wbfs/Donkey Kong Country Returns (USA) [SF8E01]/SF8E01.wbfs"
        echo -e "\nSplit Wii Game Example:"
        echo -e "USB:/wbfs/Super Smash Bros Brawl (NTSC) [RSBE01]/RSBE01.wbf1"
        echo -e "USB:/wbfs/Super Smash Bros Brawl (NTSC) [RSBE01]/RSBE01.wbf2"
        echo -e "USB:/wbfs/Super Smash Bros Brawl (NTSC) [RSBE01]/RSBE01.wbf3"
        echo -e "USB:/wbfs/Super Smash Bros Brawl (NTSC) [RSBE01]/RSBE01.wbfs"
        return 1
      fi
      myArray=( "$@" )
      for arg in "${myArray[@]}"; do
        FILENAME="${arg%.*}"
        REGION=$(wit lll -H "$arg" | awk '{print $4}')
        GAMEID=$(wit lll -H "$arg" | awk '{print $1}')
        TITLE=$(wit lll -H "$arg" | awk '{ print substr($0, index($0,$5)) }' | awk '{$1=$1};1' )
        DIR_FILENAME="$FILENAME [$GAMEID]"
        DIR_TITLENAME="$TITLE ($REGION) [$GAMEID]"
    
        ## create proper folder structure base on title inside the rom, scrub image & convert to wbfs, auto split at 4GB a piece
        # mkdir -pv "$DIR_TITLENAME"
        # wit copy --wbfs --split "$arg" "$DIR_TITLENAME"/"$GAMEID.wbfs"
    
        ## create proper folder structure base on filename, scrub image & convert to wbfs, auto split at 4GB a piece
        mkdir -pv "$DIR_FILENAME"
        wit copy --wbfs --split "$arg" "$DIR_FILENAME"/"$GAMEID.wbfs"
      done
    }
    # }}}


### references
- https://www.youtube.com/watch?v=_vcdofAUcPI
- Wii Backup Fusion GUI https://www.youtube.com/watch?v=8B2JOnFE5kM

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


