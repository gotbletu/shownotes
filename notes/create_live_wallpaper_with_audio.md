# Create Live Wallpaper with Audio
- pure ffmpeg action to create a background wallpaper for desktop or tv channel for ersatztv or tunarr
- tutorial video: [Link](https://youtu.be/oSM8jmiUEvI)
- offical website: [Link](https://www.youtube.com/user/gotbletu)

#### commands used
```
# ffmpeg concatenation multiple video/music clips together without reconverting oneliner
  # note: make sure your path/filename doesnt have single qoutes else the command will fail
ffmpeg -safe 0 -f concat -i <(find . -maxdepth 1 -type f -name "*.mp3" -printf "file '$PWD/%f'\n" | sort) -c copy music.mp3

# ffmpeg create loop video to fit audio length 'live wallpaper with music loop'
ffmpeg -stream_loop -1 -i inputvideo.mp4 -i inputaudio.mp3 -map 0:v:0 -map 1:a:0 -shortest -c copy output.mkv


# ---- Optional Extra Commands ----

# ffmpeg convert video to x265 'copy audio'
ffmpeg -i input.mp4 -c:v libx265 -vtag hvc1 -c:a copy output.mp4

# ffmpeg downscale convert video to 720p 'copy everything else'
ffmpeg -i input.mp4 -vf scale=1280:720 -c:a copy output.mp4

# ffmpeg downscale convert video to 720p and change to x265 'copy everything else'
ffmpeg -i input.mp4 -c:v libx265 -vtag hvc1 -vf scale=1280:720 -crf 20 -c:a copy output.mp4

# ffmpeg downscale convert video to 1080p 'copy everything else'
ffmpeg -i input.mp4 -vf scale=1920:1080 -c:a copy output.mp4

# ffmpeg downscale convert video to 1080p and change to x265 'copy everything else'
ffmpeg -i input.mp4 -c:v libx265 -vtag hvc1 -vf scale=1920:1080 -crf 20 -c:a copy output.mp4

# ffmpeg create x loop of video
ffmpeg -stream_loop 3 -i input.mkv -c copy loop3times.mkv

# ffmpeg convert audio to mp3
ffmpeg -i input.ogg -codec:a libmp3lame -qscale:a 2 output.mp3
```

#### contact
                 _   _     _      _         
      __ _  ___ | |_| |__ | | ___| |_ _   _ 
     / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
    | (_| | (_) | |_| |_) | |  __/ |_| |_| |
     \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
     |___/                                  

- http://www.youtube.com/user/gotbletu
- https://odysee.com/@gotbletu
- https://github.com/gotbletu

