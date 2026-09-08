#!/bin/bash
#             _   _     _      _
#  __ _  ___ | |_| |__ | | ___| |_ _   _
# / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
#| (_| | (_) | |_| |_) | |  __/ |_| |_| |
# \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
# |___/
#       https://www.youtube.com/user/gotbletu
#       https://twitter.com/gotbletu
#       https://github.com/gotbletu
#       gotbletu@gmail.com

#                   _                  _        _
#        _   _ _ __| |_ __   ___  _ __| |_ __ _| |
#       | | | | '__| | '_ \ / _ \| '__| __/ _` | |
#       | |_| | |  | | |_) | (_) | |  | || (_| | |
#        \__,_|_|  |_| .__/ \___/|_|   \__\__,_|_|
#                    |_|
#       DESC: custom way to handle url (similar idea to xdg-open, mailcap)
#             works with just about all programs (e.g w3m, rtv, newsboat, urlview ...etc)
#       DEMO: https://www.youtube.com/watch?v=2jyfrmBYzVQ
#       install: lynx youtube-dl task-spooler newsboat rtv w3m mpv urlview tmux feh plowshare streamlink curl coreutils


# newsboat:
#     vim ~/.newsboat/config
#         browser ~/.scripts/urlportal.sh

# rtv:
#     vim ~/.bashrc
#         export RTV_BROWSER=~/.scripts/urlportal.sh

# w3m:
#     vim ~/.w3m/keymap
#         open url under cursor (default: Esc+Shift+M); e.g 2+Esc+Shift+M
#         keymap  e       EXTERN_LINK ~/.scripts/urlportal.sh

# urlview:
#     vim ~/.urlview
#         COMMAND ~/.scripts/urlportal.sh

# references:
# cirrusuk http://arza.us/paste/piper
# obosob https://github.com/michael-lazar/rtv/issues/78#issuecomment-125507472
# budlabs - mpv queue https://www.youtube.com/watch?v=-vbr3-mHoRs
#                     https://github.com/budlabs/youtube/blob/master/letslinux/032-queue-files-in-mpv/openvideo
# ji99 - mpv queue script https://www.reddit.com/r/commandline/comments/920p5d/bash_script_for_queueing_youtube_links_in_mpv/


# BROWSERCLI="w3m"
# BROWSER="chromium"
# DEFAULT="xdg-open"
# DEFAULT="chromium --incognito"
# DEFAULT="w3m"
DEFAULT="$BROWSERCLI"
## long videos like youtube
VIDEO_QUEUE="tsp mpv --ontop --no-border --force-window --autofit=500x280 --geometry=-15-53"
## short videos/animated gif clips
VIDEO_CLIP="mpv --loop --quiet --ontop --no-border --force-window --autofit=900x600 --geometry=-15+60"
IMAGEGUI="feh -. -x -B black -g 900x600-15+60"
# IMAGECLI="w3m /usr/lib/w3m/cgi-bin/treat_as_url.cgi -o display_image=1 -o imgdisplay=/usr/lib/w3m/w3mimgdisplay"
IMAGECLI="w3m -o display_image=1 -o imgdisplay=w3mimgdisplay"
# IMAGECLI="fbi"
TORRENTCLI="transmission-remote --add"
# LIVEFEED='streamlink -p "mpv --cache 2048 --ontop --no-border --force-window --autofit=500x280 --geometry=-15-60"'
LIVEFEED="tsp streamlink"
DDL_PATH=~/Downloads/plowshare
DDL_QUEUE_FAST=~/.config/plowshare/queuefast.txt


# enable case-insensitive matching
shopt -s nocasematch

