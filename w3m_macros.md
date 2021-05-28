# W3M Macros - Automate Task
Using macros automate toggling settings like images display or table borders on or off quickly. Smart search similar feature using macros as well for different search engines

* tutorial video: [Link](https://youtu.be/lL73xWsaJP8)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

### install requirements
    w3m

### configuration
    $EDITOR ~/.w3m/keymap

    # for more help on options
    # $ w3m -show-option
    
    # leader key = \
    keymap  \\\?    COMMAND       "HELP; SEARCH ^User-Defined; CENTER_V"            # show user custom hotkeys binding
    keymap  \\\f    COMMAND       "HELP; SEARCH ^Input Line Editing Mode; CENTER_V" # show field hotkeys binding
    keymap  \\\c    COMMAND       "SET_OPTION color=toggle ; RESHAPE"
    keymap  \\\u    COMMAND       "SET_OPTION mark_all_pages=toggle ; RELOAD"      # Treat URL-like strings as links in all pages (convert text to url)
    keymap  \\\l    COMMAND       "SET_OPTION display_link_number=toggle ; SET_OPTION show_lnum=toggle ; RESHAPE" # toggle hinting mode / line numbers
    keymap  \\\h    COMMAND       "SET_OPTION display_link_number=toggle ; RESHAPE" # toggle hinting mode
    keymap  \\\n    COMMAND       "SET_OPTION show_lnum=toggle ; RESHAPE"           # toggle line numbers
    keymap  \\\b    COMMAND       "SET_OPTION display_borders=toggle ; RESHAPE"
    keymap  \\\i    COMMAND       "SET_OPTION display_image=toggle ; RELOAD"
    keymap  \\\e    COMMAND       "SET_OPTION user_agent='' ; RELOAD"               # empty user agent
    keymap  \\\A    COMMAND       "SET_OPTION user_agent='Opera/9.80 (S60; SymbOS; Opera Mobi/SYB-1107071606; U; en) Presto/2.8.149 Version/11.10' ; RELOAD"
    keymap  C-t     COMMAND       "TAB_GOTO https://duckduckgo.com/lite/; NEXT_LINK; GOTO_LINK"
    keymap  t       COMMAND       "TAB_GOTO https://duckduckgo.com/lite/; NEXT_LINK; GOTO_LINK"
    keymap  sg      COMMAND       "TAB_GOTO https://google.com; GOTO_LINE 6; NEXT_LINK; GOTO_LINK"
    keymap  sx      COMMAND       "TAB_GOTO https://stackexchange.com; GOTO_LINE 7; NEXT_LINK; GOTO_LINK"
    keymap  \\\m    COMMAND       "SHELL 'man w3m'"

### references
- https://youtu.be/lL73xWsaJP8
- https://github.com/felipesaa/A-vim-like-firefox-like-configuration-for-w3m/blob/master/documentation/functions.txt
- https://vitalyparnas.com/posts/2018/08/on-w3m/ 
- https://vitalyparnas.com/posts/2019/07/w3m-redux/
- https://vitalyparnas.com/guides/w3m/
- https://developers.whatismybrowser.com/useragents/explore/
- [W3M Playlist](https://www.youtube.com/playlist?list=PLqv94xWU9zZ35Yv0s6zMID5JoS8qu19Kh)

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
