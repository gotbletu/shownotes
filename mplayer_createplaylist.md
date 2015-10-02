# Mplaylist - Play and Resume Audiobooks using Mplayer
mplaylist is Python script which can play audio playlists (.m3u files),
remembering the current playback position (file and time) even when killed,
so it will resumes playback at the proper position upon restart. The playback
position is saved as an .m3u.pos file next to the .m3u file. mplaylist
uses mplayer for playing the audio files.
* tutorial video: [Link](https://www.youtube.com/watch?v=opra9r0-rtw)
* offical website: [Link](https://github.com/pts/mplaylist)

### install requirements
    python2
    mplayer
    mplaylist (https://github.com/pts/mplaylist)
   
### function to create playlist
    mplayer-createplaylist() { ls --ignore="*.m3u" --ignore="*.pos" | grep -i "$1" | sort -u > "$1".m3u ;}

### usage
    mplaylist playlist.m3u

### mplayer hotkeys
    q = quit
    < = previous on playlist
    > = next on playlist
    Enter = next

### references
- https://github.com/pts/mplaylist
- https://aur.archlinux.org/packages/play-git/
- https://aur.archlinux.org/packages/cplay-git


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


