Notes for video: https://www.youtube.com/watch?v=Dmbh4r2mmDs


## 1. requirements (depends on what u using)
* fzf (https://github.com/junegunn/fzf)
* bash
* zsh
* tmux
* surfraw

## 2. for ~/.zshrc or ~/.bashrc
    fzf-surfraw() { surfraw "$(cat ~/.config/surfraw/bookmarks | sed '/^$/d' | sort -n | fzf -e)" }

## 3. for ~/.tmux.conf
    bind-key -n 'C-\' new-window -n bookmarks -c $HOME \; \
        send-keys 'fzf-surfraw && tmux kill-window' 'Enter'

## 4. related video
* surfraw playlist
* https://www.youtube.com/playlist?list=PLqv94xWU9zZ2e-lDbmBpdASA6A6JF4Nyz
* fuzzy finder playlist
* https://www.youtube.com/playlist?list=PLqv94xWU9zZ2fMsMMDF4PjtNHCeBFbggD

