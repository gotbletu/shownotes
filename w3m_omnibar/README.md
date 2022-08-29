# W3M Omnibar
access search engine directly from the addressbar

* tutorial video: [Link](https://youtu.be/77qhjaoj_2k)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

tags: w3m omnibar omnibox search engine keywords searching commandline linux terminal internet web browser retro computer

### requirements
    
    put cgi scripts in ~/.w3m/cgi-bin/

### configuration

    chmod +x ~/.w3m/cgi-bin/*.cgi
    sed -i 's@^cgi_bin.*@cgi_bin ~/.w3m/cgi-bin:/usr/lib/w3m/cgi-bin:/usr/local/libexec/w3m/cgi-bin@g' ~/.w3m/config
    sed -i 's@^use_dictcommand.*@use_dictcommand 1@g' ~/.w3m/config
    
    $EDITOR ~/.w3m/keymap
    
    # Dictionary Lookup {{{
    ############################ Execute dictionary command (see README.dict) (DICT_WORD)
    keymap  \\\d    COMMAND "SET_OPTION dictcommand=file:///cgi-bin/dictionary.cgi ; DICT_WORD"
    ############################ Execute dictionary command for word at cursor (DICT_WORD_AT)
    keymap  \\\w    COMMAND "SET_OPTION dictcommand=file:///cgi-bin/dictionary.cgi ; DICT_WORD_AT"
    ############################ Execute omnibar command (DICT_WORD)
    # }}}
    
    ############################ Omnibar search engines {{{
    # user input keywords to search
    keymap  s1      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_1337x.cgi ; DICT_WORD"
    keymap  sa      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_aspell.cgi ; DICT_WORD"
    keymap  sb      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_bing.cgi ; DICT_WORD"
    keymap  sd      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_duckduckgo.cgi ; DICT_WORD"
    keymap  sg      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_google.cgi ; DICT_WORD"
    keymap  si      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_geminispace.cgi ; DICT_WORD"
    keymap  sn      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_nyaasi.cgi ; DICT_WORD"
    keymap  sp      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_piratebay.cgi ; DICT_WORD"
    keymap  sr      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_subreddit.cgi ; DICT_WORD"
    keymap  st      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_twitch.cgi ; DICT_WORD"
    keymap  su      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_yewtube.cgi ; DICT_WORD"
    keymap  sv      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_veronica2.cgi ; DICT_WORD"
    keymap  sw      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_wikipedia.cgi ; DICT_WORD"
    keymap  sx      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_xdcceu.cgi ; DICT_WORD"
    keymap  sy      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_yahoo.cgi ; DICT_WORD"
    # search current word under cursor
    keymap  s2      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_1337x.cgi ; DICT_WORD_AT"
    keymap  sA      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_aspell.cgi ; DICT_WORD_AT"
    keymap  sB      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_bing.cgi ; DICT_WORD_AT"
    keymap  sD      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_duckduckgo.cgi ; DICT_WORD_AT"
    keymap  sG      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_google.cgi ; DICT_WORD_AT"
    keymap  sI      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_geminispace.cgi ; DICT_WORD_AT"
    keymap  sN      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_nyaasi.cgi ; DICT_WORD_AT"
    keymap  sP      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_piratebay.cgi ; DICT_WORD_AT"
    keymap  sR      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_subreddit.cgi ; DICT_WORD_AT"
    keymap  sU      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_yewtube.cgi ; DICT_WORD_AT"
    keymap  sV      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_veronica2.cgi ; DICT_WORD_AT"
    keymap  sW      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_wikipedia.cgi ; DICT_WORD_AT"
    keymap  sX      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_xdcceu.cgi ; DICT_WORD_AT"
    keymap  sY      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_yahoo.cgi ; DICT_WORD_AT"
    keymap  sT      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_twitch.cgi ; DICT_WORD_AT"
    # }}}
    
### references
- https://youtu.be/77qhjaoj_2k
- [W3M Playlist](https://www.youtube.com/playlist?list=PLqv94xWU9zZ35Yv0s6zMID5JoS8qu19Kh)



