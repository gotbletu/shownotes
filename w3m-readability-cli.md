# readability-cli with w3m web browser macro hotkey
Firefox Reader View in your terminal!
readability-cli (aka readable) takes any HTML page and strips out unnecessary bloat by using Mozilla's Readability library. As a result, you get a web page which contains only the core content and nothing more. The resulting HTML is suitable for terminal browsers, text readers, and other uses.

* tutorial video: [Link](https://youtu.be/_j-p0z2AQp4)

### install requirements
    w3m readability-cli
 

### configuration
    vim ~/.w3m/keymap
    
    keymap  L       NEXT
    keymap  H       PREV
    keymap  \\\r    COMMAND "READ_SHELL 'readable $W3M_URL -p html-title,html-content > /tmp/readable.html' ; LOAD /tmp/readable.html"
    

### usage
    press \r on a webpage while running w3m web browser

### references
- W3M playlist https://www.youtube.com/playlist?list=PLqv94xWU9zZ35Yv0s6zMID5JoS8qu19Kh
- https://gitlab.com/gardenappl/readability-cli
- https://www.npmjs.com/package/readability-cli
- https://youtu.be/_j-p0z2AQp4

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
- gotbletu@gmail.com


