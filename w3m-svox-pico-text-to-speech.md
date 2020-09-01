# SVOX Pico TTS Text To Speech with W3M Web Browser
Text-to-speech engine used on Android phones. Works on linux also.

* tutorial video: [Link](https://youtu.be/BijKHsvOvxc)

### install requirements
    aur/svox-pico-bin   # archlinux
    libttspico-utils    # ubuntu / debian
    picospeaker         # https://gitlab.com/ky1e/picospeaker
    
### configuration
    vim ~/.w3m/keymap
    
    keymap  \\\s    COMMAND "SHELL 'picospeaker $W3M_CURRENT_WORD 2>/dev/null'"
    keymap  \\\a    COMMAND "PRINT /tmp/picospeaker.txt ; SHELL 'picospeaker < /tmp/picospeaker.txt 2>/dev/null &'"
    keymap  \\\k    COMMAND "SHELL 'killall play'"

### usage
    press \a on a webpage for the pico tts program to read it aloud

### references
- W3M playlist https://www.youtube.com/playlist?list=PLqv94xWU9zZ35Yv0s6zMID5JoS8qu19Kh
- https://gitlab.com/ky1e/picospeaker
- https://aur.archlinux.org/packages/svox-pico-bin/
- https://android.googlesource.com/platform/external/svox/+/master
- https://youtu.be/BijKHsvOvxc

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


