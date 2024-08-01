# aMule on the command line
- aMulecmd demo: https://youtu.be/IpHdH1mCUVc
- amule, emule, ed2k, edonkey2000, kademlia, p2p, file sharing, emule

#### enable amule remote controls
- amule > preferences > remote controls > [x] accept external connections
- amule > preferences > remote controls > password > [0123456789]

#### generate a remote.conf
----
    # amulecmd -h hostname -p ECport -P ECpassword -w
    # amulecmd -h 192.168.1.xxx -p 4712 -P 0123456789 -w
    amulecmd -h localhost -p 4712 -P 0123456789 -w
----

#### amulecmd.conf
- put amulecmd.conf in ~/.aMule/amulecmd.conf
- make sure all the login stuff is correct

#### start daemon
    amuled --full-daemon


#### start text client
    amulecmd

#### using scripts to start daemon and text client
    amulecli-daemon-start ; amulecli-textmode

#### Example Tmux Layout for Localhost
    session="amule"
    sessionexists=$(tmux list-sessions | grep "^$session":)
    if [ -z "$sessionexists" ]; then
      # create new session
      tmux new-session -d -s "$session" -c "$HOME"
      tmux new-window -t "$session":0 -n 'results' -c "$HOME"
      tmux rename-window -t "$session":0 'results'
      tmux send-keys -t "$session":0 "while true; do amulecli-results-hightop | less ; done" C-m
      tmux split-window -t "$session":0 -v -l 10 -c "$HOME"
      tmux send-keys -t "$session":0 'amulecli-daemon-start ; amulecli-textmode' C-m
    
      tmux new-window -t "$session":1 -n 'list-watch' -c "$HOME"
      tmux send-keys -t "$session":1 'watch -n 5 -t amulecli-list' C-m
      tmux split-window -t "$session":1 -v -l 15 -c "$HOME"
    
      tmux new-window -t "$session":2 -n 'servers' -c "$HOME"
      tmux send-keys -t "$session":2 'watch -n 60 -t amulecli-servers' C-m
      tmux split-window -t "$session":2 -v -l 10 -c "$HOME"
      tmux send-keys -t "$session":2 'amulecli-textmode' C-m
    
      tmux new-window -t "$session":3 -n 'amulebay' -c "$HOME"
      tmux send-keys -t "$session":3 "while true; do \
        tmux rename-window -t $session:3 amulebay && clear && \
        ranger ~/.aMule/Incoming ~/.aMule/Temp \
        --cmd='set preview_files false' ; done" C-m
    
      tmux switch-client -t "$session":0
    else
      tmux switch-client -t "$session"
    fi

#### Example Tmux Layout for Server
    session="amule-server"
    sessionexists=$(tmux list-sessions | grep "^$session":)
    if [ -z "$sessionexists" ]; then
      # create new session
      tmux new-session -d -s "$session" -c "$HOME"
      tmux new-window -t "$session":0 -n 'results' -c "$HOME"
      tmux rename-window -t "$session":0 'results'
      tmux send-keys -t "$session":0 "while true; do amulecli-results-hightop --config ~/.aMule/amulecmd-server.conf | less ; done" C-m
      tmux split-window -t "$session":0 -v -l 10 -c "$HOME"
      tmux send-keys -t "$session":0 'amulecli-textmode --config ~/.aMule/amulecmd-server.conf' C-m

      tmux new-window -t "$session":1 -n 'list-watch' -c "$HOME"
      tmux send-keys -t "$session":1 'watch -n 5 -t amulecli-list --config ~/.aMule/amulecmd-server.conf' C-m
      tmux split-window -t "$session":1 -v -l 15 -c "$HOME"

      tmux new-window -t "$session":2 -n 'servers' -c "$HOME"
      tmux send-keys -t "$session":2 'watch -n 60 -t amulecli-servers --config ~/.aMule/amulecmd-server.conf' C-m
      tmux split-window -t "$session":2 -v -l 10 -c "$HOME"
      tmux send-keys -t "$session":2 'amulecli-textmode --config ~/.aMule/amulecmd-server.conf' C-m

      tmux new-window -t "$session":3 -n 'amulebay' -c "$HOME"
      tmux send-keys -t "$session":3 "while true; do \
        tmux rename-window -t $session:3 amulebay && clear && \
        ranger /run/user/1000/sshfs/heoyea@192.168.1.131/alfa/amule/completed \
        --cmd='set preview_files false' ; done" C-m

      tmux switch-client -t "$session":0
    else
      tmux switch-client -t "$session"
    fi

