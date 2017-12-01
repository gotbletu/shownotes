# Wget Batch Download Based on File Extensions
* tutorial video: [Link](https://www.youtube.com/watch?v=oWRBjLy8B-I)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

### install requirements
    wget

### configuration
    vim ~/.bashrc or vim ~/.zshrc
    
    #-------- Wget (Retrieve Files From The Web) {{{
    #------------------------------------------------------
    wget-extension() {
      if [ $# -lt 2 ]; then
        echo -e "Download all files with specific extension on a webpage"
        echo -e "\nUsage: $0 <file_extension> <url>"
        echo -e "\nExample:\n$0 mp4 http://example.com/files/"
        echo -e "$0 mp3,ogg,wma http://samples.com/files/"
        echo -e "\nGoogle: http://lmgtfy.com/?q=intitle%3Aindex.of+mp3+-html+-htm+-php+-asp+-txt+-pls+madonna"
        return 1
      fi
    
      outputdir_name=$(echo "$2" | rev | cut -d\/ -f2 | rev)
      mkdir -pv "$outputdir_name"
      cd "$outputdir_name" && wget -r -l1 -H -t1 -nd -N -np -A "$1" -erobots=off "$2"
    }
    
    # }}}
    

### references
- https://www.youtube.com/watch?v=oWRBjLy8B-I
- http://stackoverflow.com/a/18709707

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


