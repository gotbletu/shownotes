# Tmux 2.4 Custom Layout
allows you to pre-define tmux windows and pane to execute any programs or commands you wish

* tutorial video: [Link](https://www.youtube.com/watch?v=91d4KBDN-xM)
* offical website: [Link](https://tmux.github.io/)

### install requirements
    tmux

### configuration
    vim ~/.tmux.conf
    


    # -v = split horizontal
    # -h = split veritical

    # Template
    # tmux 2.4 custom layout https://www.youtube.com/watch?v=91d4KBDN-xM
    bind-key M-f new-window -n fm -c $HOME \; \
      send-keys -t fm 'figlet gotbletu' 'Enter' \; \
      split-window -t fm \; \
      send-keys -t fm 'ranger ~/Downloads' 'Enter' \; \
      new-window -n torr -c $HOME \; \
      send-keys -t torr 'tpb.sh' 'Enter' \; \
      split-window -t torr -h -p 25 \; \
      send-keys -t torr 'figlet hello' 'Enter' \; \
      send-keys -t torr 'figlet world' 'Enter'


    # Template for single line (no prefix key)
    # fzf-locate from https://www.youtube.com/watch?v=AbveiTAymy0
    bind-key -n 'M-\' new-window -n locate \; send-keys -t locate "fzf-locate && tmux kill-window\n"


### references
* tmux 2.4 custom layout https://www.youtube.com/watch?v=91d4KBDN-xM
* tmux custom layout 2.3 or lower https://www.youtube.com/watch?v=sxw-n5Du600
* tmux playlist https://www.youtube.com/playlist?list=PL5BE1545D8486D66D

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


