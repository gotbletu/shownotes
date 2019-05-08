#!/bin/bash
#             _   _     _      _         
#  __ _  ___ | |_| |__ | | ___| |_ _   _ 
# / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
#| (_| | (_) | |_| |_) | |  __/ |_| |_| |
# \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
# |___/                                  
#       http://www.youtube.com/user/gotbletu
#       https://twitter.com/gotbletu
#       https://plus.google.com/+gotbletu
#       https://github.com/gotbletu
#       gotbletu@gmail.com

# demo video: https://www.youtube.com/watch?v=cDtVEXjiKTw
# A script to download random wallpaper and delete old wallpaper at the sametime (wallhaven.cc)

# Variable (you can change any of these to your liking)
real_wall_dir=~/Pictures/Wallpapers
temp_wall_dir=/tmp/wallpaper_wallhaven
expire_wall_date=30

# create folders
mkdir -p $real_wall_dir	
mkdir -p $temp_wall_dir

cd $temp_wall_dir

# get links of images and download it
get_random_url=$(lynx -dump "https://alpha.wallhaven.cc/random" | awk '/\/wallpaper\// && !/favorites/ && !/thumbTags/ && !/html/ {print $2}')

get_images_url=$(echo "$get_random_url" | while read line; do lynx -source "$line" | grep -Po '(<img id="wallpaper" src=")[^"]*' | cut -d '/' -f3- ; done )

add_https_prefix=$(echo "$get_images_url" | while read line; do echo "https://"$line"" ; done )

dl_images=$(echo "$add_https_prefix" | while read line; do wget -N "$line" ; done)


# delete any file under 200k in size (to avoid shitty thumnbails or crap quality)
find . -type f -iname "*.jp*g" -size -200k -exec rm {} \;
find . -type f -iname "*.png" -size -200k -exec rm {} \;

# change the downloaded wallpaper metadata (modified date to todays date)
#  this makes it easy to see which files are older to delete later on
find . -type f -iname "*.jp*g" -exec touch -m {} \;
find . -type f -iname "*.png" -exec touch -m {} \;

# now that everything is cleaned and filter
#  send the downloaded images to the wallpaper folder 
find . -type f -iname "*.jp*g" -exec mv {} $real_wall_dir \;
find . -type f -iname "*.png" -exec mv {} $real_wall_dir \;

#  delete wallpaper image older then X days and remove temp folder
rm -rf $temp_wall_dir
find $real_wall_dir -mtime +$expire_wall_date -exec rm {} \;
