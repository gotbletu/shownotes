Notes for video:
https://www.youtube.com/watch?v=NG13yOTPgfY



## 1. download the piratebay / torrentzeu script:
https://github.com/saironiq/shellscripts

    git clone https://github.com/saironiq/shellscripts.git


## 2. edit the script

   program='/usr/bin/peerflix -p 55055'


## 3. alias

    PFLIX_PORT=55055
    pfx() { ~/.binary/peerflix_script/thepiratebay_se/tpb.sh $@ ;}
    pfx-trz() { ~/.binary/peerflix_script/torrentz_eu/torrentz_eu.sh $@ ;}
    pfx-vlc() { vlc http://localhost:$PFLIX_PORT ;}
    pfx-mplayer() { mplayer http://localhost:$PFLIX_PORT ;}	
    
