# SVOX Pico TTS Text To Speech with W3M Web Browser
Text-to-speech engine used on Android phones. Works on linux also.

* tutorial video: [Link](https://youtu.be/BijKHsvOvxc)

### install requirements
    aur/svox-pico-bin   # archlinux
    libttspico-utils    # ubuntu / debian
    picospeaker         # https://gitlab.com/ky1e/picospeaker
    toggle-process.zsh  # https://github.com/chimay/scripts/blob/master/zsh/toggle-process.zsh
    rdrview             # https://github.com/eafer/rdrview
    
### configuration
    vim ~/.w3m/keymap
    
    # say current word
    keymap  \\\s    COMMAND "READ_SHELL 'picospeaker $W3M_CURRENT_WORD 2>/dev/null' ; BACK"
    
    # read current page
    keymap  \\\a    COMMAND "READ_SHELL 'rm /tmp/picospeaker.txt' ; BACK ; PRINT /tmp/picospeaker.txt ; SHELL 'picospeaker < /tmp/picospeaker.txt 2>/dev/null &'"
    
    # strip junk from current page and read current page
    keymap  \\\R    COMMAND "READ_SHELL 'rdrview -H $W3M_URL 2> /dev/null 1> /tmp/rdrview.html' ; BACK ; LOAD /tmp/rdrview.html ; READ_SHELL 'rm /tmp/picospeaker.txt' ; BACK ; PRINT /tmp/picospeaker.txt ; SHELL 'picospeaker < /tmp/picospeaker.txt 2>/dev/null &'"
    
    # stop current text to speech process
    keymap  \\\k    COMMAND "READ_SHELL 'killall play' ; BACK"
    
    # toggle (pause/play) current text to speech process
    keymap  \\\p    COMMAND "READ_SHELL 'toggle-process.zsh /usr/bin/play' ; BACK"
    

### usage
    press \a on a webpage for the pico tts program to read it aloud

### references
- W3M playlist https://www.youtube.com/playlist?list=PLqv94xWU9zZ35Yv0s6zMID5JoS8qu19Kh
- https://gitlab.com/ky1e/picospeaker
- https://aur.archlinux.org/packages/svox-pico-bin/
- https://android.googlesource.com/platform/external/svox/+/master
- https://youtu.be/BijKHsvOvxc
- https://github.com/chimay/scripts/blob/master/zsh/toggle-process.zsh

### contact

                 _   _     _      _         
      __ _  ___ | |_| |__ | | ___| |_ _   _ 
     / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
    | (_| | (_) | |_| |_) | |  __/ |_| |_| |
     \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
     |___/                                  

- http://www.youtube.com/user/gotbletu
- https://lbry.tv/@gotbletu
- https://twitter.com/gotbletu
- https://github.com/gotbletu
- gotbletu@gmail.com


