# Newsbeuter Macro
couple of macros i use with my terminal rss reader, we dont need to reinvent the wheel, we are just going to use existing tools and chain them together.
* tutorial video: [Link](https://www.youtube.com/watch?v=mRnMg2V9n-E)
* offical website: [Link](http://newsbeuter.org/)

### install requirements
    newsbeuter

### how to use newsbeuter
- newsbeuter playlist: https://www.youtube.com/playlist?list=PLqv94xWU9zZ30jHFe8pqC5qES6ya6v2sE

### variables
    vim ~/.bashrc or ~/.zshrc
    
    export BROWSER=chromium
    export BROWSERCLI=w3m

### configuration
    vim ~/.newsbeuter/config
    
    
    browser $BROWSER
    save-path ~/.newsbeuter/saved_articles
    
    #-------- macros {{{
    #------------------------------------------------------
    # Note: macro prefix key ( default: , )
    
    # open in cli web browser
    # w3m: https://www.youtube.com/watch?v=Z22cFTB-uqg
    # tmux: https://www.youtube.com/watch?v=ZNM1KfqpyGo
    # macro o set browser "$BROWSERCLI %u"; open-in-browser ; set browser "$BROWSER %u"
    macro o set browser "tmux split-window && tmux send-keys '$BROWSERCLI %u && tmux kill-pane\n'"; open-in-browser ; set browser "$BROWSER %u"
    
    # read reddit comments with rtv (reddit terminal viewer)
    # rtv: https://www.youtube.com/watch?v=jc2ZVSof5-g
    # macro r set browser "rtv -l %u"; open-in-browser ; set browser "$BROWSER %u"
    macro r set browser "tmux split-window && tmux send-keys 'rtv -l %u && tmux kill-pane\n'"; open-in-browser ; set browser "$BROWSER %u"
    
    # add video or audio to play queue using mpv (requires: task-spooler, mpv, youtube-dl)
    # task-spooler: https://www.youtube.com/watch?v=wv8D8wT20ZY
    # youtube-dl: https://www.youtube.com/watch?v=MFxlwVhwayg
    macro p set browser "tsp mpv --ontop --no-border --force-window --autofit=500x280 --geometry=-15-10 %u"; open-in-browser ; set browser "$BROWSER %u"
    
    # copy url to clipboard "yank"
    # xclip: https://www.youtube.com/watch?v=fKP0FLp3uW0
    macro y set browser "echo -n %u | xclip -selection clipboard"; open-in-browser ; set browser "$BROWSER %u"
    

    # read saved files
    # ranger: https://www.youtube.com/watch?v=qooLR8NmYKs
    # w3m context url: https://www.youtube.com/watch?v=C7YPjbrTeCs
    macro s set browser "tmux split-window && tmux send-keys 'ranger ~/.newsbeuter/saved_articles && tmux kill-pane\n'" ; open-in-browser ; set browser "$BROWSER %u"
    
    # }}}
    

### references
- newsbeuter playlist: https://www.youtube.com/playlist?list=PLqv94xWU9zZ30jHFe8pqC5qES6ya6v2sE
- w3m: https://www.youtube.com/watch?v=Z22cFTB-uqg
- tmux: https://www.youtube.com/watch?v=ZNM1KfqpyGo
- rtv: https://www.youtube.com/watch?v=jc2ZVSof5-g
- task-spooler: https://www.youtube.com/watch?v=wv8D8wT20ZY
- youtube-dl: https://www.youtube.com/watch?v=MFxlwVhwayg
- xclip: https://www.youtube.com/watch?v=fKP0FLp3uW0
- ranger: https://www.youtube.com/watch?v=qooLR8NmYKs
- w3m context url: https://www.youtube.com/watch?v=C7YPjbrTeCs

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


