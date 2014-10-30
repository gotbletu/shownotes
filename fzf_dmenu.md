Notes for video: https://www.youtube.com/watch?v=9qkK3RmPSS4


## 1. requirements (depends on what u using)
fzf (https://github.com/junegunn/fzf)
bash
zsh
tmux

## 2. for ~/.zshrc
    fzf-dmenu() { 
    	# note: xdg-open has a bug with .desktop files, so we cant use that shit
    	selected="$(ls /usr/share/applications | fzf -e)"
    	nohup `grep '^Exec' "/usr/share/applications/$selected" | tail -1 | sed 's/^Exec=//' | sed 's/%.//'` >/dev/null 2>&1&
    }

    # hotkey to run the function (Ctrl+O)
    bindkey -s '^O' "fzf-dmenu\n"

## 3. for ~/.bashrc
    fzf-dmenu() { 
    	# note: xdg-open has a bug with .desktop files, so we cant use that shit
    	selected="$(ls /usr/share/applications | fzf -e)"
    	nohup `grep '^Exec' "/usr/share/applications/$selected" | tail -1 | sed 's/^Exec=//' | sed 's/%.//'` >/dev/null 2>&1&
    }

    # hotkey to run the function (Ctrl+O)
    bind '"\C-O":"fzf-dmenu\n"'

## 4. for ~/.tmux.conf
    bind-key -n C-Space new-window -n fzf-dmenu -c $HOME \; \
    	send-keys 'fzf-dmenu && sleep 1 && tmux kill-window' 'Enter'

## 5. related video
https://www.youtube.com/watch?v=hO8vd1y0h6g
