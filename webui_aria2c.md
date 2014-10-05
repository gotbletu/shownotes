Notes for video: https://www.youtube.com/watch?v=LCr_0zFcbaM

## 1. requirements
aria2
webui-aria2 (download from https://github.com/ziahamza/webui-aria2 )
python (if you want to use the simplehttpserver)


## 2. add these shits to ~/.bashrc or ~/.zshrc

    aria2c-quit() {
    
    	killall aria2c
    	kill $(ps -ef | grep '[h]ttp.server' | awk '{print $2}')
    	#kill $(ps -ef | grep '[S]impleHTTPServer' | awk '{print $2}')
    	}
    
    aria2c-webui() {
    
    	# download location
    	DIR_DL=~/Downloads
    
    	# run as daemon
    	aria2c --enable-rpc --rpc-listen-all -D -d "$DIR_DL"
    
    
    	# use python simplehttpserver to host the webui 
    	# this avoids download the index.html file on each computer
    	# https://github.com/ziahamza/webui-aria2
    	
    	# path to the webui index.html
    	DIR_WEBUI=~/.binary/webui-aria2/
    
    	# webui-aria2c uses port 6800 so we use 6801 for python_simple_http_server
    	PORT=6801
    	cd "$DIR_WEBUI"
    	nohup python3 -m http.server "$PORT" >/dev/null 2>&1&
    
    	# for older distro
    	# nohup python2 -m SimpleHTTPServer "$PORT" >/dev/null 2>&1&
    	
    	echo "connect via http://localhost:6801 or http://ip_address_of_server:6801"
    
    	}


## 3. Aria2c Integration addon ( Chrome / Chromium)
https://chrome.google.com/webstore/detail/aria2c-integration/edcakfpjaobkpdfpicldlccdffkhpbfk?hl=en

 
