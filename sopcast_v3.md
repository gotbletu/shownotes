# Sopcast - Free P2P Internet TV - Linux CLI ( v3 minor code update)
SopCast is a simple, free way to broadcast video and audio or watch the video and listen to radio on the Internet. Adopting P2P(Peer-to-Peer) technology, It is very efficient and easy to use. Let anyone become a broadcaster without the costs of a powerful server and vast bandwidth.

SoP is the abbreviation for Streaming over P2P. Sopcast is a Streaming Direct Broadcasting System based on P2P. The core is the communication protocol produced by Sopcast Team, which is named sop://, or SoP technology.

* tutorial video: [Link](https://www.youtube.com/watch?v=Khvo4ge1PLQ)
* offical website: [Link](http://www.sopcast.com/)

### install requirements
    sopcast gnu-netcat

### configuration
    vim ~/.bashrc or ~/.zshrc



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

    #-------- Sopcast CLI v3 (Streaming P2P Videos) [last updated April 27, 2018] {{{
    #------------------------------------------------------
    # DEMOv2: http://www.youtube.com/watch?v=Dm7cFjhzgHo
    # DEMOv3: https://www.youtube.com/watch?v=Khvo4ge1PLQ
    # DESC: watch streaming movies/tv shows over p2p
    # FEED: http://www.sopcast.com/chlist.xml
    #       http://sopcast.ucoz.com
    #       http://streams.magazinmixt.ro
    #       google keyword: sop://broker.sopcast
    #       https://www.google.com/#tbs=qdr:w&q=sop:%2F%2Fbroker.sopcast
    
    # package:
    # Archlinux: sopcast ( x64 https://www.archlinux.org/packages/multilib/x86_64/sopcast/)
    # Ubuntu/Debian: sp-auth (https://launchpad.net/~jason-scheunemann/+archive/ppa)
    
    sppc() {
      # choose a player (cvlc is default)
      # SP_VIDPLAYER=cvlc
      # SP_VIDPLAYER=(cvlc --file-caching=10000)
      # SP_VIDPLAYER=(cvlc --video-on-top --width=500 --height=280 --video-x=-15 --video-y=-50)
      # SP_VIDPLAYER=vlc
      # SP_VIDPLAYER=(vlc --control=lirc)
      # SP_VIDPLAYER=mplayer
      # SP_VIDPLAYER=(mplayer -cache 1000)
      # SP_VIDPLAYER=mpv
      # SP_VIDPLAYER=(mpv --cache=1000)
      # SP_VIDPLAYER=(mpv --ontop --no-border --force-window --autofit=500x280 --geometry=-15-50)
      SP_VIDPLAYER=(mpv --cache=2048 --ontop --no-border --force-window --autofit=500x280 --geometry=-15-50)
    
      # sopcast port
      SP_LOCAL_PORT=55050
    
      # ip address and port for video player to connect to
      SP_PLAYER_IPADDR=localhost
      SP_PLAYER_PORT=55051
    
      echo -e "${Red}>>>Kill any exiting sopcast connection ${Color_Off}"
        killall sp-sc &>/dev/null
      echo -e "${Yellow}>>>Loading sopcast connection ${Color_Off}"
        (sp-sc "$1" "$SP_LOCAL_PORT" "$SP_PLAYER_PORT" &>/dev/null &)
      echo -e "${Yellow}>>>Check if sopcast stream is alive at $SP_PLAYER_IPADDR:$SP_PLAYER_PORT [hit Ctrl+C on this screen to exit properly] ${Color_Off}"
        until nc -vzw 2 "$SP_PLAYER_IPADDR" "$SP_PLAYER_PORT"; do sleep 2; done
      echo -e "${Green}>>>Connecting to sopcast stream ${Color_Off}"
        ($SP_VIDPLAYER http://"$SP_PLAYER_IPADDR":"$SP_PLAYER_PORT")
      echo "${On_IRed}>>>Video Player has exited properly. Killing sopcast stream now ${Color_Off}"
        wait
        killall sp-sc
    }
    
    # manually kill sopcast (sometimes it doesnt exit properly and still uses bandwidth in the background)
    sppc-kill() { killall sp-sc ;}
    
    # channel list
    spp-acasa() { sppc "sop://broker.sopcast.com:3912/149256" ;}
    spp-acasagolda() { sppc "sop://broker.sopcast.com:3912/253471" ;}
    spp-acasatv() { sppc "sop://broker.sopcast.com:3912/149256" ;}
    spp-antena1a() { sppc "sop://broker.sopcast.com:3912/149257" ;}
    spp-antena1b() { sppc "sop://broker.sopcast.com:3912/151301" ;}
    spp-antena1c() { sppc "sop://broker.sopcast.com:3912/148083" ;}
    spp-antenastars() { sppc "sop://broker.sopcast.com:3912/148255" ;}
    spp-antena3() { sppc "sop://broker.sopcast.com:3912/148084" ;}
    spp-axn() { sppc "sop://broker.sopcast.com:3912/253035" ;}
    spp-axnblack() { sppc "sop://broker.sopcast.com:3912/149261" ;}
    spp-axnwhite() { sppc "sop://broker.sopcast.com:3912/149262" ;}
    spp-b1() { sppc "sop://broker.sopcast.com:3912/148087" ;}
    spp-boomerang() { sppc "sop://broker.sopcast.com:3912/149264" ;}
    spp-cartoonnetwork() { sppc "sop://broker.sopcast.com:3912/148254" ;}
    spp-digiworld() { sppc "sop://broker.sopcast.com:3912/148260" ;}
    spp-digisport1a() { sppc "sop://broker.sopcast.com:3912/148886" ;}
    spp-digisport1b() { sppc "sop://broker.sopcast.com:3912/173020" ;}
    spp-digisport2c() { sppc "sop://broker.sopcast.com:3912/263242" ;}
    spp-discoverychannel() { sppc "sop://broker.sopcast.com:3912/256241" ;}
    spp-discoveryscience() { sppc "sop://broker.sopcast.com:3912/256243" ;}
    spp-disneychannel() { sppc "sop://broker.sopcast.com:3912/253031" ;}
    spp-disneyjunior() { sppc "sop://broker.sopcast.com:3912/256239" ;}
    spp-diva() { sppc "sop://broker.sopcast.com:3912/253034/123456" ;}
    spp-divauniversal() { sppc "sop://broker.sopcast.com:3912/253034" ;}
    spp-ducktv() { sppc "sop://broker.sopcast.com:3912/148259" ;}
    spp-etnotv() { sppc "sop://broker.sopcast.com:3912/173116" ;}
    spp-euforia() { sppc "sop://broker.sopcast.com:3912/253473" ;}
    spp-eurosport1() { sppc "sop://broker.sopcast.com:3912/263056" ;}
    spp-filmbox() { sppc "sop://broker.sopcast.com:3912/148981" ;}
    spp-filmcafe() { sppc "sop://broker.sopcast.com:3912/256238" ;}
    spp-hbo+hd() { sppc "sop://51.15.38.157:3912/260710" ;}
    spp-idx() { sppc "sop://broker.sopcast.com:3912/256244" ;}
    spp-kanald() { sppc "sop://broker.sopcast.com:3912/149258" ;}
    spp-minimax() { sppc "sop://broker.sopcast.com:3912/148263" ;}
    spp-natgeowild() { sppc "sop://broker.sopcast.com:3912/253037" ;}
    spp-nationalgeographic() { sppc "sop://broker.sopcast.com:3912/148248" ;}
    spp-nationaltv() { sppc "sop://broker.sopcast.com:3912/253030" ;}
    spp-nickelodeon() { sppc "sop://broker.sopcast.com:3912/253472" ;}
    spp-paramount() { sppc "sop://broker.sopcast.com:3912/253033" ;}
    spp-primatv() { sppc "sop://broker.sopcast.com:3912/148086" ;}
    spp-procinema() { sppc "sop://broker.sopcast.com:3912/148249" ;}
    spp-protva() { sppc "sop://broker.sopcast.com:3912/149252" ;}
    spp-protvb() { sppc "sop://broker.sopcast.com:3912/151380" ;}
    spp-realitateatv() { sppc "sop://broker.sopcast.com:3912/253036" ;}
    spp-romaniatv() { sppc "sop://broker.sopcast.com:3912/148258" ;}
    spp-sport.ro() { sppc "sop://broker.sopcast.com:3912/178547" ;}
    spp-tlc() { sppc "sop://broker.sopcast.com:3912/148256" ;}
    spp-traveltv() { sppc "sop://broker.sopcast.com:3912/148885" ;}
    spp-tv1000() { sppc "sop://broker.sopcast.com:3912/256337/123456" ;}
    spp-tvpaprika() { sppc "sop://broker.sopcast.com:3912/148881" ;}
    spp-tv1000() { sppc "sop://broker.sopcast.com:3912/256337" ;}
    spp-tvr1() { sppc "sop://broker.sopcast.com:3912/148085" ;}
    spp-tvr2() { sppc "sop://broker.sopcast.com:3912/173286" ;}
    spp-viasathistory() { sppc "sop://broker.sopcast.com:3912/151300" ;}
    spp-zutv() { sppc "sop://broker.sopcast.com:3912/148252" ;}
    
    
    # format channel to functions quicker
    # e.g soprip newchannels.txt
    soprip() {
      if [ $# -lt 1 ]
      then
        echo -e "turn sopcast channel listing into functions"
        echo -e "copy sopcast list from http://sopcast.ucoz.com/ to text file"
        echo -e "\nUsage:\n$0 <filename.txt>"
        return 1
      fi
      # lowercase list; rm spaces/empty lines; merge name and link
      LIST=$(cat "$1" | tr '[:upper:]' '[:lower:]' | sed 's/ //g' | sed '$!N;s/\n/ /' | sed '/^$/d')
      echo $LIST | while read line; do
        SOPNAME=$(echo $line | awk '{print $1}')
        SOPLINK=$(echo $line | awk '{print $2}')
        # print into functions format
        echo "spp-"$SOPNAME"() { sppc \""$SOPLINK"\" ;}"
      done
    }
    
    
    #}}}


### references
- https://www.youtube.com/watch?v=Khvo4ge1PLQ
- Sopcast v2
  - https://www.youtube.com/watch?v=Dm7cFjhzgHo
  - https://github.com/gotbletu/shownotes/blob/master/sopcast_v2.txt

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


