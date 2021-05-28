# W3M Prefix Search Engines Searches Using FZF and Surfraw
improving w3m by having a quick way to search multiple search engines or even custom search engines via the power of surfraw elvi

* tutorial video: [Link](https://youtu.be/p5NZb8f8AHA) | update [Link](https://youtu.be/0j3pUfZjCeQ)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

tags: linux w3m omnibar address bar quick w3m smart search fzf fuzzy finder surfraw tmux workaround current url

### install requirements
    w3m surfraw fzf gawk coreutils grep
    
### install script to local directory
[Download at cgi-bin](w3m_plugins/cgi-bin)
    
---- 
    
    ~/.w3m/cgi-bin/fzf_surfraw.cgi
    ~/.w3m/cgi-bin/goto_clipboard.cgi
    ~/.w3m/cgi-bin/goto_clipboard_primary.cgi
    ~/.w3m/cgi-bin/goto_tmux_clipboard.cgi
    ~/.w3m/cgi-bin/goto_w3m_clipboard.cgi
    
---- 
    chmod +x ~/.w3m/cgi-bin/*.cgi

### configuration
    vim ~/.w3m/keymap
    
    # search with surfraw (no clipboard required)
    keymap  xs      COMMAND "READ_SHELL ~/.w3m/cgi-bin/fzf_surfraw.cgi ; BACK ; GOTO file:/cgi-bin/goto_w3m_clipboard.cgi"
    keymap  XS      COMMAND "READ_SHELL ~/.w3m/cgi-bin/fzf_surfraw.cgi ; BACK ; TAB_GOTO file:/cgi-bin/goto_w3m_clipboard.cgi"
    
    # yank url to multiple clipboard
    keymap  yy      EXTERN_LINK "url=%s ; echo "$url" > /tmp/w3m_clipboard.txt ; echo "$url" | xsel -b ; echo "$url" | tmux load-buffer -"
    keymap  YY      EXTERN      "url=%s ; echo "$url" > /tmp/w3m_clipboard.txt ; echo "$url" | xsel -b ; echo "$url" | tmux load-buffer -"
    
    # paste url and go
    keymap  pp      GOTO        file:/cgi-bin/goto_clipboard.cgi
    keymap  PP      TAB_GOTO    file:/cgi-bin/goto_clipboard.cgi
    keymap  pt      GOTO        file:/cgi-bin/goto_tmux_clipboard.cgi
    keymap  PT      TAB_GOTO    file:/cgi-bin/goto_tmux_clipboard.cgi
    keymap  pw      GOTO        file:/cgi-bin/goto_w3m_clipboard.cgi
    keymap  PW      TAB_GOTO    file:/cgi-bin/goto_w3m_clipboard.cgi
    
### change config settings
    sed -i 's@cgi_bin.*@cgi_bin ~/.w3m/cgi-bin:/usr/lib/w3m/cgi-bin:/usr/local/libexec/w3m/cgi-bin@g' ~/.w3m/config
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
