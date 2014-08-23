Notes for video: https://www.youtube.com/watch?v=jhv-2pNWfr4


credits: http://askubuntu.com/a/18210

    pa-list() { pacmd list-sinks | awk '/index/ || /name:/' ;}
    pa-set() { 
    	# list all apps in playback tab (ex: cmus, mplayer, vlc)
    	inputs=($(pacmd list-sink-inputs | awk '/index/ {print $2}')) 
    	# set the default output device
    	pacmd set-default-sink $1 &> /dev/null
    	# apply the changes to all running apps to use the new output device
    	for i in ${inputs[*]}; do pacmd move-sink-input $i $1 &> /dev/null; done
    }
    pa-playbacklist() { 
    	# list individual apps
    	echo "==============="
    	echo "Running Apps"
    	pacmd list-sink-inputs | awk '/index/ || /application.name /'
    
    	# list all sound device
    	echo "==============="
    	echo "Sound Devices"
    	pacmd list-sinks | awk '/index/ || /name:/'
    }
    pa-playbackset() { 
    	# set the default output device
    	pacmd set-default-sink "$2" &> /dev/null
    	# apply changes to one running app to use the new output device
    	pacmd move-sink-input "$1" "$2" &> /dev/null
    }


