# Nap - Console Linux Napster Client
Nap is a console napster client written by Kevin Sullivan. It runs on Linux, OpenBSD, and other systems. Current releases of nap, such as 1.5.4, are very stable. They can run for weeks at a time without crashing or user intervention.
* tutorial video: [Link](https://www.youtube.com/watch?v=UxYmZIGy3Qc)
* offical website: [Link](http://nap.sourceforge.net/)

### install requirements
    nap

### how to compile manually and installing
    wget http://nap.sourceforge.net/dist/nap-1.5.4.tar.gz
    tar xvzf nap-1.5.4.tar.gz
    cd nap-1.5.4/
    ./configure
    make -j
    sudo cp ./src/nap /usr/local/bin/
    sudo cp ./src/napping /usr/local/bin/
    sudo chmod +x /usr/local/bin/nap
    sudo chmod +x /usr/local/bin/napping
    sudo chmod u+s /usr/local/bin/napping
    
### configuration
    vim ~/.nap/napconf
    
    servers=sanctuary.darkservers.net:3456;johnson1.linkpc.net:5995:z3n.overflow.biz:8888:share-it.loginto.me:3456

- https://web.archive.org/web/*/http://gotnap.com/index.php/list


### connect to a server
    nap -r -s ipaddress:port
    nap -r -s sanctuary.darkservers.net:3456 -s johnson1.linkpc.net:5995
    
### commands
    /help
    /search [keyword]
    /results          # open results window
    /dlul             # open download/upload window
    /quit             # quit program
    /quit yes         # force quit
    /tquit            # quit after transfer is done, no new upload will be accepted
    /unquit           # undo /tquit
    /browse username  # browse a users share files
    /browse2 username # browse a users share files without napster server
    
### hotkeys
    F1-F3             # switch different screens main, /results, /dlul
    Alt+1 - Alt+3     # switch different screens main, /results, /dlul
    Alt+up/Alt+down   # switch between download/uploads
    o                 # switch between download/uploads
    Ctrl+P/Ctrl+N     # scroll up/down
    PageUp/PageDown   # scroll up/down
    Ctrl+C Ctrl+C     # quit program quickly
    d                 # delete task
    r                 # retry failed task
    R                 # retry all failed task
    f                 # force download
    P                 # purge stopped task
    Tab               # [main window] autocomplete
    Tab               # [results/dlul window] toggle switch windows

### references
- http://nap.sourceforge.net/userguide.html
- [list of old opennap server list](https://web.archive.org/web/*/http://gotnap.com/index.php/list)

### Contact

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
- gotbletu@gmail.com


