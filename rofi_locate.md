# Rofi-locate - Search files and folders on your system
* tutorial video: [Link](https://www.youtube.com/watch?v=Oks3p_R54IU)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

### install requirements
    rofi mlocate

### colors
    vim ~/.Xresources
    

    !-------- ROFI Color theme {{{
    !------------------------------------------------------
    ! https://davedavenport.github.io/rofi/p11-Generator.html
    rofi.color-enabled: true
    rofi.color-window: #000000, #000000, #000000
    rofi.color-normal: #000000, #b3e774, #000000, #b3e774, #000000
    rofi.color-active: #000000, #b3e774, #000000, #b3e774, #000000
    rofi.color-urgent: #000000, #b3e774, #000000, #b3e774, #000000
    ! }}}


### hotkey binding command (better version) Thanks [@smilingverb](https://github.com/gotbletu/shownotes/issues/16)
    locate home media | rofi -threads 0 -width 100 -dmenu -i -p "locate:" | xargs -r -0 xdg-open

### hotkey binding command (alternative version with colors without needing ~/.Xresources)
    xdg-open "$(locate home media | rofi -threads 0 -width 100 -color-window "#000000, #000000, #000000" -color-normal "#000000, #b3e774, #000000, #b3e774, #000000" -color-active "#000000, #b3e774, #000000, #b3e774, #000000" -color-urgent "#000000, #b3e774, #000000, #b3e774, #000000" -dmenu -i -p "locate:")"


### refresh locate command database
    sudo updatedb

### references
- https://www.youtube.com/watch?v=Oks3p_R54IU
- https://davedavenport.github.io/rofi/
- rofi playlist: https://www.youtube.com/playlist?list=PLqv94xWU9zZ0LVP1SEFQsLEYjZC_SUB3m

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


