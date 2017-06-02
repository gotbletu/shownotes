# PlayOnLinux Fix Shortcuts
If you are moving or importing your playonlinux folder to a new computer or location, you might run into this issue of the shortcut not launching your games or programs. It is a simple fix using a single command.

* tutorial video: [Link](https://www.youtube.com/watch?v=GHlnCaeMFUk)
* offical website: [Link](https://www.playonlinux.com/en/)

### install requirements
    playonlinux

### commands
    # find your username
    whoami
    
    # old user
    look at a shortcut inside of ~/.PlayOnLinux/shortcuts to find out what the username was
    
    # change shortcut user path for all shortcut
    find ~/.PlayOnLinux/shortcuts -type f -exec sed -i 's:OLDUSER:NEWUSER:g' {} \;

### references
- https://www.youtube.com/watch?v=GHlnCaeMFUk
- PlayOnLinux / Wine Playlist: https://www.youtube.com/playlist?list=PL6F3AC35CE269F6F2

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


