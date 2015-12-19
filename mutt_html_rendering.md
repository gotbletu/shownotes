# Mutt HTML Rendering for CLI and GUI
Preview and Render HTML emails, both in commandline or in a GUI web browser
* tutorial video: [Link](https://www.youtube.com/watch?v=Tt-EQxj5k_U)
* offical website: [Link](http://www.mutt.org/)

### install requirements
    mutt


### muttrc
    vim ~/.muttrc
    
    # open in gui browser: hit "v" then go down to text/html then hit "m"
    bind attach <return> view-mailcap
    auto_view text/html                                      # view html automatically
    alternative_order text/plain text/enriched text/html     # list html for last


### mailcap
    vim ~/.mailcap

    # text/html; chromium %s &; test=test -n "$DISPLAY"; needsterminal;
    # text/html; w3m -I %{charset} -T text/html; copiousoutput;
    text/html; "$BROWSER" %s &; test=test -n "$DISPLAY"; needsterminal;
    text/html; "$BROWSERCLI" -I %{charset} -T text/html; copiousoutput;
    
### references
- http://jasonwryan.com/blog/2012/05/12/mutt/

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


