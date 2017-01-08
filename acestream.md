# acestream-launcher: watch streaming video channels
Ace Stream is an innovative multimedia platform of a new generation, which includes different products and solutions for ordinary Internet users as well as for professional members of the multimedia market.
Note: Ace Stream uses in its core, P2P (peer-to-peer) technology, BitTorrent protocol, which is acknowledged as the most effective protocol to transfer/deliver «heavy content».
Ace Stream is more than just BitTorrent client for file exchange via P2P-networks!
* tutorial video: [Link](https://www.youtube.com/watch?v=dxar7KLsrg8)
* offical website: [Link](https://github.com/jonian/acestream-launcher)

### install requirements
    acestream-launcher
    acestream-engine
    vlc

### configuration
    vim ~/.zshrc or ~/.bashrc

    #-------- Acestream CLI (Streaming P2P Videos) {{{
    #------------------------------------------------------
    # DEMO: https://www.youtube.com/watch?v=dxar7KLsrg8
    # DESC: view streaming videos using acestream live feeds
    # LINK: https://github.com/jonian/acestream-launcher
    # FEED: https://www.google.com/#q=acestream://&tbs=qdr:w
    #       http://www.acesoplisting.in/
    #       http://arenavision.in/
    #       http://streams.magazinmixt.ro/
    #       http://www.livefootballol.me/acestream-channel-list-2016-1.html
    
    acestream-cvlc() { acestream-launcher --player cvlc "$@" ;}
    acestream-mpv() { acestream-launcher --player mpv "$@" ;}
    acestream-mplayer() { acestream-launcher --player mplayer "$@" ;}
    
    # choose a player (default is cvlc)
    ACE_PLAYER=cvlc
    # ACE_PLAYER=mpv
    
    acc-bbcone-eng() { acestream-launcher --player "$ACE_PLAYER" acestream://964d4a6632bf9c8c088de94e12a4597b2173e291 ;}
    acc-tele5-spa() { acestream-launcher --player "$ACE_PLAYER" acestream://97f0eaa031804b7c9f5b7f60599047254d9128b1 ;}
    acc-espn-eng() { acestream-launcher --player "$ACE_PLAYER" acestream://5d25598468b68aabc1d908921cea98062c7f8739 ;}
    acc-espn-deportes-spa() { acestream-launcher --player "$ACE_PLAYER" acestream://0a0be3253e0374f5f6323391c62b244eed5673c6 ;}
    acc-beinsports-fr() { acestream-launcher --player "$ACE_PLAYER" acestream://b5950a56db8f722876dc74443d74b565fb99368f ;}
    acc-tennis() { acestream-launcher --player "$ACE_PLAYER" acestream://f3b9d8f1575cf21be3db910af0d4e1a3ae19f3e2 ;}
    
    # }}}

### references
- https://www.youtube.com/watch?v=dxar7KLsrg8
- http://info.acestream.org/#/about/acestream
- https://github.com/jonian/acestream-launcher
- https://www.google.com/#q=acestream://&tbs=qdr:w
- http://www.acesoplisting.in/
- http://arenavision.in/
- http://streams.magazinmixt.ro/
- http://www.livefootballol.me/acestream-channel-list-2016-1.html


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


