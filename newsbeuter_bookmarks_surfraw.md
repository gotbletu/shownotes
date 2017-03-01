# Newsbeuter save Bookmarks to Surfraw
* tutorial video: [Link](https://www.youtube.com/watch?v=rHVfgGTTtNQ)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

### install requirements
    newsbeuter surfraw

### configuration
    vim ~/.newsbeuter/config
    
    # references: https://newsbeuter.wordpress.com/2007/08/27/bookmarking/
    bookmark-cmd "~/.scripts/newsbeuter_bookmarks_surfraw.sh"
    
### script
- You can wget the script here: [newsbeuter_bookmarks_surfraw.sh](newsbeuter_bookmarks_surfraw.sh)
- or manually save below




    #!/bin/sh
    #             _   _     _      _         
    #  __ _  ___ | |_| |__ | | ___| |_ _   _ 
    # / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
    #| (_| | (_) | |_| |_) | |  __/ |_| |_| |
    # \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
    # |___/                                  
    #       https://www.youtube.com/user/gotbletu
    #       https://twitter.com/gotbletu
    #       https://plus.google.com/+gotbletu
    #       https://github.com/gotbletu
    #       gotbleu@gmail.com
    
    # info: newsbeuter script to save bookmarks directly to surfraw
    # demo video: https://www.youtube.com/watch?v=rHVfgGTTtNQ
    # references: https://newsbeuter.wordpress.com/2007/08/27/bookmarking/
    # config: 
    #   vim ~/.newsbeuter/config
    #     bookmark-cmd "~/.scripts/newsbeuter_bookmarks_surfraw.sh"
    # hotkey:
    #   Ctrl+B to bookmark an article url
    #   Ctrl+G to cancel
    
    url="$1"            # url
    title="$2"          # tags
    description="$3"    # nickname (single word only, no spaces)
    echo -e "${description}\t${url}\t;; newsbeuter ${title}" >> ~/.config/surfraw/bookmarks


### launch bookmarks (fzf + surfraw)
Note: This was not cover in the video since it was already explained in this old video below

https://www.youtube.com/watch?v=Dmbh4r2mmDs

### references
- https://www.youtube.com/watch?v=rHVfgGTTtNQ
- fzf bookmark launcher: https://www.youtube.com/watch?v=Dmbh4r2mmDs&list=PLqv94xWU9zZ2fMsMMDF4PjtNHCeBFbggD&index=3
- https://newsbeuter.wordpress.com/2007/08/27/bookmarking/
- Newsbeuter playlist: https://www.youtube.com/playlist?list=PLqv94xWU9zZ30jHFe8pqC5qES6ya6v2sE

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


