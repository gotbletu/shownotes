# Calibre-Server -- Calibre Content Server

http://manual.calibre-ebook.com/cli/calibre-server.html

Video Tutorial:
https://www.youtube.com/watch?v=N1hwEfa9W1s

## 1. install require packages

    calibre

## 2. crontab ( auto start on bootup)
    crontab -e

    # library path
    cbcomic=~/MA_Calibre/Comic
    cbdojinshi=~/MA_Calibre/Dojinshi
    cbeurotica=~/MA_Calibre/Eurotica
    cbhanime=~/MA_Calibre/Hanime
    cbnormal=~/MA_Calibre/Normal
    cbtextbook=~/MA_Calibre/Textbook
    
    
    @reboot calibre-server -p 57770 --daemonize --with-library "$cbcomic"
    
    @reboot calibre-server -p 57771 --daemonize --with-library "$cbdojinshi"
    
    @reboot calibre-server -p 57772 --daemonize --with-library "$cbeurotica"
    
    @reboot calibre-server -p 57773 --daemonize --with-library "$cbhanime"
    
    @reboot calibre-server -p 57774 --daemonize --with-library "$cbnormal"
    
    @reboot calibre-server -p 57775 --daemonize --with-library "$cbtextbook"
    


## 3. connect to Calibre WebUI content server

    # display ip info
    ifconfig
    ip a

open web browser to http://192.168.1.XXX:57770

## 4. alias

    # library path
    cbcomic=~/MA_Calibre/Comic
    cbdojinshi=~/MA_Calibre/Dojinshi
    cbeurotica=~/MA_Calibre/Eurotica
    cbhanime=~/MA_Calibre/Hanime
    cbnormal=~/MA_Calibre/Normal
    cbtextbook=~/MA_Calibre/Textbook

    cmx-quit() { kill $(ps -ef | grep -i '[C]alibre-server' | awk '{print $2}') ;}
    
    cmx-server() {
            calibre-server -p 57770 --daemonize --with-library "$cbcomic"
            
    		calibre-server -p 57771 --daemonize --with-library "$cbdojinshi"
    		
    		calibre-server -p 57772 --daemonize --with-library "$cbeurotica"
    		
    		calibre-server -p 57773 --daemonize --with-library "$cbhanime"
    		
    		calibre-server -p 57774 --daemonize --with-library "$cbnormal"
    		
    		calibre-server -p 57775 --daemonize --with-library "$cbtextbook"
    }