url="$1"
case "$url" in
    *gfycat.com/*|*streamable.com/*)
        nohup $VIDEO_CLIP "${url/.gifv/.webm}" > /dev/null 2>&1 &
        ;;
    *v.redd.it/*|*video.twimg.com/*|*dailymotion.com*)
        nohup $VIDEO_CLIP "$url" > /dev/null 2>&1 &
        ;;
    *youtube.com/watch*|*youtu.be/*|*clips.twitch.tv/*)
        $VIDEO_QUEUE "$url"
        ;;
    *twitch.tv/*)
        $LIVEFEED "$url"
        ;;
    *pornhub.com/*|*xvideos.com/*)
        # $VIDEO_QUEUE "$url"
        nohup $VIDEO_CLIP "$url" > /dev/null 2>&1 &
        ;;
    *reddit.com/r/*)
        tmux new-window -n rtv && tmux send-keys "rtv -l $url && tmux kill-pane" 'Enter'
        ;;
    *glodls.to/*|*eogli.org/*|*limetorrents.io/*|*limetorrents.cc/*|*pornoshara.tv/item*|*rustorrents.net/details*|*xxx-tracker.com/*)
        tmux new-window -n browse && tmux send-keys "$BROWSERCLI '$url' && tmux kill-pane" 'Enter'
        ;;
    *thepiratebay.org/*|*torrentdownloads.me/*|*yourbittorrent2.com/*|*torlock2.com/*|*bt-scene.cc/*|*rarbg.to/*|*ettorrent.xyz/*)
        tmux new-window -n browse && tmux send-keys "$BROWSERCLI '$url' && tmux kill-pane" 'Enter'
        ;;
    *22pixx.xyz/ia-i/*)
        cleanurl="$(printf $url | sed 's/ia-i/i/g' | sed 's/\.html//g')"
        tmux new-window -n pixcli && tmux send-keys "$IMAGECLI '$cleanurl' && tmux kill-pane" 'Enter'
        ;;
    *freebunker.com/*)
        cleanurl="$(printf $url | sed 's@img\/@tn\/i@')"
        tmux new-window -n pixcli && tmux send-keys "$IMAGECLI '$cleanurl' && tmux kill-pane" 'Enter'
        ;;
    *imagerar.com/t/*)
        cleanurl="$(printf $url | sed 's@/t@/u@')"
        tmux new-window -n pixcli && tmux send-keys "$IMAGECLI '$cleanurl' && tmux kill-pane" 'Enter'
        ;;
    *imagerar.com/imgy-u/*)
        cleanurl="$(printf $url | sed 's/imgy-u/u/g' | sed 's/.html//g')"
        tmux new-window -n pixcli && tmux send-keys "$IMAGECLI '$cleanurl' && tmux kill-pane" 'Enter'
        ;;
    *imageshtorm.com/upload/small/*|*hotimage.uk/upload/small/*|*hdmoza.com//upload/small/*|*nikapic.ru/upload/small/*|*imagedecode.com/upload/small/*|*trans.firm.in//upload/small/*)
        # nohup $IMAGEGUI "$(printf $url | sed 's/small/big/')" > /dev/null 2>&1 &
        cleanurl="$(printf $url | sed 's/small/big/')"
        tmux new-window -n pixcli && tmux send-keys "$IMAGECLI '$cleanurl' && tmux kill-pane" 'Enter'
        ;;
    *imageshtorm.com/img*)
        # nohup $IMAGEGUI "$(printf $url | sed 's/small/big/')" > /dev/null 2>&1 &
        cleanurl="$(curl -s "$url" | grep onclick | grep -oP '<a href=\047\K[^\047]+')"
        tmux new-window -n pixcli && tmux send-keys "$IMAGECLI '$cleanurl' && tmux kill-pane" 'Enter'
        ;;
    *freescreens.ru/allimage/*|*imgclick.ru/allimage/*|*money-pic.ru/allimage/*)
        cleanurl="$(printf $url | sed 's/-thumb//')"
        tmux new-window -n pixcli && tmux send-keys "$IMAGECLI '$cleanurl' && tmux kill-pane" 'Enter'
        ;;
    *freescreens.ru/*)
        cleanurl="$(printf "$url/1/" | sed 's/freescreens.ru/picpic.online/')"
        tmux new-window -n pixcli && tmux send-keys "$IMAGECLI '$cleanurl' && tmux kill-pane" 'Enter'
        ;;
    *pixcloud.ru/view*)
        cleanurl="$(curl -s "$url" | grep -oP '<img id="photo" src="\K[^"]+')"
        tmux new-window -n pixcli && tmux send-keys "$IMAGECLI '$cleanurl' && tmux kill-pane" 'Enter'
        ;;
    *money-pic.ru/*)
        cleanurl="$(curl -s "$url/1/" | grep allimage | grep -oP '<img src="\K[^"]+')"
        tmux new-window -n pixcli && tmux send-keys "$IMAGECLI '$cleanurl' && tmux kill-pane" 'Enter'
        ;;
    *imagecurl.com/viewer.php?file=*)
        cleanurl="$(printf $url | sed 's@https://@https://cdn.@' | sed 's@/viewer.php?file=@/images/@')"
        tmux new-window -n pixcli && tmux send-keys "$IMAGECLI '$cleanurl' && tmux kill-pane" 'Enter'
        ;;
    *img2share.com/*|*imgpeak.com/*|*damimage.com/img*|*imagedecode.com/img*|*picfuture.com/*|*imageteam.org/*|*imgsalem.com/*|*dimtus.com/img*|*imgstudio.org/img*|*imagehub.pro/img*|*trans.firm.in//img*|*pic.hotimg.site/img*)
        # cleanurl="$(curl -s "$url" | grep -oP '<img class=\047centred\047 src=\047\K[^\047]+')"
        cleanurl="$(curl -s "$url" | grep centred | grep -oP 'src=\047\K[^\047]+')"
        tmux new-window -n pixcli && tmux send-keys "$IMAGECLI '$cleanurl' && tmux kill-pane" 'Enter'
        ;;
    *imgadult.com/img*|*imgdrive.net/*)
        cleanurl="$(curl -s "$url" | grep -oP '<meta property="og:image" content="\K[^"]+' | sed 's/small/big/')"
        tmux new-window -n pixcli && tmux send-keys "$IMAGECLI '$cleanurl' && tmux kill-pane" 'Enter'
        ;;
    *xxximagetpb.org/*|*img-central.com/*|*imgdone.com/image/*|*i.nmfiles.com/image/*|*i.imghost.top/image/*|*mstimg.com/image/*|*imagebam.com/image/*|*imgflip.com/i/*)
        cleanurl="$(lynx -source "$url" | grep -oP '<meta property="og:image" content="\K[^"]+')"
        tmux new-window -n pixcli && tmux send-keys "$IMAGECLI '$cleanurl' && tmux kill-pane" 'Enter'
        ;;
    *wallpaperspic.pw/*|*pornweb.xyz/*)
        cleanurl="$(curl -s "$url" | grep imagebam | grep -oP '<p><img src="\K[^"]+')"
        tmux new-window -n pixcli && tmux send-keys "$IMAGECLI '$cleanurl' && tmux kill-pane" 'Enter'
        ;;
    */imagetwist.com/*)
        cleanurl="$(curl -s "$url" | grep -oP '<p style="display: block; text-align:center;"><img src="\K[^"]+')"
        tmux new-window -n pixcli && tmux send-keys "$IMAGECLI '$cleanurl' && tmux kill-pane" 'Enter'
        ;;
    *imgtornado.com/img*|*placeimg.net/img*|*http://imgjazz.com/img*|*picmoza.com//img*|*xxxwebdlxxx.org/img*)
        cleanurl="$(curl --data "imgContinue=Continue to image ..." --location "$url" | grep centred | grep -oP 'src=\047\K[^\047]+')"
        tmux new-window -n pixcli && tmux send-keys "$IMAGECLI '$cleanurl' && tmux kill-pane" 'Enter'
        ;;
    *hotimage.uk/img*)
        cleanurl="$(curl --data "imgContinue=Continue to image ..." --location "$(printf $url | sed 's@http://@https://www.@')" | grep centred | grep -oP 'src=\047\K[^\047]+')"
        tmux new-window -n pixcli && tmux send-keys "$IMAGECLI '$cleanurl' && tmux kill-pane" 'Enter'
        ;;
    *i.imgur.com/*.gifv|*i.imgur.com/*.mp4|*i.imgur.com/*.webm|*i.imgur.com/*.gif)
        nohup $VIDEO_CLIP "$url" > /dev/null 2>&1 &
        ;;
    *i.imgur.com/*| *imgur.com/*.*)
        # nohup $IMAGEGUI "$url" > /dev/null 2>&1 &
        tmux new-window -n pixcli && tmux send-keys "$IMAGECLI '$url' && tmux kill-pane" 'Enter'
        ;;
    *imgur.com/*)
        # tmux split-window && tmux send-keys "lynx -source "$url" | grep post-image-container | grep -oP '<div id=\"\K[^\"]+' | while read line; do echo https://i.imgur.com/"\$line".png; done | urlview && tmux kill-pane" 'Enter'
        multiurlextract="(lynx -source "$url" | grep post-image-container | grep -oP '<div id=\"\K[^\"]+' | while read line; do echo https://i.imgur.com/"\$line".png; done | urlview)"
        tmux split-window && tmux send-keys "$multiurlextract && tmux kill-pane" 'Enter'
        ;;
    mailto:*)
        tmux split-window -fv && tmux send-keys "mutt -- '$url' && tmux kill-pane" 'Enter'
        ;;
    *.pls|*.m3u)
        tmux split-window -fv -p 20 && tmux send-keys "mpv '$url' && exit" 'Enter'
        ;;
    magnet:*|*.torrent)
        $TORRENTCLI "$url"
        ;;
    *.jpg|*.jpeg|*.png|*:large)
        tmux new-window -n pixcli && tmux send-keys "$IMAGECLI '$url' && tmux kill-pane" 'Enter'
        # nohup $IMAGEGUI "$url" > /dev/null 2>&1 &
        ;;
    *.gif)
        nohup $VIDEO_CLIP "${url/.gifv/.webm}" > /dev/null 2>&1 &
        ;;
    *zippyshare.com/*|*mediafire.com/file/*|*sendspace.com/file/*)
        if pgrep -f $DDL_QUEUE_FAST > /dev/null
        then
            echo "$url" >> $DDL_QUEUE_FAST
        else
            echo "$url" >> $DDL_QUEUE_FAST
            cat $DDL_QUEUE_FAST | awk '!x[$0]++' | sponge $DDL_QUEUE_FAST
            tmux split-window -fv -p 20 && tmux send-keys "until [[ \$(cat $DDL_QUEUE_FAST | grep -v '#' | wc -l) -eq 0 ]]; do mkdir -p $DDL_PATH && cd $DDL_PATH && plowdown -m $DDL_QUEUE_FAST -o $DDL_PATH ; done" 'Enter'
        fi
        ;;
    *.mp4|*.mkv|*.avi|*.wmv|*.m4v|*.mpg|*.mpeg|*.flv|*.ogm|*.ogv|*.gifv)
        $VIDEO_QUEUE "$url"
        ;;
    *.mp3|*.m4a|*.wav|*.ogg|*.oga|*.flac)
        # create queue fifo files if it does not exist
        if [[ ! -p /tmp/mpvinput ]]; then
            mkfifo /tmp/mpvinput
        fi

        # check if process mpv exist (e.g mpv --input-file=/tmp/mpvinput filename.mp3)
        if pgrep -f mpvinput > /dev/null
        then
            # if mpv is already running then append new url/files to queue
            # echo loadfile \"${url/'/\\'}\" append-play > /tmp/mpvinput
            echo loadfile \"$url\" append-play > /tmp/mpvinput
        # nohup $VIDEO_CLIP "${url/.gifv/.webm}" > /dev/null 2>&1 &
        else
            # if mpv is not running then start it (initial startup)
            # mpv --no-video --input-file=/tmp/mpvinput "$1"
            tmux split-window -fv -p 20 && tmux send-keys "mpv --no-video --input-file=/tmp/mpvinput \"$url\" && exit" 'Enter'
        fi
        # Note: use "<" or ">" hotkeys to skip between songs/audio queue list on mpv
        ;;
    *|*.html)
        # $DEFAULT "$url"
        tmux new-window -n browse && tmux send-keys "$DEFAULT '$url' && tmux kill-pane" 'Enter'
        ;;
esac

