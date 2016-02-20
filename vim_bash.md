# Using Bash Commands in Vim
Pipe results to vim, bind custom hotkey to execute bash shell commands.
Enjoy the power of mixing different commandline tools together.

* tutorial video: [Link](https://www.youtube.com/watch?v=YIP36MT4go0)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

### examples used
    locate -ir Naruto | vim -R -
    ls | vim -R -

### hotkeys to know
    ZQ    to exit vim quickly without saving (or use ZZ)
    \     default leader key

### configuration
    vim ~/.vimrc
    
    " open parent directory of a file
    " nohup xdg-open "$(echo $1 | rev | cut -d\/ -f2- | rev )" >/dev/null 2>&1&
    map <leader>d :exec '!nohup xdg-open "$(echo ' . shellescape(getline('.'), 1) . ' \| rev \| cut -d\/ -f2- \| rev )" >/dev/null 2>&1&' <CR><CR>
    
    " nohup xdg-open $1 >/dev/null 2>&1&'
    map <leader>o :exec '!nohup xdg-open ' . shellescape(getline('.'), 1) . ' >/dev/null 2>&1&'<CR><CR>
    
    map <leader>f :exec '!nohup feh ' . shellescape(getline('.'), 1) . ' >/dev/null 2>&1&'<CR><CR>
    map <leader>mp :exec '!nohup mplayer ' . shellescape(getline('.'), 1) . ' >/dev/null 2>&1&'<CR><CR>
    map <leader>mm :exec '!mplayer ' . shellescape(getline('.'), 1) <CR><CR>
    
    " stream justin tv ..etc
    map <leader>li :exec '!livestreamer -p mplayer ' . shellescape(getline('.'), 1) . 'best' <CR><CR>
    
    " watch streaming porn
    map <leader>p :exec '!mplayer $(youtube-dl -g ' . shellescape(getline('.'), 1) . ')' <CR><CR>
    
    " download videos/files
    map <leader>yt :exec '!cd ~/Downloads; youtube-dl ' . shellescape(getline('.'), 1) <CR><CR>
    map <leader>wg :exec '!cd ~/Downloads; wget -N -c ' . shellescape(getline('.'), 1) <CR><CR>

### references
http://vimhelp.appspot.com/eval.txt.html#shellescape%28%29


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


