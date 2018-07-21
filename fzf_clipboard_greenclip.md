# fzf-clipboard
manage clipboard history via the terminal
* tutorial video: [Link](https://www.youtube.com/watch?v=Vzt0tVNrJ0A)
* offical website: [Link](https://github.com/erebe/greenclip)

### install requirements
    greenclip fzf xclip

### add to autostart
    greenclip daemon

### configuration
    vim ~/.bashrc or ~/.zshrc
    

    # start fuzzy finder frontend to greenclip
    fzf-clipboard() { echo -n "$(greenclip print | fzf -e -i)" | xclip -selection clipboard ;}
    
    # greenclip configuration settings
    cfg-greenclip() { killall greenclip ; $EDITOR ~/.config/greenclip.cfg && nohup greenclip daemon > /dev/null 2>&1 & }

    # greenclip reload
    rld-greenclip() { killall greenclip ; nohup greenclip daemon > /dev/null 2>&1 & }
    
    # greenclip clear history
    derez-greenclip() { killall greenclip ; rm ~/.cache/greenclip.history && nohup greenclip daemon > /dev/null 2>&1 & }


### references
- https://www.youtube.com/watch?v=Vzt0tVNrJ0A
- [Fuzzy Finder Playlist](https://www.youtube.com/playlist?list=PLqv94xWU9zZ2fMsMMDF4PjtNHCeBFbggD)
- [Rofi Clipboard Manager via Greenclip - Linux GUI](https://www.youtube.com/watch?v=4IycORAdW9M)
- https://github.com/erebe/greenclip
- https://github.com/junegunn/fzf

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


