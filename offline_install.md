Notes for video: http://www.youtube.com/watch?v=MhdE_3Ws5Jo

# Offline update install packages:
1) Refresh your repository list
> sudo apt-get update

2) Makes a list of apps/security that needs to be update from your system
> sudo apt-get --print-uris -y upgrade | grep "'" | cut -d\' -f2 > mylist.txt


3) downloads all the debs
> wget -i mylist.txt

4) installs all the deb files at once
> sudo dpkg -i *.deb

