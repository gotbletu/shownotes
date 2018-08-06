# Podqueue - Send URL To Podboat Queue
repurposing podboat as a TUI download manager instead of only handling podcast

* tutorial video: [Link](https://www.youtube.com/watch?v=1ylYBDfqyPY)
* offical website: [Link](https://newsboat.org/)

tags: linux, terminal, newsboat, podboat, newsbeuter, podbeuter, download manager, TUI, Text User Interface, Ncurses, commandline, CLI, rss feed reader, podcast catcher, downloader

### install requirements
    newsboat

### configuration
    $EDITOR ~/.newsboat/config
    
    #-------- podboat (podcast downloader) {{{
    #------------------------------------------------------
    download-path               "~/Downloads/%n"
    max-downloads               2
    player                      "xdg-open"
    # }}}

### function
    $EDITOR ~/.zshrc or $EDITOR ~/.bashrc


    podqueue() {
      if [ $# -lt 1 ]; then
        echo -e "Add Links To Podboat, Use Podboat As A TUI Download Manager"
        echo -e "\nUsage: $0 <url>"
        echo -e "\nExample:\n$0 http://abcxyz.com/filename.mp3"
        return 1
      fi
    
      URL="$1"
      SAVE_PATH=~/Downloads
      GET_FILENAME="$(echo "$1" | rev | cut -d\/ -f1 | rev | sed -e 's@\%20@\_@g' )"
    
      echo "$URL" "$SAVE_PATH/$GET_FILENAME" >> ~/.newsboat/queue
    }


### standalone script

    wget https://raw.githubusercontent.com/gotbletu/shownotes/master/podqueue.sh
    chmod +x podqueue.sh

### using with w3m web browser
----
    $EDITOR ~/.w3m/config
    
    extbrowser6 /path/to/script/podqueue.sh
----

How to use custom scripts with w3m: https://www.youtube.com/watch?v=YzgCgarUa_M

### references
- https://www.youtube.com/watch?v=1ylYBDfqyPY
- [How to use custom scripts with w3m](https://www.youtube.com/watch?v=YzgCgarUa_M)
- [podbeuter - podcast downloader](https://www.youtube.com/watch?v=5wyefy3GuDg)
- https://newsboat.org/

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


