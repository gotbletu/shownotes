# W3M Custom External Commands
w3m web browser can call external commands using the "extbrowser" options in the config file.
Now we can use our own custom commands or scripts to execute commands on different links.
Such as playing videos with mpv, download files, ripping audio, copying to clipboard, adding torrent.
* tutorial video: [Link](https://www.youtube.com/watch?v=YzgCgarUa_M)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

### install requirements
    w3m mpv youtube-dl aria2 task-spooler xclip libnotify transmission-cli

### configuration
    vim ~/.w3m/config
    

    extbrowser $BROWSER
    extbrowser2 bash -c 'echo -n "$0" | xclip -selection clipboard && notify-send -t 5000 -i edit-copy "W3M URL Yank To Clipboard" "$0"'
    extbrowser3 bash -c 'tsp mpv --ontop --no-border --force-window --autofit=500x280 --geometry=-15-50 "$0" && notify-send -t 5000 -i video-x-generic "MPV Queue" "$0"'
    extbrowser4 bash -c 'TS_SOCKET=/tmp/w3m tsp youtube-dl -c --restrict-filenames -x --audio-format mp3 -o "~/Downloads/%(title)s.%(ext)s" "$0" && notify-send -t 5000 -i audio-x-generic "Youtube-DL: Ripping Audio" "$0"'
    extbrowser5 bash -c 'transmission-remote -a "$0" && notify-send -t 5000 -i emblem-downloads "Adding Torrent" "$0"'
    extbrowser6 bash -c 'TS_SOCKET=/tmp/w3m tsp aria2c -j 1 -c -d ~/Downloads "$0" && notify-send -t 5000 -i package-x-generic "Aria2c: Downloading" "$0"'
    extbrowser7
    extbrowser8
    extbrowser9


### keymap
    vim ~/.w3m/keymap


    ######################
    # My Custom Keybinding
    ######################
    
    # open current url (default: Shift+M)
    # e.g 2+Shift+M
    keymap  e EXTERN
    
    # open url under cursor (default: Esc+Shift+M)
    # e.g 2+Esc+Shift+M
    keymap  f EXTERN_LINK

### references
- https://www.youtube.com/watch?v=YzgCgarUa_M
- [w3m playlist](https://www.youtube.com/playlist?list=plqv94xwu9zz35yv0s6zmid5jos8qu19kh)
- [surfraw playlist](https://www.youtube.com/playlist?list=plqv94xwu9zz2e-ldbmbpdasa6a6jf4nyz)
- [task-spooler playlist](https://www.youtube.com/playlist?list=plqv94xwu9zz3qfx2jqahotg54nt0fq3vu)

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

