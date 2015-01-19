Notes for video: https://www.youtube.com/watch?v=AbveiTAymy0


## 1. requirements (depends on what u using)
* fzf (https://github.com/junegunn/fzf)
* bash
* zsh
* tmux

## 2. for ~/.zshrc or ~/.bashrc
    fzf-locate() { xdg-open "$(locate "*" | fzf -e)" ;}
    fzf-playonlinux() { playonlinux --run '$(ls ~/.PlayOnLinux/shortcuts | fzf -e)' ;}

## 3. for ~/.tmux.conf
    bind-key -n 'C-]' new-window -n playonlinux \; send-keys "fzf-playonlinux && tmux kill-window\n"
    bind-key -n 'M-\' new-window -n locate \; send-keys "fzf-locate && tmux kill-window\n"

## 4. related video
* fuzzy finder playlist
* https://www.youtube.com/playlist?list=PLqv94xWU9zZ2fMsMMDF4PjtNHCeBFbggD



