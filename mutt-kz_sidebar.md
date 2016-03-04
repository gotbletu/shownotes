# Mutt Sidebar
Mutt email client with sidebar

* tutorial video: [Link](https://www.youtube.com/watch?v=C35NRp42bEQ)
* offical website: [Link](https://github.com/karelzak/mutt-kz)

### install requirements
    mutt-kz (any other mutt sidebar patch)

### configuration
    vim ~/.muttrc
    
    # requires sidebar patch for mutt
    mailboxes "+-- My mailbox -----------"
    set sidebar_visible = yes
    set sidebar_width = 25
    set sort_sidebar = desc
    set sidebar_delim = '|'
    color sidebar_new yellow default
    
    bind index,pager \CP sidebar-prev
    bind index,pager \CN sidebar-next
    bind index,pager \CO sidebar-open
    bind index,pager \CU sidebar-scroll-up
    bind index,pager \CD sidebar-scroll-down
    
    # macro index,pager b '<enter-command>toggle sidebar_visible<enter>'
    macro index b '<enter-command>toggle sidebar_visible<enter><refresh>'
    macro pager b '<enter-command>toggle sidebar_visible<enter><redraw-screen>'
    
    
    # always show X number of mails in the index
    set pager_index_lines = 6

### references
- http://baptiste-wicht.com/posts/2014/07/a-mutt-journey-my-mutt-configuration.html
- https://upsilon.cc/~zack/blog/posts/2008/01/mutt_patched_key_bindings/
- http://www.vigasdeep.com/install-config-mutt-sidebar/
- https://wiki.archlinux.org/index.php/Mutt#Mutt-Sidebar
    


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


