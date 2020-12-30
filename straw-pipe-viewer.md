# Pipe-Viewer & Straw-Viewer - Search Youtube via Terminal - Linux CLI
* tutorial video: [Link](https://youtu.be/I4tfHUmklWo)

### config for tmux
----
    vim ~/.tmux.conf
    
    bind-key -T copy-mode-vi 'u' send-keys -X copy-selection \; new-window -n youtube \; send-keys -t youtube 'pipe-viewer "$(tmux show-buffer)" && tmux kill-window' 'Enter'
    bind-key -T copy-mode-vi 'U' send-keys -X copy-selection \; new-window -n youtube \; send-keys -t youtube 'straw-viewer "$(tmux show-buffer)" && tmux kill-window' 'Enter'
----
    

### task-spooler configs for pipe-viewer
----
    vim ~/.config/pipe-viewer/pipe-viewer.conf
    
    video_player_selected => "tsp",
    video_players         => {
                               tsp => {
                                        arg => "--ontop --no-border --force-window --autofit=500x280 --geometry=-15-53 --really-quiet --force-media-title=*TITLE* --no-ytdl *VIDEO*",
                                        audio => "--audio-file=*AUDIO*",
                                        cmd => "tsp mpv",
                                        fs => "--fullscreen",
                                        novideo => "--no-video",
                                        srt => "--sub-file=*SUB*",
                                      },
    
----
### task-spooler configs for straw-viewer
----
    vim ~/.config/straw-viewer/straw-viewer.conf
  
    video_player_selected => "tsp",
    video_players         => {
                               tsp => {
                                        arg => "--ontop --no-border --force-window --autofit=500x280 --geometry=-15-53 --really-quiet --title=*TITLE* --no-ytdl",
                                        audio => "--audio-file=*AUDIO*",
                                        cmd => "tsp mpv",
                                        fs => "--fullscreen",
                                        novideo => "--no-video",
                                        srt => "--sub-file=*SUB*",
                                      },
----
    
### references
- https://youtu.be/I4tfHUmklWo
- https://github.com/trizen/pipe-viewer
- https://github.com/trizen/straw-viewer
- [task-spooler playlist](https://www.youtube.com/playlist?list=PLqv94xWU9zZ3QfX2jQaHotg54NT0Fq3Vu)
- [tmux playlist](https://www.youtube.com/playlist?list=PL5BE1545D8486D66D)

### Contact

                 _   _     _      _
      __ _  ___ | |_| |__ | | ___| |_ _   _
     / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
    | (_| | (_) | |_| |_) | |  __/ |_| |_| |
     \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
     |___/

- https://www.youtube.com/user/gotbletu
- https://lbry.tv/@gotbletu
- https://twitter.com/gotbletu
- https://github.com/gotbletu
- gotbletu@gmail.com


