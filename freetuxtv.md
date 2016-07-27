# FreeTuxTV - Watch Free IPTV Channels Using VLC
Using the FreeTuxTV Database of Working WebTV channels and playing it with VLC
* tutorial video: [Link](https://www.youtube.com/watch?v=ZTLIGP98zpk)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

### install requirements
    vlc

### configuration
    vim ~/.bashrc or vim ~/.zshrc
    
    #-------- FreeTuxTV - Free IPTV Using Existing Database {{{
    #------------------------------------------------------
    # DEMO: https://www.youtube.com/watch?v=ZTLIGP98zpk
    # DESC: free iptv working list from freetuxtv webtv database
    # REFF: http://database.freetuxtv.net/site/index
    #       How to use nvlc: https://www.youtube.com/watch?v=7y_58wpHuFE
    
    alias nvlc='nvlc --no-color'				# vlc black/white color
    freetuxtv-french() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=fr&isp=all" ;}
    freetuxtv-english() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=en&isp=all" ;}
    freetuxtv-turkish() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=tr&isp=all" ;}
    freetuxtv-spanish() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=es&isp=all" ;}
    freetuxtv-german() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=de&isp=all" ;}
    freetuxtv-arabic() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=ar&isp=all" ;}
    freetuxtv-italian() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=it&isp=all" ;}
    freetuxtv-russian() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=ru&isp=all" ;}
    freetuxtv-chinese() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=zh&isp=all" ;}
    freetuxtv-slovak() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=sk&isp=all" ;}
    freetuxtv-czech() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=cs&isp=all" ;}
    freetuxtv-hungerian() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=hu&isp=all" ;}
    freetuxtv-portuguese() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=pt&isp=all" ;}
    freetuxtv-bulgarian() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=bg&isp=all" ;}
    freetuxtv-romanian() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=ro&isp=all" ;}
    freetuxtv-serbo-croatian() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=sh&isp=all" ;}
    freetuxtv-serbian() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=sr&isp=all" ;}
    freetuxtv-dutch() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=nl&isp=all" ;}
    freetuxtv-croatian() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=hr&isp=all" ;}
    freetuxtv-persian() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=fa&isp=all" ;}
    freetuxtv-polish() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=pl&isp=all" ;}
    freetuxtv-hindi() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=hi&isp=all" ;}
    freetuxtv-albanian() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=sq&isp=all" ;}
    freetuxtv-macedonian() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=mk&isp=all" ;}
    freetuxtv-indonesian() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=in&isp=all" ;}
    freetuxtv-greek() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=el&isp=all" ;}
    freetuxtv-korean() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=ko&isp=all" ;}
    freetuxtv-hebrew() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=iw&isp=all" ;}
    freetuxtv-ukrainian() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=uk&isp=all" ;}
    freetuxtv-vietnamese() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=vi&isp=all" ;}
    freetuxtv-slovenian() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=sl&isp=all" ;}
    freetuxtv-thai() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=th&isp=all" ;}
    # freetuxtv-japanese() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=ja&isp=all" ;}
    freetuxtv-finnish() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=fi&isp=all" ;}
    freetuxtv-lithuanian() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=lt&isp=all" ;}
    freetuxtv-danish() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=da&isp=all" ;}
    freetuxtv-kurdish() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=ku&isp=all" ;}
    freetuxtv-swedish() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=sv&isp=all" ;}
    freetuxtv-azerbaijani() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=az&isp=all" ;}
    freetuxtv-amharic() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=am&isp=all" ;}
    freetuxtv-malay() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=ms&isp=all" ;}
    freetuxtv-norwegian() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=no&isp=all" ;}
    freetuxtv-bengali-bangla() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=bn&isp=all" ;}
    freetuxtv-armenian() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=hy&isp=all" ;}
    freetuxtv-georgian() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=ka&isp=all" ;}
    freetuxtv-urdu() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=ur&isp=all" ;}
    # freetuxtv-latin() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=la&isp=all" ;}
    freetuxtv-catalan() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=ca&isp=all" ;}
    freetuxtv-tagalog() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=tl&isp=all" ;}
    freetuxtv-estonian() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=et&isp=all" ;}
    freetuxtv-latvian-lettish() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=lv&isp=all" ;}
    freetuxtv-afrikaans() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=af&isp=all" ;}
    freetuxtv-kazakh() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=kk&isp=all" ;}
    freetuxtv-cambodian() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=km&isp=all" ;}
    # freetuxtv-malayalam() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=ml&isp=all" ;}
    freetuxtv-somali() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=so&isp=all" ;}
    # freetuxtv-gujarati() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=gu&isp=all" ;}
    freetuxtv-mongolian() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=mn&isp=all" ;}
    freetuxtv-maltese() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=mt&isp=all" ;}
    freetuxtv-turkmen() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=tk&isp=all" ;}
    freetuxtv-irish() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=ga&isp=all" ;}
    # freetuxtv-interlingua() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=ia&isp=all" ;}
    freetuxtv-moldavian() { nvlc "http://database.freetuxtv.net/WebStreamExport/index?format=m3u&type=1&status=2&lng=mo&isp=all" ;}
    
    # }}}

### references
- http://database.freetuxtv.net/site/index
- [How to use NVLC](https://www.youtube.com/watch?v=7y_58wpHuFE)

### contact

                 _   _     _      _         
      __ _  ___ | |_| |__ | | ___| |_ _   _ 
     / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
    | (_| | (_) | |_| |_) | |  __/ |_| |_| |
     \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
     |___/                                  

- http://www.youtube.com/user/gotbletu
- https://twitter.com/gotbletu
- https://plus.google.com/+gotbletu
- https://github.com/gotbletu
- gotbletu@gmail.com


