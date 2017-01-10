# Tmux Full Window Split
* tutorial video: [Link](https://www.youtube.com/watch?v=jt_tz0zXxQE)
* offical website: [Link](https://tmux.github.io/)

### install requirements
    tmux


### configuration
    vim ~/.tmux.conf

    
    # split pane (tmux 1.9+)
    bind-key \ split-window -h -c "#{pane_current_path}"	# vertical split (default prefix-%)
    bind-key - split-window -v -c "#{pane_current_path}"	# horizontal split (default prefix-")
    
    # split full window (tmux 2.3+)
    bind-key | split-window -fh -c "#{pane_current_path}"	# vertical split
    bind-key _ split-window -fv -c "#{pane_current_path}"	# horizontal split

### references
* Tmux Playlist: https://www.youtube.com/playlist?list=PL5BE1545D8486D66D
 
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


