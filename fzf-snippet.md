Notes for video: https://www.youtube.com/watch?v=Zew0mgJwAh8


## 1. requirements (depends on what u using)
* fzf (https://github.com/junegunn/fzf)
* bash
* zsh
* tmux
* xclip

## 2. create folder
    mkdir ~/.multisnippet
    
## 3. alias for zshrc/bashrc

    # edit single line snippet
    cfg-snippetrc() { $EDITOR ~/.snippetrc ;}
    
    # edit multiline snippet
    cfg-multisnippetrc() { $EDITOR ~/.multisnippet/"$(ls ~/.multisnippet | fzf -e -i)" ;}
    
    #create new multiline snippet
    multisnippet() { $EDITOR ~/.multisnippet/"$1" ;}
    
    fzf-snippet() { 
    	selected="$(cat ~/.snippetrc | sed '/^$/d' | sort -n | fzf -e -i )"
    	# remove tags, leading and trailing spaces, also no newline
    	echo "$selected" | sed -e s/\;\;\.\*\$// | sed 's/^[ \t]*//;s/[ \t]*$//' | tr -d '\n' | xclip -selection clipboard
    }
    
    fzf-multisnippet() { 
    	# location of snippets
    	dir=~/.multisnippet
    
    	# merge filename and tags into single line
    	results=$(for FILE in $dir/*
    	do
    		getname=$(basename $FILE)
    		gettags=$(head -n 1 $FILE)
    
    		echo "$getname \t $gettags" 
    
    	done)
    
    	# copy content into clipboard without tags
    	filename=$(echo "$(echo $results | fzf -e -i )" | cut -d' ' -f 1)
    	sed 1d $dir/$filename | xclip -selection clipboard
    }


## 4. sample: nano ~/.snippetrc
### ( ;; is the delimiter for tags)
    http://i.imgur.com/CGQJxHi.jpg						;;adblocker thug complains website goes down image meme
    "Words fall from your mouth as shit from ass!" - Vettius		;;spartacus quote
    "You counsel to suck the cock that pisses on me!" - Batiatus		;;spartacus quote
    "What's the point of going out? We're just gonna wind up back here anyway." - Homer Simpson ;;simpsons qoutes cartoon stupid
    "Operator! Give me the number for 911!" - Homer Simpson			;;simpsons qoutes cartoon stupid
    
        
## 5. sample: nano ~/.multisnippet/FILENAME
### ( tags are store on the 1st line)

    tags go on this first line
    #             _   _     _      _         
    #  __ _  ___ | |_| |__ | | ___| |_ _   _ 
    # / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
    #| (_| | (_) | |_| |_) | |  __/ |_| |_| |
    # \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
    # |___/                                  
    #       http://www.youtube.com/user/gotbletu
    #       https://twitter.com/gotbletu
    #       https://www.facebook.com/gotbletu
    #       https://plus.google.com/+gotbletu
    #       https://github.com/gotbletu
    
## 6. nano ~/.tmux.conf
### (optional keybinding for tmux users)
#### i use  single and double qoute hotkey
    bind-key "'" new-window -n snippet \; send-keys "fzf-snippet && tmux kill-window\n"
    bind-key '"' new-window -n multisnippet \; send-keys "fzf-multisnippet && tmux kill-window\n"


## 7. related video
* fuzzy finder playlist
* https://www.youtube.com/playlist?list=PLqv94xWU9zZ2fMsMMDF4PjtNHCeBFbggD

