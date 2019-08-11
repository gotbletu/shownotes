#!/usr/bin/env bash
###             _   _     _      _         
###  __ _  ___ | |_| |__ | | ___| |_ _   _ 
### / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
###| (_| | (_) | |_| |_) | |  __/ |_| |_| |
### \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
### |___/                                  
###       https://www.youtube.com/user/gotbletu
###       https://twitter.com/gotbletu
###       https://github.com/gotbletu
###       gotbletu@gmail.com
###
### Author          : gotbletu
### Name            : dl_wallhaven_wallpapers.sh
### Version         : 0.2
### Date            : 20190811
### Description     : A script to download random wallpaper and delete old wallpaper at the sametime (wallhaven.cc)
### Depends On      : bash  coreutils  grep  findutils  lynx  wget
### Video Demo      : https://www.youtube.com/watch?v=cDtVEXjiKTw

### Release Notes   : 20190811 -- v0.2 minor fixes to get it working again
###                   20170121 -- v0.1 it has begun


# Variable (you can change any of these to your liking)
real_wall_dir=~/Pictures/Wallpapers
temp_wall_dir=/tmp/wallpaper_wallhaven
expire_wall_date=30

# create folders
mkdir -p $real_wall_dir	
mkdir -p $temp_wall_dir

cd $temp_wall_dir

# get links of images and download it
get_random_url=$(lynx -listonly -nonumbers -dump "https://wallhaven.cc/random" | grep '/w/')
get_images_url=$(echo "$get_random_url" | while read line; do lynx -source "$line" | grep -Po '<img id="wallpaper" src="\K[^"]+' ; done )
dl_images=$(echo "$get_images_url" | while read line; do wget -N "$line" ; done)

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

