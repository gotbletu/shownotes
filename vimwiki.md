# Vimwiki using Markdown and Preview
Taking notes with the best text editor! =)
* tutorial video: [Link](https://www.youtube.com/watch?v=ONh95PNBW-Q)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

### install requirements
- vim
- vimwiki (https://github.com/vimwiki/vimwiki)
- vim-instant-markdown (https://github.com/suan/vim-instant-markdown)

### configuration
    vim ~/.vimrc
    

    " vimwiki - Personal Wiki for Vim
    " https://github.com/vimwiki/vimwiki
    set nocompatible
    filetype plugin on
    syntax on
    " vimwiki with markdown support
    let g:vimwiki_ext2syntax = {'.md': 'markdown', '.markdown': 'markdown', '.mdown': 'markdown'}
    " helppage -> :h vimwiki-syntax 
    
    " vim-instant-markdown - Instant Markdown previews from Vim
    " https://github.com/suan/vim-instant-markdown
    let g:instant_markdown_autostart = 0	" disable autostart
    map <leader>md :InstantMarkdownPreview<CR>
    
### usage
    vim index.md
    
    # hotkeys
    Enter - create a new note (cusor must be on a word)
    Enter - enter into the note
    Backspace - Go back
    <leader>md - Open Markdown preview on web browser

### markdown
As far as markdown syntax you can learn that on your own, takes about 5-10mins really, just google it

### references
- https://github.com/vimwiki/vimwiki
- https://github.com/suan/vim-instant-markdown


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
