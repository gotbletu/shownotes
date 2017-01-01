# Rofi Websearches and Bookmarks using Surfraw
combining the power of **surfraw** to handle web searches and bookmarks into the **rofi** launcher. Bookmarks has tags support, making easier for users to remember all the sh/t they got.
* tutorial video: [Link](https://www.youtube.com/watch?v=36QV8VE5PVY)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

### install requirements
    rofi
    surfraw

### code for hotkey
_Note: What ever distro you are using, just bind it to a hotkey, it also might be best to create a bash script out of it since some desktop environment hotkey manager does not like direct bash code._


    # rofi-surfraw-websearch: web search via surfraw
    surfraw -browser=$BROWSER $(sr -elvi | awk -F'-' '{print $1}' | sed '/:/d' | awk '{$1=$1};1' | rofi -kb-row-select "Tab" -kb-row-tab "Control+space" -color-window "#000000, #000000, #000000" -color-normal "#000000, #b3e774, #000000, #b3e774, #000000" -color-active "#000000, #b3e774, #000000, #b3e774, #000000" -color-urgent "#000000, #b3e774, #000000, #b3e774, #000000" -dmenu -mesg ">>> Tab = Autocomplete" -i -p "websearch: ")
    
    # rofi-surfraw-bookmarks: bookmarks with tags via surfraw
    surfraw -browser=$BROWSER "$(cat ~/.config/surfraw/bookmarks | sed '/^$/d' | sed '/^#/d' | sed '/^\//d' | sort -n | rofi -color-window "#000000, #000000, #000000" -color-normal "#000000, #b3e774, #000000, #b3e774, #000000" -color-active "#000000, #b3e774, #000000, #b3e774, #000000" -color-urgent "#000000, #b3e774, #000000, #b3e774, #000000" -dmenu -mesg ">>> Edit to add new bookmarks at ~/.config/surfraw/bookmarks" -i -p "bookmarks: ")"
    
### edit or add new bookmarks
    vim ~/.config/surfraw/bookmarks
    
    # format example: name url ;; tags
    gotbletu    https://www.youtube.com/user/gotbletu   ;; youtube screencast year of the linux desktop
    
    
### how to create your own websearches for surfraw (aka elvi/elvis)
- https://www.youtube.com/watch?v=FvimaTL_kJU

### references
- [Surfraw Youtube Playlist](https://www.youtube.com/playlist?list=PLqv94xWU9zZ2e-lDbmBpdASA6A6JF4Nyz)
- [Rofi Youtube Playlist](https://www.youtube.com/playlist?list=PLqv94xWU9zZ0LVP1SEFQsLEYjZC_SUB3m)
- [Fuzzy Finder FZF Youtube Playlist](https://www.youtube.com/playlist?list=PLqv94xWU9zZ2fMsMMDF4PjtNHCeBFbggD)


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


