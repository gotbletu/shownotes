# Vim or Neovim as a Manpager Replacement
vim religion invades the manpages
* tutorial video: [Link](https://www.youtube.com/watch?v=YjYgAn5li4g)

### vim as manpager
    vim ~/.bashrc or ~/.zshrc
    export MANPAGER="/bin/sh -c \"col -b | vim --not-a-term -c 'set ft=man ts=8 nomod nolist noma' -\""
    
    # extra stuff in vimrc
    vim ~/.vimrc
    set cursorline                       " Highligt the cursor line
    set cursorcolumn                     " Highlight the column line
    set number                           " Show the line number

### neovim as manpager with table of contents
    nvim ~/.bashrc or ~/.zshrc
    export MANPAGER="nvim +set\ filetype=man -"
    
    if the above doesn't work try the following:
    export MANPAGER="nvim -c 'set ft=man' -"

    nvim ~/.config/fish/config.fish
    set MANPAGER "nvim -c 'set ft=man' -"

    The following code snippet does seem to disable the default keybinding gO to toggle the TOC: 
    nvim ~/.config/nvim/init.vim
    filetype plugin on
    syntax on
    
    " manpage with table of contents sidebar with neovim
    " https://asciinema.org/a/165076
    " add to shellrc: export MANPAGER="nvim +set\ filetype=man -"
    augroup manlaunchtoc
        autocmd!
        if has('nvim')
            autocmd FileType man
                \ call man#show_toc() |
                \ setlocal laststatus=0 nonumber norelativenumber |
                \ nnoremap <buffer> l <Enter> |
                \ wincmd H |
                \ vert resize 35 |
                \ wincmd p
        endif
    augroup end

### references
- https://www.youtube.com/watch?v=YjYgAn5li4g
- https://asciinema.org/a/165076
- http://vim.wikia.com/wiki/Using_vim_as_a_man-page_viewer_under_Unix
- https://zameermanji.com/blog/2012/12/30/using-vim-as-manpager/
- https://vi.stackexchange.com/questions/4682/how-can-i-suppress-the-reading-from-stdin-message-from-within-vim

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


