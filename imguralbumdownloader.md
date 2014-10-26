Notes for video: https://www.youtube.com/watch?v=dW4co9f5Ors


## 1. functions for ~/.bashrc or ~/.zshrc

    # imgur album downloader
    # https://github.com/alexgisby/imgur-album-downloader
    imguralbum() { python ~/.binary/imgur-album-downloader/imguralbum.py "$@" ;}
    
    imguralbum_cbz() { 
    	# usage: imguralbum [link] [filename]
    	
    	local IMGUR_SAVE_PATH=/tmp
    
    	# make a temp folder
    	# mkdir -p "$IMGUR_SAVE_PATH"/"$2"
    
    	#download album
    	python ~/.binary/imgur-album-downloader/imguralbum.py "$1" "$IMGUR_SAVE_PATH"/"$2"
    
    	#create zip archive using .cbz extension for comics
    	zip -r "${2%/}.cbz" "$IMGUR_SAVE_PATH"/"$2"
    
    	#delete temp folder
    	rm -rf "$IMGUR_SAVE_PATH"/"$2"
    }

