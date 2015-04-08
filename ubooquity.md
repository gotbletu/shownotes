# Ubooquity - Comics and Ebooks Server

Ubooquity is a free, lightweight and easy-to-use home server for your comics and ebooks. Use it to access your files from anywhere, with a tablet, an e-reader, a phone or a computer.

Main features
Simple graphical interface to configure your server in a few minutes
Web administration page available if you prefer to do everything through your browser
User management with secured access, to decide who can see what
Online comic reader to read your comics without downloading huge files
Compatible with Calibre metadata, for better ebooks collection management
Can be installed on any OS supporting Java (Windows, Linux, Mac OS...) and on a wide range of hardware (desktop computer, server, NAS...)

* tutorial video: [Link](https://www.youtube.com/watch?v=qfLG9nKt3ew)
* offical website: [Link](http://vaemendis.net/ubooquity/)

### install requirements
    
    # if you want the gui (optional)
    jre7-openjdk
    
    # for cli server
    jre7-openjdk-headless


    # download ubooquity
    wget "http://vaemendis.net/ubooquity/service/download.php" -O ubooquity.zip
    unzip ubooquity.zip
    mkdir -p ~/.binary/ubooquity
    mv Ubooquity.jar ~/.binary/ubooquity

### aliases
	# add these to ~/.bashrc or ~/.zshrc and reload your shell

	PATH_UBOOQUITY=~/.binary/ubooquity
	ubooquity() { cd $PATH_UBOOQUITY && nohup java -jar $PATH_UBOOQUITY/Ubooquity.jar -webadmin -headless >/dev/null 2>&1& }
	ubooquity-gui() { cd $PATH_UBOOQUITY && nohup java -jar $PATH_UBOOQUITY/Ubooquity.jar -webadmin >/dev/null 2>&1& }
	ubooquity-quit() { kill $(ps -ef | grep '[U]booquity.jar' | awk '{print $2}') ;}
	ubooquity-status() { 
		if ps -ef | grep '[U]booquity.jar' > /dev/null
		then
			echo "Ubooquity is running on http://localhost:2202"
			echo "To change settings use http://localhost:2202/admin"

		else
			echo "Ubooquity has stopped"
		fi
	}

### configuration

    ubooquity
    ubooquity-status

- run the ubooquity command then open browser to: http://localhost:2202/admin




***
### start services
    crontab -e
    
    PATH_UBOOQUITY=~/.binary/ubooquity
    @reboot sleep 180 && cd $PATH_UBOOQUITY && nohup java -jar $PATH_UBOOQUITY/Ubooquity.jar -webadmin -headless

### references

- http://vaemendis.net/ubooquity/static5/documentation

### contact

                 _   _     _      _         
      __ _  ___ | |_| |__ | | ___| |_ _   _ 
     / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
    | (_| | (_) | |_| |_) | |  __/ |_| |_| |
     \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
     |___/                                  

- http://www.youtube.com/user/gotbletu
- https://twitter.com/gotbletu
- https://www.facebook.com/gotbletu
- https://plus.google.com/+gotbletu
- https://github.com/gotbletu
- gotbletu@gmail.com

