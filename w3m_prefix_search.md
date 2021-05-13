# W3M Prefix Search Engines Searches Using FZF and Surfraw
improving w3m by having a quick way to search multiple search engines or even custom search engines via the power of surfraw elvi

* tutorial video: [Link](https://youtu.be/p5NZb8f8AHA) | update [Link](https://youtu.be/0j3pUfZjCeQ)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

tags: linux w3m omnibar address bar quick w3m smart search fzf fuzzy finder surfraw tmux workaround current url

### install requirements
    w3m surfraw fzf gawk coreutils grep (xsel or tmux)
    
### install scripts to root directory
Download at [root-cgi-bin](w3m_plugins/root-cgi-bin)
    
---- 
    # save it to 
    
    /usr/lib/w3m/cgi-bin/goto_clipboard_primary.cgi
    /usr/lib/w3m/cgi-bin/goto_clipboard.cgi
    /usr/lib/w3m/cgi-bin/goto_tmux_clipboard.cgi
---- 
    chmod +x <script.cgi>
    
### install script to local directory
Download at [cgi-bin](w3m_plugins/cgi-bin)
    
---- 
    # save it to 
    
    ~/.w3m/cgi-bin/fzf_surfraw.cgi
---- 
    chmod +x <script.cgi>

### configuration
    vim ~/.w3m/keymap
    
    # for x sessions
    keymap  xs      COMMAND "READ_SHELL ~/.w3m/cgi-bin/fzf_surfraw.cgi ; BACK ; GOTO /usr/lib/w3m/cgi-bin/goto_clipboard_primary.cgi ; REDRAW"
    keymap  XS      COMMAND "READ_SHELL ~/.w3m/cgi-bin/fzf_surfraw.cgi ; BACK ; TAB_GOTO /usr/lib/w3m/cgi-bin/goto_clipboard_primary.cgi ; REDRAW"
    
    # for tmux users
    # keymap  xs      COMMAND "READ_SHELL ~/.w3m/cgi-bin/fzf_surfraw.cgi ; BACK ; GOTO /usr/lib/w3m/cgi-bin/goto_tmux_clipboard.cgi ; REDRAW"
    # keymap  XS      COMMAND "READ_SHELL ~/.w3m/cgi-bin/fzf_surfraw.cgi; BACK ; TAB_GOTO /usr/lib/w3m/cgi-bin/goto_tmux_clipboard.cgi ; REDRAW"
    
    
### set the default open-url to current url
    sed -i 's:default_url.*:default_url 1:g' ~/.w3m/config

### usage example
    $ w3m google.com
    then press xs or XS to use surfraw for smart search

### references
- https://youtu.be/0j3pUfZjCeQ
- https://youtu.be/p5NZb8f8AHA
- https://github.com/felipesaa/A-vim-like-firefox-like-configuration-for-w3m
- [W3M Playlist](https://www.youtube.com/playlist?list=PLqv94xWU9zZ35Yv0s6zMID5JoS8qu19Kh)
- [Surfraw Playlist](https://www.youtube.com/playlist?list=PLqv94xWU9zZ2e-lDbmBpdASA6A6JF4Nyz)
- [FZF Playlist](https://www.youtube.com/playlist?list=PLqv94xWU9zZ2fMsMMDF4PjtNHCeBFbggD)

### contact

                 _   _     _      _
      __ _  ___ | |_| |__ | | ___| |_ _   _
     / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
    | (_| | (_) | |_| |_) | |  __/ |_| |_| |
     \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
     |___/

- https://www.youtube.com/user/gotbletu
- https://lbry.tv/@gotbletu
- https://twitter.com/gotbletu
- https://github.com/gotbletu
