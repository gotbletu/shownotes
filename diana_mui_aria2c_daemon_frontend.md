# Diana-MUI - Menu User Interface To Aria2c Daemon
a poorman's frontend to diana (which is a commandline frontend to aria2 daemon)

* tutorial video: [Link](https://youtu.be/y59JwlYsrAE)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

### install requirements
    bash  aria2  coreutils  fzf  gawk  procps-ng  xdg-utils diana (https://github.com/baskerville/diana)

### download required scripts
    $ wget https://raw.githubusercontent.com/gotbletu/shownotes/master/diana-mui
    $ wget https://raw.githubusercontent.com/gotbletu/shownotes/master/diana-progress

### usage
    $ diana-mui

### configuration
    run the diana-mui and change the download path (hit D). Restart script and start the daemon (hit s)
    
### optional: w3m keymap
    vim ~/.w3m/keymap
    
    # add to download active list
    keymap  xd      EXTERN_LINK   'diana add'
    # add to download paused list
    keymap  XD      EXTERN_LINK   'diana --pause add'
    # open diana-mui script
    keymap  xD      SHELL         'diana-mui'

### references
- https://youtu.be/y59JwlYsrAE
- [aria2c - The Ultra Fast Download Utility - Linux CLI](https://www.youtube.com/watch?v=ZMiyeNxcBSY)
- [W3M Web Browser Playlist](https://www.youtube.com/playlist?list=PLqv94xWU9zZ35Yv0s6zMID5JoS8qu19Kh)
- [Transmission CLI TUI Torrent Client](https://www.youtube.com/playlist?list=PLqv94xWU9zZ05Dbc551z14Eerj2xPWyVt)
- https://github.com/baskerville/diana
- [Undocumented Diana Features](https://github.com/baskerville/diana/blob/87c5b1b57425585b4c0f543edcf7e9038cf793c5/diana#L427-L429)
- [Aria2c Integration Add-on Chrome Chromium](https://chrome.google.com/webstore/detail/aria2c-integration/edcakfpjaobkpdfpicldlccdffkhpbfk)

### contact

                 _   _     _      _         
      __ _  ___ | |_| |__ | | ___| |_ _   _ 
     / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
    | (_| | (_) | |_| |_) | |  __/ |_| |_| |
     \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
     |___/                                  

- http://www.youtube.com/user/gotbletu
- https://twitter.com/gotbletu
- https://github.com/gotbletu
- gotbletu@gmail.com


tags: gotbletu youtube tutorial screencast tips and tricks guide hidden gems shownotes computer opensource free software linuxmint linux distro ubuntu debian fedora archlinux terminal console tty commandline cli tui mui ncurses zsh shell bash curses text user interface scripts scripting server aria2c aria2 aria daemon download manager downloader w3m web browser opendirectories
