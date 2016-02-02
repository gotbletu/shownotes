# Bang! Previous Command Hotkeys
print previous command but only the first nth argument.
Alt+1, Alt+2 ...etc

* tutorial video: [Link](https://www.youtube.com/watch?v=R5fca6IUxHA)

### install requirements
    zsh or bash

### bash 
    vim ~/.bashrc && source ~/.bashrc
    
    # enable history verification:
    # bang commands (!, !!, !?) will print to shell and not be auto executed
    # http://superuser.com/a/7416
    shopt -s histverify

    # Bang! Previous Command Hotkeys
    # print previous command but only the first nth arguments
    # Alt+1, Alt+2 ...etc
    bind '"\e1": "!:0 \n"'
    bind '"\e2": "!:0-1 \n"'
    bind '"\e3": "!:0-2 \n"'
    bind '"\e4": "!:0-3 \n"'
    bind '"\e5": "!:0-4 \n"'
    bind '"\e`": "!:0- \n"'     # all but the last word

    
### zsh 
    vim ~/.zshrc && source ~/.zshrc
    

    # Bang! Previous Command Hotkeys
    # print previous command but only the first nth arguments
    # Alt+1, Alt+2 ...etc
    bindkey -s '\e1' "!:0 \t"
    bindkey -s '\e2' "!:0-1 \t"
    bindkey -s '\e3' "!:0-2 \t"
    bindkey -s '\e4' "!:0-3 \t"
    bindkey -s '\e5' "!:0-4 \t"
    bindkey -s '\e`' "!:0- \t"     # all but the last word
    
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


