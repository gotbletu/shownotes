# python-readability-lxml with w3m web browser
Given a html document, it pulls out the main body text and cleans it up.

* tutorial video: [Link](https://youtu.be/qPiE1JUgsBg)

### install requirements
    pip install readability-lxml

### basic commandline usage
    python3 -m readability.readability -h
    python3 -m readability.readability -u 'https://www.servethehome.com/amd-psb-vendor-locks-epyc-cpus-for-enhanced-security-at-a-cost/' > output.html
 
### configuration
    vim ~/.w3m/keymap
    
    keymap  L       NEXT
    keymap  H       PREV
    keymap  \\\r    COMMAND "READ_SHELL 'python3 -m readability.readability -u $W3M_URL 2> /dev/null 1> /tmp/readability.html' ; LOAD /tmp/readability.html"
    

### usage
    press \r on a webpage while running w3m web browser

### references
- W3M playlist https://www.youtube.com/playlist?list=PLqv94xWU9zZ35Yv0s6zMID5JoS8qu19Kh
- https://pypi.org/project/readability-lxml/ 
- https://aur.archlinux.org/packages/python-readability-lxml/
- https://youtu.be/qPiE1JUgsBg

### contact

                 _   _     _      _         
      __ _  ___ | |_| |__ | | ___| |_ _   _ 
     / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
    | (_| | (_) | |_| |_) | |  __/ |_| |_| |
     \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
     |___/                                  

- http://www.youtube.com/user/gotbletu
- https://lbry.tv/@gotbletu
- https://twitter.com/gotbletu
- https://github.com/gotbletu
- [submitted by proteusx](https://www.youtube.com/channel/UCaCROa2gD0qyMj0qbXRxw2Q)
- gotbletu@gmail.com


