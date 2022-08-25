# W3M Links Hint Mode (Similar to Vimium)
using w3m hint mode like vimium to jump to links quicker

* tutorial video: [Link](https://youtu.be/-bK5rTFM9B4)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

tags: w3m links hinting hint mode commandline linux terminal internet web browser retro computer

### configuration
    $EDITOR ~/.w3m/keymap

    #### toggle hinting mode (vimium similar)
    keymap  f-SPC   COMMAND "SET_OPTION display_link_number=toggle ; RESHAPE"
    #### jump to link number (e.g press 3ff) and hide hinting mode (similar to gg in vim)
    keymap  ff      COMMAND "SET_OPTION display_link_number=0 ; RESHAPE ; LINK_BEGIN"
    #### open current cursor link in new tab and hide hinting mode
    keymap  ft      COMMAND "SET_OPTION display_link_number=0 ; RESHAPE ; TAB_LINK"
    #### copy link to clipboard (e.g press f-SPC then 4fy to yank url)
    keymap  fy      COMMAND "SET_OPTION display_link_number=toggle ; RESHAPE ; LINK_BEGIN ; EXTERN_LINK 'url=%s ; printf "%b" "$url" > /tmp/clipbrd.txt ; printf "%b" "$url" | xsel -b 2>/dev/null ; printf "%b" "$url" | tmux load-buffer - ; printf '%s' "$url" | wl-copy 2>/dev/null  ; printf '%s' "$url" | clip 2>/dev/null ; printf '%s' "$url" > /dev/clipboard 2>/dev/null ; printf '%s' "$url" | pbcopy 2>/dev/null ; printf '%s' "$url" | termux-clipboard-set 2>/dev/null'"
    #### jump to link number and open it
    keymap  fo       COMMAND "SET_OPTION display_link_number=0 ; RESHAPE ; LINK_BEGIN ; GOTO_LINK"
    #### jump to link number and open it in new tab
    keymap  fn       COMMAND "SET_OPTION display_link_number=0 ; RESHAPE ; LINK_BEGIN ; TAB_LINK"
    # yank url to multiple clipboard (under cursor)
    keymap  yy      EXTERN_LINK "url=%s ; printf "%b" "$url" > /tmp/clipbrd.txt ; printf "%b" "$url" | xsel -b 2>/dev/null ; printf "%b" "$url" | tmux load-buffer - ; printf '%s' "$url" | wl-copy 2>/dev/null  ; printf '%s' "$url" | clip 2>/dev/null ; printf '%s' "$url" > /dev/clipboard 2>/dev/null ; printf '%s' "$url" | pbcopy 2>/dev/null ; printf '%s' "$url" | termux-clipboard-set 2>/dev/null"
    # yank url to multiple clipboard (current page)
    keymap  YY      EXTERN "url=%s ; printf "%b" "$url" > /tmp/clipbrd.txt ; printf "%b" "$url" | xsel -b 2>/dev/null ; printf "%b" "$url" | tmux load-buffer - ; printf '%s' "$url" | wl-copy 2>/dev/null  ; printf '%s' "$url" | clip 2>/dev/null ; printf '%s' "$url" > /dev/clipboard 2>/dev/null ; printf '%s' "$url" | pbcopy 2>/dev/null ; printf '%s' "$url" | termux-clipboard-set 2>/dev/null"
        
### usage example
- 1. w3m http://68k.news/
- 2. press f-Space
- 3. press 15fo

### references
- https://youtu.be/-bK5rTFM9B4
- [W3M Playlist](https://www.youtube.com/playlist?list=PLqv94xWU9zZ35Yv0s6zMID5JoS8qu19Kh)

### contact

                 _   _     _      _
      __ _  ___ | |_| |__ | | ___| |_ _   _
     / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
    | (_| | (_) | |_| |_) | |  __/ |_| |_| |
     \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
     |___/

- https://www.youtube.com/user/gotbletu
- https://odysee.com/@gotbletu
- https://twitter.com/gotbletu
- https://github.com/gotbletu

