#!/bin/bash
# http://toolbartv.swagbucks.com
# requires: xdotool
# xdotool getmouselocation
# xdotool mousemove x y
# made by gotbleu
# improved by jonny

# ------------------------------------------------------
# y cordinates ranges (top to bottom)
FIXEDBOX=$(shuf -i 520-577 -n 1)

# x cordinates ranges (left to right)
# will select a random number within that range
BOX1=$(shuf -i 32-105 -n 1)
BOX2=$(shuf -i 116-190 -n 1)
BOX3=$(shuf -i 200-274 -n 1)
BOX4=$(shuf -i 285-357 -n 1)

# x & y cordinates ranges for the right green arrow
# will select a random number within that range
X_ARROW=$(shuf -i 369-373 -n 1)	# left to right
Y_ARROW=$(shuf -i 555-560 -n 1) # top to bottom

# sound play when finish
alertme() {
	mplayer ~/Public/sound-effects/mariobros/cheerRedTeam.wav
}
#-----------------------------------------------------

# sleep timer before next click (dont need to change this)
SLPNUM=$(shuf -i 65-90 -n 1)


# made it move 2 times to the same box
# my lame way of making it click if i am on the computer using the mouse also.
video_one() {
	xdotool mousemove $BOX1 $FIXEDBOX
	xdotool click 1
	sleep $SLPNUM
}
video_two() {
	xdotool mousemove $BOX2 $FIXEDBOX
	xdotool click 1
	sleep $SLPNUM
}

video_three() {
	xdotool mousemove $BOX3 $FIXEDBOX
	xdotool click 1
	sleep $SLPNUM
}
video_four() {
	xdotool mousemove $BOX4 $FIXEDBOX
	xdotool click 1
	sleep $SLPNUM
}

arrow_click() {
	xdotool mousemove $X_ARROW $Y_ARROW
	xdotool click 1
	sleep 5
}

# start from box1
method_a() {
	# initial sleep time delay; so u can move your terminal/apps out of the way
	sleep 3
	video_one && video_two && video_three && video_four
	arrow_click
	video_one && video_two && video_three && video_four
	arrow_click
	video_one && video_two
	alertme
}

method_c() {
        # initial sleep time delay; so u can move your terminal/apps out of the way
        sleep 3
        video_one && video_two && video_three && video_four
        arrow_click
	ever
}

ever() {
	video_one && video_two && video_three && video_four
        arrow_click
	method_c
}
# start from box3
method_b() {
	# initial sleep time delay; so u can move your terminal/apps out of the way
	sleep 3
	video_three && video_four
	arrow_click
	video_one && video_two && video_three && video_four
	arrow_click
	video_one && video_two && video_three && video_four
	alertme
}


# This is for when i need to take a long shit; so make it stop at video number 9
# start from box1
shit_a() {
	# initial sleep time delay; so u can move your terminal/apps out of the way
	sleep 3
	video_one && video_two && video_three && video_four
	arrow_click
	video_one && video_two && video_three && video_four
	arrow_click
	video_one
}
# start from box3
shit_b() {
	# initial sleep time delay; so u can move your terminal/apps out of the way
	sleep 3
	video_three && video_four
	arrow_click
	video_one && video_two && video_three && video_four
	arrow_click
	video_one && video_two && video_three
}

# enter in options users like to run
if [[ "$1" == 1 ]]; then
	method_a
elif [[ "$1" == 2 ]]; then
	method_b
elif [[ "$1" == 1shit ]]; then
	shit_a
elif [[ "$1" == 2shit ]]; then
	shit_b
elif [[ "$1" == 3 ]]; then
        method_c
else
	echo "enter argument 1, 2, 3, 1shit, or 2shit. example: sbtv 2"
fi
