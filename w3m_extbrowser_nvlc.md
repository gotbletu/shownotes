# W3M + Tmux + nVLC = Browser Extension For Streaming Media
scan url for media links then generate a playlist to stream it

* tutorial video: [Link](https://www.youtube.com/watch?v=QczYT67JqYs)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

### install requirements
    w3m tmux vlc bash

### download script
    
    mkdir -pv ~/.scripts/w3m_scripts_collection
    cd ~/.scripts/w3m_scripts_collection
    wget https://raw.githubusercontent.com/gotbletu/shownotes/master/w3m_scripts_collection/w3m_extbrowser_tmux_w3mplay_via_nvlc.sh
    chmod +x ~/.scripts/w3m_scripts_collection/w3m_extbrowser_tmux_w3mplay_via_nvlc.sh

### configuration
    vim ~/.w3m/config
    
    extbrowser8 bash -c '(tmux set-buffer "$0") && ~/.scripts/w3m_scripts_collection/w3m_extbrowser_tmux_w3mplay_via_nvlc.sh'

### configuration (hotkey references)
    vim ~/.w3m/keymap

    ############################ Display using an external browser (EXTERN)
    # open current url (default: Shift+M); e.g 2+Shift+M
    keymap  ]       EXTERN
    ############################ Display target using an external browser (EXTERN_LINK)
    # open url under cursor (default: Esc+Shift+M); e.g 2+Esc+Shift+M
    keymap  e       EXTERN_LINK

----
usage example: open w3m > go to url with media files > hit **8]**

### W3M as URL Viewer
- https://www.youtube.com/watch?v=C7YPjbrTeCs
- currently: i bind this to prefix + u in tmux.conf

### references
- https://www.youtube.com/watch?v=QczYT67JqYs
- W3M Context View URL Extractor - Linux TUI https://www.youtube.com/watch?v=C7YPjbrTeCs
- nvlc - Media Player - Linux TUI https://www.youtube.com/watch?v=7y_58wpHuFE
- w3m - Custom External Commands - Linux TUI https://www.youtube.com/watch?v=YzgCgarUa_M
- surfraw playlist https://www.youtube.com/playlist?list=PLqv94xWU9zZ2e-lDbmBpdASA6A6JF4Nyz

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


