# Rofi Clipboard Manager via Greenclip
Greenclip is a simple clipboard manager.
Now you can search your clipboard history using rofi.
This one we are going to add it to our rofi-bangs script.
If you do not want to use it with rofi-bangs then just follow the directions on the greenclip website, instead of using this wiki.

* tutorial video: [Link](https://www.youtube.com/watch?v=4IycORAdW9M)
* offical website: [Link](https://github.com/erebe/greenclip)

### install requirements
    rofi greenclip
----
- https://github.com/erebe/greenclip

### script requirements
https://github.com/gotbletu/shownotes/blob/master/rofi-scripts-collection/rofi-bangs.sh

### what is rofi-bangs?
https://www.youtube.com/watch?v=kxJClZIXSnM

### configuration (for rofi-bangs script)
    vim rofi-bangs.sh
    

    # greenclip clipboard history
    # source: https://github.com/erebe/greenclip
    COMMANDS["clipboard"]='rofi -modi "clipboard:greenclip print" -show clipboard'
    LABELS["clipboard"]=""
    
### add to autostart
    greenclip daemon

### change clipboard size
    killall greenclip
    vim ~/.config/greenclip.cfg
    greenclip daemon &

### references
- https://www.youtube.com/watch?v=4IycORAdW9M
- [rofi playlist](https://www.youtube.com/playlist?list=PLqv94xWU9zZ0LVP1SEFQsLEYjZC_SUB3m)
- https://github.com/erebe/greenclip
- https://davedavenport.github.io/rofi/

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


