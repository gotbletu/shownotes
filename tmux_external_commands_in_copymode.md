# Tmux Run External Commands In Copy Mode
emulate right click **"search google for {text}"** like you do in GUI web browsers. We can do other custom commands also like search highlighted text in wikipedia, translate, text to speech and many others. Think of other stuff to use it with like **mps-youtube, youtube-viewer, torrents ...etc.** Share with me if you got some good ones =)

* tutorial video: [Link](https://www.youtube.com/watch?v=sYp2xfoq8Fs)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

### install requirements
    tmux surfraw w3m translate-shell

### configuration
    vim ~/.tmux.conf

    # tmux 2.4 or higher examples =====================
    bind-key -T copy-mode-vi 'o' send-keys -X copy-selection \; new-window -n google \; send-keys -t google 'sr google "$(tmux show-buffer)" && tmux kill-window' 'Enter'
    bind-key -T copy-mode-vi 'i' send-keys -X copy-selection \; new-window -n imagegoogle \; send-keys -t imagegoogle 'sr imagesgoogle "$(tmux show-buffer)" && tmux kill-window' 'Enter'
    bind-key -T copy-mode-vi 'p' send-keys -X copy-selection \; new-window -n wikipedia \; send-keys -t wikipedia 'sr wikipedia "$(tmux show-buffer)" && tmux kill-window' 'Enter'
    bind-key -T copy-mode-vi 'u' send-keys -X copy-selection \; new-window -n youtube \; send-keys -t youtube 'mpsyt /"$(tmux show-buffer)" && tmux kill-window' 'Enter'
    bind-key -T copy-mode-vi 'O' send-keys -X copy-selection \; new-window -n w3m \; send-keys -t w3m 'w3m "$(tmux show-buffer)" && tmux kill-window' 'Enter'
    
    # translate, dictionary, text to speech
    bind-key -T copy-mode-vi 't' send-keys -X copy-selection \; new-window -n translate \; send-keys -t translate 'translate-shell es "$(tmux show-buffer)" | w3m && tmux kill-window' 'Enter'
    bind-key -T copy-mode-vi 'd' send-keys -X copy-selection \; new-window -n dict \; send-keys -t dict 'translate-shell -d "$(tmux show-buffer)" | w3m && tmux kill-window' 'Enter'
    bind-key -T copy-mode-vi 's' send-keys -X copy-selection \; new-window -n speak \; send-keys -t speak 'translate-shell -brief "$(tmux show-buffer)" -play && tmux kill-window' 'Enter'





    # tmux 2.3 or lower examples ===================
    bind-key -t vi-copy s copy-selection \; new-window -n gsearch \; send-keys -t gsearch 'sr google "$(tmux show-buffer)" && tmux kill-window' 'Enter'
    
    bind-key -t vi-copy o copy-selection \; new-window -n google \; send-keys -t google 'sr -browser=elinks google "$(tmux show-buffer)" && tmux kill-window' 'Enter'
    bind-key -t vi-copy i copy-selection \; new-window -n imagegoogle \; send-keys -t imagegoogle 'sr imagesgoogle "$(tmux show-buffer)" && tmux kill-window' 'Enter'
    bind-key -t vi-copy p copy-selection \; new-window -n wikipedia \; send-keys -t wikipedia 'sr wikipedia "$(tmux show-buffer)" && tmux kill-window' 'Enter'
    bind-key -t vi-copy t copy-selection \; new-window -n translate \; send-keys -t translate 'translate-shell es "$(tmux show-buffer)" | w3m && tmux kill-window' 'Enter'
    bind-key -t vi-copy d copy-selection \; new-window -n dict \; send-keys -t dict 'translate-shell -d "$(tmux show-buffer)" | w3m && tmux kill-window' 'Enter'
    bind-key -t vi-copy s copy-selection \; new-window -n speak \; send-keys -t speak 'translate-shell -brief "$(tmux show-buffer)" -play && tmux kill-window' 'Enter'



### Usage
Enter into copy mode **Prefix + ]**, then highlight the text you want, then hit the hotkey you binded in our configurations above

### references
- https://www.youtube.com/watch?v=sYp2xfoq8Fs
- [How To Use Surfraw](https://www.youtube.com/playlist?list=PLqv94xWU9zZ2e-lDbmBpdASA6A6JF4Nyz)
- [How To Use W3M CLI Web Browser](https://www.youtube.com/playlist?list=PLqv94xWU9zZ35Yv0s6zMID5JoS8qu19Kh)
- [How To Use Tmux](https://www.youtube.com/playlist?list=PL5BE1545D8486D66D)

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


