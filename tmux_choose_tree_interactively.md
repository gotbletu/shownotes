# Tmux Swap Windows Pane Interactively
* tutorial video: [Link](https://youtu.be/_OOSbjHmLPY)
* offical website: [Link](https://www.youtube.com/user/gotbletu)
 
keywords: tmux terminal multiplexer choose-tree interactively commandline linux

### configuration
----
    vim ~/.tmux.conf
    
      bind-key W choose-tree -Zw "swap-window -t '%%'"
      bind-key P choose-tree -Zw "swap-pane -t '%%'"
      bind-key C-p choose-tree -Zw "move-pane -t '%%'"
      
      bind-key C-M-w command-prompt -p "Swap Current Window To? (e.g 3; 4; session_name:5)" "swap-window -t '%%'"
      bind-key C-M-p command-prompt -p "Swap Current Pane To? (e.g 2.0; session_name:4.0)" "swap-pane -t '%%'"
      bind-key M-p command-prompt -p "Move Current Pane To? (e.g 3.1; session_name:6.0)" "move-pane -t '%%'"
----
    
### references
- https://youtu.be/_OOSbjHmLPY
- https://www.reddit.com/r/commandline/comments/8wv0w6/interactively_moving_panes_to_other_windows/
- https://stackoverflow.com/questions/33396831/how-to-force-tmux-to-wait-for-output-from-command-prompt

### contact

                 _   _     _      _         
      __ _  ___ | |_| |__ | | ___| |_ _   _ 
     / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
    | (_| | (_) | |_| |_) | |  __/ |_| |_| |
     \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
     |___/                                  

- http://www.youtube.com/user/gotbletu
- https://twitter.com/gotbletu
- https://github.com/gotbletu
- gotbletu@gmail.com


