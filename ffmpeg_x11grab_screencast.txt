# this is notes for video: http://www.youtube.com/watch?v=mNz5Lrc06_s

#-------- FFMPEG X11GRAB Screencasting
#------------------------------------------------------
# compile ffmpeg:	http://ubuntuforums.org/showthread.php?t=786095
# proper screencast: 	http://ubuntuforums.org/showthread.php?t=1392026
# http://nowardev.wordpress.com/2011/05/23/how-to-screencast/
# press q to quit

# orginal one line code for fullscreen
ffmpeg -f alsa -ac 2 -i hw:0,0 -f x11grab -r 30 -s $(xwininfo -root | grep 'geometry' | awk '{print $2;}') -i :0.0 -acodec pcm_s16le -vcodec libx264 -preset ultrafast -crf 0 -threads 0 -y screencast_out.avi

# record single window, use mouse to click on the window to start recording
ffmpeg -f alsa -ac 2 -i hw:0,0 -f x11grab -r 30 -s $(xwininfo -frame | grep -oEe 'geometry [0-9]+x[0-9]+' | grep -oEe '[0-9]+x[0-9]+') -i :0.0+$(xwininfo -frame | grep -oEe 'Corners:\s+\+[0-9]+\+[0-9]+' | grep -oEe '[0-9]+\+[0-9]+' | sed -e 's/\+/,/' ) -acodec pcm_s16le -vcodec libx264 -preset ultrafast -crf 0 -threads 0 -y screencast_out.avi

# -y = will overwrite output file

#Note: if u have problems with preset errors,
# run 'x264 -h' look for supported presets and replace it, like
# ultrafast, superfast, fast ...etc


#Note 2: If you like to scale down your videos at the same time when recording
# add in for example
# -vf "scale=1280:720"
# The reason this is useful is becuase I have a 16:10 resolution but youtube only supports 16:9
# So I can avoid the black bars on left/right side of the videos with this option






#==============================================
# This is what I use, added to bashrc/zshrc

FFX_MONO="1"		# mono
FFX_DUAL="2"		# dual channel
FFX_HW="hw:1,0" 	# alsa; run 'cat /proc/asound/pcm' to change to the correct numbers
FFX_PULSE="pulse" 	# pulseaudio; might have to install pavucontrol to change volume
FFX_FPS="30"		# frame per seconds
FFX_WIN_FULL=$(xwininfo -root | grep 'geometry' |awk '{print $2;}')	# record fullscreen
FFX_AUDIO="pcm_s16le"	# audio codec
FFX_VIDEO="libx264"	# video codec
FFX_PRESET="ultrafast"	# preset error? run 'x264 -h' replace with fast,superfast, slow ..etc
FFX_CRF="0"
FFX_THREADS="0"
FFX_SCALE="scale=1280:720"	# scale resolution, no black bars on sides of video on youtube
FFX_OUTPUT=~/Public/screencast/aa_screencast_baking.avi
# Note: -vf is optional delete if you want, -y is to overwrite existing file

# capture fullscreen using alsa or pulseaudio
ffx-full-hw() { ffmpeg -f alsa -ac $FFX_MONO \
	-i $FFX_HW -f x11grab -r $FFX_FPS -s $FFX_WIN_FULL -i :0.0 \
	-acodec $FFX_AUDIO -vcodec $FFX_VIDEO \
       	-preset $FFX_PRESET -crf $FFX_CRF -threads $FFX_THREADS \
	-vf $FFX_SCALE \
	-y $FFX_OUTPUT
}
ffx-full-pa() { ffmpeg -f alsa -ac $FFX_MONO \
	-i $FFX_PULSE -f x11grab -r $FFX_FPS -s $FFX_WIN_FULL -i :0.0 \
	-acodec $FFX_AUDIO -vcodec $FFX_VIDEO \
       	-preset $FFX_PRESET -crf $FFX_CRF -threads $FFX_THREADS \
	-vf $FFX_SCALE \
	-y $FFX_OUTPUT
}

# capture single window, use mouse cursor to select window you want to record
ffx-winselect-hw() { 
	FFX_INFO=$(xwininfo -frame)

	ffmpeg -f alsa -ac $FFX_MONO \
	-i $FFX_HW -f x11grab -r $FFX_FPS \
	-s $(echo $FFX_INFO | grep -oEe 'geometry [0-9]+x[0-9]+'\
	| grep -oEe '[0-9]+x[0-9]+') \
	-i :0.0+$(echo $FFX_INFO | grep -oEe 'Corners:\s+\+[0-9]+\+[0-9]+' \
	| grep -oEe '[0-9]+\+[0-9]+' | sed -e 's/\+/,/' ) \
	-acodec $FFX_AUDIO -vcodec $FFX_VIDEO \
       	-preset $FFX_PRESET -crf $FFX_CRF -threads $FFX_THREADS \
	-vf $FFX_SCALE \
	-y $FFX_OUTPUT
}
ffx-winselect-pa() { 
	FFX_INFO=$(xwininfo -frame)

	ffmpeg -f alsa -ac $FFX_MONO \
	-i $FFX_PULSE -f x11grab -r $FFX_FPS \
	-s $(echo $FFX_INFO | grep -oEe 'geometry [0-9]+x[0-9]+'\
	| grep -oEe '[0-9]+x[0-9]+') \
	-i :0.0+$(echo $FFX_INFO | grep -oEe 'Corners:\s+\+[0-9]+\+[0-9]+' \
	| grep -oEe '[0-9]+\+[0-9]+' | sed -e 's/\+/,/' ) \
	-acodec $FFX_AUDIO -vcodec $FFX_VIDEO \
       	-preset $FFX_PRESET -crf $FFX_CRF -threads $FFX_THREADS \
	-vf $FFX_SCALE \
	-y $FFX_OUTPUT
}
