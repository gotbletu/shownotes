# Tmux Copy Mode (Vim Style)
Should work detect any tmux version and load the proper configurations for tmux copy mode
* tutorial video: [Link](https://www.youtube.com/watch?v=P8goLYv2vqs)
* offical website: [Link](https://tmux.github.io)

### install requirements
    tmux xclip xsel

### configuration
    vim ~/.tmux.conf


    #-------- Copy Mode (Vim Style) {{{
    #------------------------------------------------------
    # This section of hotkeys mainly work in copy mode and no where else
    
    # vim keys in copy and choose mode
    set-window-option -g mode-keys vi
    
    # copying selection vim style
    # http://jasonwryan.com/blog/2011/06/07/copy-and-paste-in-tmux/
    # https://github.com/myfreeweb/dotfiles/blob/master/tmux.conf
    bind-key Escape copy-mode			# enter copy mode; default [
    bind-key p paste-buffer				# paste; (default hotkey: ] )
    bind-key P choose-buffer 			# tmux clipboard history
    bind-key + delete-buffer \; display-message "Deleted current Tmux Clipboard History"
    
    # Send To Tmux Clipboard or System Clipboard
    bind-key < run-shell "tmux set-buffer -- \"$(xsel -o -b)\"" \; display-message "Copy To Tmux Clipboard"
    bind-key > run-shell 'tmux show-buffer | xsel -i -b' \; display-message "Copy To System Clipboard"
    
    # set the current tmux version (use this variable on if-shell commands)
    run-shell "tmux set-environment -g TMUX_VERSION $(tmux -V | cut -c 6-)"
    
    # vim copy mode rebinds for (tmux 2.4+)
    # https://shapeshed.com/custom-vim-bindings-in-tmux-2-4/
    # https://github.com/tmux/tmux/issues/754#issuecomment-303156000
    # https://stackoverflow.com/a/40902312
    # Note: rectangle-toggle (aka Visual Block Mode) > hit v then C-v to trigger it
    if-shell -b '[ "$(echo "$TMUX_VERSION >= 2.4" | bc)" = 1 ]' \
      'bind-key -T copy-mode-vi v send-keys -X begin-selection; \
      bind-key -T copy-mode-vi V send-keys -X select-line; \
      bind-key -T copy-mode-vi C-v send-keys -X rectangle-toggle; \
      bind-key -T choice-mode-vi h send-keys -X tree-collapse ; \
      bind-key -T choice-mode-vi l send-keys -X tree-expand ; \
      bind-key -T choice-mode-vi H send-keys -X tree-collapse-all ; \
      bind-key -T choice-mode-vi L send-keys -X tree-expand-all ; \
      bind-key -T copy-mode-vi MouseDragEnd1Pane send-keys -X copy-pipe "xclip -in -selection clipboard"; \
      bind-key -T copy-mode-vi y send-keys -X copy-pipe "xclip -in -selection clipboard"'
    
    # vim copy mode rebinds for (tmux 2.3 or lower)
    if-shell -b '[ "$(echo "$TMUX_VERSION < 2.4" | bc)" = 1 ]' \
      'bind-key -t vi-copy v begin-selection; \
      bind-key -t vi-copy V select-line; \
      bind-key -t vi-copy C-v rectangle-toggle; \
      bind-key -t vi-choice h tree-collapse; \
      bind-key -t vi-choice l tree-expand; \
      bind-key -t vi-choice H tree-collapse-all; \
      bind-key -t vi-choice L tree-expand-all; \
      bind-key -t vi-copy MouseDragEnd1Pane copy-pipe "xclip -in -selection clipboard"; \
      bind-key -t vi-copy y copy-pipe "xclip -in -selection clipboard"'

    #}}}

### references
- https://www.youtube.com/watch?v=P8goLYv2vqs
- [Youtube Tmux Playlist](https://www.youtube.com/playlist?list=PL5BE1545D8486D66D)

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


