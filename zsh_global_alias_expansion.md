# ZSH Global Alias Expansion
Allows you to expand your global alias code in the terminal

* tutorial video: [Link](https://www.youtube.com/watch?v=WTTIGjZAMGg)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

### install requirements
    zsh

### configuration
    vim ~/.zshrc

    #-------- Global Alias {{{
    #------------------------------------------------------
    # Automatically Expanding Global Aliases (Space key to expand)
    # references: http://blog.patshead.com/2012/11/automatically-expaning-zsh-global-aliases---simplified.html 
    globalias() {
      if [[ $LBUFFER =~ '[A-Z0-9]+$' ]]; then
        zle _expand_alias
        zle expand-word
      fi
      zle self-insert
    }
    zle -N globalias
    bindkey " " globalias                 # space key to expand globalalias
    # bindkey "^ " magic-space            # control-space to bypass completion
    bindkey "^[[Z" magic-space            # shift-tab to bypass completion
    bindkey -M isearch " " magic-space    # normal space during searches
    
    
    # http://www.zzapper.co.uk/zshtips.html
    alias -g ND='*(/om[1])' 	      # newest directory
    alias -g NF='*(.om[1])' 	      # newest file
    #alias -g NE='2>|/dev/null'
    alias -g NO='&>|/dev/null'
    alias -g P='2>&1 | $PAGER'
    alias -g VV='| vim -R -'
    alias -g L='| less'
    alias -g M='| most'
    alias -g C='| wc -l'
    alias -g H='| head'
    alias -g T='| tail'
    alias -g G='| grep'
    alias -g LL="2>&1 | less"
    alias -g CA="2>&1 | cat -A"
    alias -g NE="2> /dev/null"
    alias -g NUL="> /dev/null 2>&1"
    
    #}}}


### reload zsh

    source ~/.zshrc

### references
- https://www.youtube.com/watch?v=WTTIGjZAMGg
- http://blog.patshead.com/2012/11/automatically-expaning-zsh-global-aliases---simplified.html
- http://www.zzapper.co.uk/zshtips.html

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


