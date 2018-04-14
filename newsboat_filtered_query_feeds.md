# Newsboat Filtered Query Feeds
Filtering out junk and get to the articles we want to see in our rss reader.

* tutorial video: [Link](https://www.youtube.com/watch?v=PUxPUdyCy_U)
* offical website: [Link](https://newsboat.org/)

### install requirements
    newsboat

### configuration
    vim ~/.newsboat/urls
    
    
    # -------- Filter Feeds {{{
    # ------------------------------------------------------
    # https://newsboat.org/releases/2.11.1/docs/newsboat.html#_filter_language
    
    https://thepiratebay.org/rss//top100/0 "BTRSS"
    https://www.torrentdownload.ch/feed_latest "BTRSS"
    
    "query:Only 720p:tags =~ \"BTRSS\" and ( title =~ \"720p\" )" "BTRSS"
    "query:Only 1080p:tags =~ \"BTRSS\" and ( title =~ \"1080p\" )" "BTRSS"
    "query:Only SD:tags =~ \"BTRSS\" and ( title =~ \"hdtv|x264|web\" )" "BTRSS"
    
    # }}}

### references
- https://newsboat.org/releases/2.11.1/docs/newsboat.html#_filter_language
- https://www.youtube.com/watch?v=PUxPUdyCy_U

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


