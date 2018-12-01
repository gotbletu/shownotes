# W3M Web Browser - EXTERN, EXTERN_LINK, SHELL Custom Commands Keybindings

custom keybindings for the terminal web browser w3m

* tutorial video: [Link](https://youtu.be/b6YMAsiZSTM)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

### install packages
    w3m xsel mpv youtube-dl feh task-spooler tmux procps-ng wget aria2 transmission-cli

### configuration
        vim ~/.w3m/keymap

        # External Commands {{{
        # EXTERN_LINK = under cursor
        # EXTERN      = current page
        
        # yank url to clipboard
        keymap  yy      EXTERN_LINK   '(echo -n %s | xsel -b)'
        keymap  YY      EXTERN        '(echo -n %s | xsel -b)'
        # yank url to tmux clipboard
        keymap  ys      EXTERN_LINK   'tmux set-buffer'
        keymap  YS      EXTERN        'tmux set-buffer'
        
        # open gui browser
        keymap  xw      EXTERN_LINK   '$BROWSER'
        %% keymap  xw      EXTERN_LINK   'chromium'
        keymap  XW      EXTERN        '$BROWSER'
        keymap  xn      EXTERN_LINK   '$BROWSER_PRIVATE'
        %% keymap  xn      EXTERN_LINK   'chromium --incognito'
        keymap  XN      EXTERN        '$BROWSER_PRIVATE'
        
        # queue download file (task-spooler)
        keymap  xd      EXTERN_LINK   'TS_SOCKET=/tmp/w3m tsp aria2c -j 1 -x 2 -c -d ~/Downloads'
        keymap  xD      EXTERN_LINK   'TS_SOCKET=/tmp/w3m tsp wget -c -P ~/Downloads'
        
        # queue external media player (task-spooler) e.g youtube, video links
        keymap  xm      EXTERN_LINK   'tsp mpv --ontop --no-border --force-window --autofit=500x280 --geometry=-15-53'
        keymap  XM      EXTERN        'tsp mpv --ontop --no-border --force-window --autofit=500x280 --geometry=-15-53'
        
        # open external image viewer
        keymap  xi      EXTERN_LINK   'w3m -o display_image=1 -o imgdisplay=w3mimgdisplay'
        keymap  xI      EXTERN_LINK   'feh -. -x -B black -g 900x600-15+60 %s &'
        keymap  xg      EXTERN_LINK   'mpv --loop --quiet --ontop --no-border --force-window --autofit=900x600 --geometry=-15+60'
        
        # add torrent or magnetlinks
        keymap  xt      EXTERN_LINK   'transmission-remote --add'
        
        # basic task-spooler view, cat, clear
        keymap  xs      SHELL         'watch TS_SOCKET=/tmp/w3m tsp'
        keymap  XS      SHELL         'clear && TS_SOCKET=/tmp/w3m tsp -c'
        keymap  xc      SHELL         'clear && TS_SOCKET=/tmp/w3m tsp -C'
        
        # }}}

### references
- w3m playlist https://www.youtube.com/playlist?list=PLqv94xWU9zZ35Yv0s6zMID5JoS8qu19Kh
- task-spooler playlist https://www.youtube.com/playlist?list=PLqv94xWU9zZ3QfX2jQaHotg54NT0Fq3Vu

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


