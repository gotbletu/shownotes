# Nap - Console Linux Napster Client
Nap is a console napster client written by Kevin Sullivan. It runs on Linux, OpenBSD, and other systems. Current releases of nap, such as 1.5.4, are very stable. They can run for weeks at a time without crashing or user intervention.
* tutorial video: [Link](https://www.youtube.com/watch?v=UxYmZIGy3Qc)
* offical website: [Link](http://nap.sourceforge.net/)

### install requirements
    nap

### configuration
    vim ~/.nap/napconf
    
    servers=share-it.loginto.me:3456;108.19.45.179:7777;95.248.174.8:8888;108.19.45.179:8888;spica.sytes.net:8888;84.24.69.59:6436;98.202.75.0:8877;79.103.115.248:5995;82.53.30.153:3456;80.181.212.54:8888

http://gotnap.com/index.php/list

### connect to a server
    nap -r -s ipaddress:port
    nap -r -s 79.103.107.173:5995 -s 98.202.75.0:8877
    
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
- http://nap.sourceforge.net/userguide.html#4.
- http://gotnap.com/index.php/list


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


