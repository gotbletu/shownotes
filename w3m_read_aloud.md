# W3M Read Aloud (Text to Speech)
add read aloud features to w3m terminal web browser, with hotkeys to pause, stop and play

* tutorial video: [Link](https://youtu.be/DD0K0cpfAXo)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

#### bindings ~/.w3m/keymap

----

    ############################ Text to speech TTS (espeak-ng) {{{
    keymap  \\\s    COMMAND "READ_SHELL 'espeak $W3M_CURRENT_WORD 2>/dev/null' ; BACK"  # say current word (text to speech)
    keymap  \\\a    COMMAND "READ_SHELL 'rm /tmp/espeak.txt'; BACK ; PRINT /tmp/espeak.txt ; READ_SHELL 'espeak-ng -f /tmp/espeak.txt -w /tmp/espeak.wav && setsid mpv --no-video /tmp/espeak.wav 2>/dev/null &'; BACK" # read aloud current page (Ctrl-c to continue browsing)
    keymap  \\\t    COMMAND "READ_SHELL 'rdrview -H $W3M_CURRENT_LINK 2>/dev/null' ; VIEW ; DELETE_PREVBUF; READ_SHELL 'rm /tmp/espeak.txt'; BACK ; PRINT /tmp/espeak.txt ; READ_SHELL 'espeak-ng -f /tmp/espeak.txt -w /tmp/espeak.wav && setsid mpv --no-video /tmp/espeak.wav 2>/dev/null &'; BACK" # remove html junk then read aloud current page (Ctrl-c to continue browsing)
    keymap  \\\T    COMMAND "READ_SHELL 'rdrview -H $W3M_URL 2>/dev/null' ; VIEW ; DELETE_PREVBUF; READ_SHELL 'rm /tmp/espeak.txt'; BACK ; PRINT /tmp/espeak.txt ; READ_SHELL 'espeak-ng -f /tmp/espeak.txt -w /tmp/espeak.wav && setsid mpv --no-video /tmp/espeak.wav 2>/dev/null &'; BACK" # remove html junk then read aloud current page (Ctrl-c to continue browsing)
    # }}}
    
    
    ########################### Text to speech TTS (SVOX Pico) {{{
    # https://aur.archlinux.org/packages/svox-pico-bin/
    # https://web.archive.org/web/20230729001652/https://aur.archlinux.org/packages/svox-pico-bin
    keymap \\\s    COMMAND "READ_SHELL 'echo $W3M_CURRENT_WORD | pico2wave -w /tmp/pico2wave.wav' ; BACK ; READ_SHELL 'mpv --no-video /tmp/pico2wave.wav >/dev/null 2>&1 &' ; BACK" ## Text to Speech - Svox Pico - Read aloud word on cursor
    keymap \\\a    COMMAND "READ_SHELL 'rm /tmp/pico2wave.txt' ; BACK ; PRINT /tmp/pico2wave.txt ; READ_SHELL 'pico2wave -w /tmp/pico2wave.wav < /tmp/pico2wave.txt' ; BACK ; READ_SHELL 'mpv --no-video /tmp/pico2wave.wav >/dev/null 2>&1 &'; BACK" ## Text to Speech - Svox Pico - Read aloud page
    keymap \\\t    COMMAND "READ_SHELL 'rdrview -H $W3M_CURRENT_LINK 2>/dev/null' ; VIEW ; DELETE_PREVBUF ; READ_SHELL 'rm /tmp/pico2wave.txt' ; BACK ; PRINT /tmp/pico2wave.txt ; READ_SHELL 'pico2wave -w /tmp/pico2wave.wav < /tmp/pico2wave.txt' ; BACK ; READ_SHELL 'mpv --no-video /tmp/pico2wave.wav >/dev/null 2>&1 &'; BACK" ## Text to Speech - Svox Pico - Clean page with rdrview then read aloud page (cursor link)
    keymap \\\T    COMMAND "READ_SHELL 'rdrview -H $W3M_URL 2>/dev/null' ; VIEW ; DELETE_PREVBUF ; READ_SHELL 'rm /tmp/pico2wave.txt' ; BACK ; PRINT /tmp/pico2wave.txt ; READ_SHELL 'pico2wave -w /tmp/pico2wave.wav < /tmp/pico2wave.txt' ; BACK ; READ_SHELL 'mpv --no-video /tmp/pico2wave.wav >/dev/null 2>&1 &'; BACK" ## Text to Speech - Svox Pico - Clean page with rdrview then read aloud page (current page)
    # }}}


    ############################ Media keys (playerctl/mpris) {{{
    # requires: mpv mpv-mpris playerctl
    keymap \\\1 COMMAND "READ_SHELL 'amixer set Master toggle'; BACK"           ## Playerctl& - Toggle Volume mute
    keymap \\\2 COMMAND "READ_SHELL 'playerctl --player=mpv volume 0.2-'; BACK" ## Playerctl& - Volume down (mpv)
    keymap \\\3 COMMAND "READ_SHELL 'playerctl --player=mpv volume 0.2+'; BACK" ## Playerctl& - Volume up (mpv)
    keymap \\\4 COMMAND "READ_SHELL 'playerctl --player=mpv stop'; BACK"        ## Playerctl& - Quit/stop/exit (mpv)
    keymap \\\5 COMMAND "READ_SHELL 'playerctl --player=mpv shuffle on'; BACK"  ## Playerctl& - Shuffle on (mpv)
    keymap \\\6 COMMAND "READ_SHELL 'playerctl --player=mpv previous'; BACK"    ## Playerctl& - Playlist previous (mpv)
    keymap \\\7 COMMAND "READ_SHELL 'playerctl --player=mpv play-pause'; BACK"  ## Playerctl& - Toggle play/pause (mpv)
    keymap \\\8 COMMAND "READ_SHELL 'playerctl --player=mpv next'; BACK"        ## Playerctl& - Playlist next (mpv)
    keymap \\\9 COMMAND "READ_SHELL 'playerctl --player=mpv position 5-'; BACK" ## Playerctl& - Seek/rewind (mpv)
    keymap \\\0 COMMAND "READ_SHELL 'playerctl --player=mpv position 5+'; BACK" ## Playerctl& - Seek/forward (mpv)
    
    # }}}

----

#### contact

                 _   _     _      _
      __ _  ___ | |_| |__ | | ___| |_ _   _
     / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
    | (_| | (_) | |_| |_) | |  __/ |_| |_| |
     \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
     |___/

- https://www.youtube.com/user/gotbletu
- https://odysee.com/@gotbletu
- https://github.com/gotbletu

