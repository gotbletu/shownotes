# ncdc - Direct Connect Client
Modern and lightweight direct connect client with a friendly ncurses interface
* tutorial video: [Link](https://www.youtube.com/watch?v=mwE0pzsVGt4)
* offical website: [Link](http://dev.yorhel.nl/ncdc)

### install requirements
    ncdc

### help page
https://dev.yorhel.nl/ncdc/man#GETTING_STARTED

### hublist
- http://www.te-home.net/?do=hublist
- http://www.thehublist.com/?do=hubs

### set basic info
    /set nick USERNAME
    /set description sharing is caring :)
    /set connection 10
    /share "music" /home/USERNAME/Music
    /share "bankai" /media/Bankai

### change settings
    /help set
    /hset              # settings per hub
    /set               # show a list of global settings
    /unset
    /unshare

### my color themes
    /set color*        # show only color settings
    
    /set color_list_default yellow
    /set color_list_header white,bold
    /set color_list_select red,bold
    /set color_log_default red
    /set color_log_highlight yellow,bold
    /set color_log_join cyan,bold
    /set color_log_nick blue
    /set color_log_ownnick white,bold
    /set color_log_quit cyan
    /set color_log_time black,bold
    /set color_separator yellow,reverse
    /set color_tab_active red,bold
    /set color_tabprio_high magenta,bold
    /set color_tabprio_low black,bold
    /set color_tabprio_med cyan,bold
    /set color_title yellow,reverse

### connect to a hub
    /help connect
    
    /open globalconnect
    /connect dchub://tankafett.biz/
    
    /open tankafett
    /connect dchub://traphouse.tankafett.biz:420
    
    /open destinymagneto
    /connect dchub://wolverine.x-menworld.it:412/
    
    # open a hub (hub are auto saved once you connect once)
    /open #tankafett

### commands
    /help
    /queue              # open queue window
    /connections        # show connections/upload/download window

### searches
    /search [keyword]
    
      -hub      Search the current hub only. (default)
      -all      Search all connected hubs, except those with `chat_only' set.
      -le  <s>  Size of the file must be less than <s>.
      -ge  <s>  Size of the file must be larger than <s>.
      -t   <t>  File must be of type <t>. (see below)
      -tth <h>  TTH root of this file must match <h>.
    File sizes (<s> above) accept the following suffixes: G (GiB), M (MiB) and K (KiB).
    
    The following file types can be used with the -t option:
    
      1  any      Any file or directory. (default)
      2  audio    Audio files.
      3  archive  (Compressed) archives.
      4  doc      Text documents.
      5  exe      Windows executables.
      6  img      Image files.
      7  video    Video files.
      8  dir      Directories.


### hotkey
    Alt-#               # switch window
    Alt-c               # close window
    Alt-q               # open queue tab
    Alt-n               # open connections tab
    Alt+o               # open own file list
    ?                   # [result window] show a list of hotkeys
    d                   # [result window] add to download
    d                   # [queue window] delete from queue

### references
- https://en.wikipedia.org/wiki/Direct_Connect_(protocol)
- https://dev.yorhel.nl/ncdc/man#GETTING_STARTED
- http://www.te-home.net/?do=hublist
- http://www.thehublist.com/?do=hubs

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


