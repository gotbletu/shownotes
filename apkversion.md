# apkversion
display android version requirements of the apk file

tags: android find apk file version system requirements minimum sdk aapt dump

* tutorial video: [Link](https://youtu.be/9QxQmDx1wms)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

### configuration
    vim ~/.zshrc or ~/.bashrc


    # DESC: color code for bash compatible shell
    # LINK: https://wiki.archlinux.org/index.php?title=Bash/Prompt_customization&oldid=419076#List_of_colors_for_prompt_and_Bash
    
    # Reset
    Color_Off='\e[0m'       # Text Reset
    
    # Regular Colors
    Black='\e[0;30m'        # Black
    Red='\e[0;31m'          # Red
    Green='\e[0;32m'        # Green
    Yellow='\e[0;33m'       # Yellow
    Blue='\e[0;34m'         # Blue
    Purple='\e[0;35m'       # Purple
    Cyan='\e[0;36m'         # Cyan
    White='\e[0;37m'        # White
    
    # https://stackoverflow.com/questions/6289149/read-the-package-name-of-an-android-apk
    # https://stackoverflow.com/questions/8300822/android-how-to-find-which-platform-version-an-apk-targets
    alias aapt="/opt/android-sdk/build-tools/28.0.3/aapt"
    apkversion() {
      if [ $# -lt 1 ]; then
        echo -e "display android version requirements of the apk file"
        echo -e "\nUsage: $0 <filename>"
        echo -e "\nExample:\n$0 file.apk"
        echo -e "$0 file1.apk file2.apk file3.apk"
        echo -e "$0 *.apk"
        echo -e "\nrequirement:\nhttps://aur.archlinux.org/packages/android-sdk-build-tools/"
        echo -e "https://developer.android.com/studio/releases/build-tools"
        return 1
      fi
      myArray=( "$@" )
      for arg in "${myArray[@]}"; do
        sdkVersion=$(aapt dump badging "$arg" | grep sdkVersion)
        targetSdkVersion=$(aapt dump badging "$arg" | grep targetSdkVersion)
        packageinfo=$(aapt dump badging "$arg" | grep package)
        packagename=$(aapt dump badging "$arg" | grep application-label:)
    
        # Chart https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels
    
        echo -e "${Red}$arg${Color_Off} \n-- $packagename \n-- $packageinfo"
    
        if [ "$sdkVersion" = "sdkVersion:'28'" ] ; then echo "-- sdkVersion:'28' = Android 9 (P)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'27'" ] ; then echo "-- sdkVersion:'27' = Android 8.1 (O_MR1)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'26'" ] ; then echo "-- sdkVersion:'26' = Android 8.0 (O)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'25'" ] ; then echo "-- sdkVersion:'25' = Android 7.1, 7.1.1 (N_MR1)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'24'" ] ; then echo "-- sdkVersion:'24' = Android 7.0 (N)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'23'" ] ; then echo "-- sdkVersion:'23' = Android 6.0 (M)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'22'" ] ; then echo "-- sdkVersion:'22' = Android 5.1 (LOLLIPOP_MR1)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'21'" ] ; then echo "-- sdkVersion:'21' = Android 5.0 (LOLLIPOP)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'20'" ] ; then echo "-- sdkVersion:'20' = Android 4.4W (KITKAT_WATCH)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'19'" ] ; then echo "-- sdkVersion:'19' = Android 4.4 (KITKAT)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'18'" ] ; then echo "-- sdkVersion:'18' = Android 4.3 (JELLY_BEAN_MR2)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'17'" ] ; then echo "-- sdkVersion:'17' = Android 4.2, 4.2.2 (JELLY_BEAN_MR1)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'16'" ] ; then echo "-- sdkVersion:'16' = Android 4.1, 4.1.1 (JELLY_BEAN)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'15'" ] ; then echo "-- sdkVersion:'15' = Android 4.0.3, 4.0.4 (ICE_CREAM_SANDWICH_MR1)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'14'" ] ; then echo "-- sdkVersion:'14' = Android 4.0, 4.0.1, 4.0.2 (ICE_CREAM_SANDWICH)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'13'" ] ; then echo "-- sdkVersion:'13' = Android 3.2 (HONEYCOMB_MR2)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'12'" ] ; then echo "-- sdkVersion:'12' = Android 3.1.x (HONEYCOMB_MR1)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'11'" ] ; then echo "-- sdkVersion:'11' = Android 3.0.x (HONEYCOMB)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'10'" ] ; then echo "-- sdkVersion:'10' = Android 2.3.3, 2.3.4 (GINGERBREAD_MR1)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'9'" ] ;  then echo "-- sdkVersion:'9'  = Android 2.3, 2.3.1, 2.3.2 (GINGERBREAD)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'8'" ] ;  then echo "-- sdkVersion:'8'  = Android 2.2.x (FROYO)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'7'" ] ;  then echo "-- sdkVersion:'7'  = Android 2.1.x (ECLAIR_MR1)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'6'" ] ;  then echo "-- sdkVersion:'6'  = Android 2.0.1 (ECLAIR_0_1)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'5'" ] ;  then echo "-- sdkVersion:'5'  = Android 2.0 (ECLAIR)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'4'" ] ;  then echo "-- sdkVersion:'4'  = Android 1.6 (DONUT)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'3'" ] ;  then echo "-- sdkVersion:'3'  = Android 1.5 (CUPCAKE)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'2'" ] ;  then echo "-- sdkVersion:'2'  = Android 1.1 (BASE_1_1)" ; fi
        if [ "$sdkVersion" = "sdkVersion:'1'" ] ;  then echo "-- sdkVersion:'1'  = Android 1.0 (BASE)" ; fi
    
        if [ "$targetSdkVersion" = "targetSdkVersion:'28'" ] ; then echo "-- targetSdkVersion:'28' = Android 9 (P)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'27'" ] ; then echo "-- targetSdkVersion:'27' = Android 8.1 (O_MR1)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'26'" ] ; then echo "-- targetSdkVersion:'26' = Android 8.0 (O)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'25'" ] ; then echo "-- targetSdkVersion:'25' = Android 7.1, 7.1.1 (N_MR1)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'24'" ] ; then echo "-- targetSdkVersion:'24' = Android 7.0 (N)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'23'" ] ; then echo "-- targetSdkVersion:'23' = Android 6.0 (M)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'22'" ] ; then echo "-- targetSdkVersion:'22' = Android 5.1 (LOLLIPOP_MR1)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'21'" ] ; then echo "-- targetSdkVersion:'21' = Android 5.0 (LOLLIPOP)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'20'" ] ; then echo "-- targetSdkVersion:'20' = Android 4.4W (KITKAT_WATCH)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'19'" ] ; then echo "-- targetSdkVersion:'19' = Android 4.4 (KITKAT)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'18'" ] ; then echo "-- targetSdkVersion:'18' = Android 4.3 (JELLY_BEAN_MR2)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'17'" ] ; then echo "-- targetSdkVersion:'17' = Android 4.2, 4.2.2 (JELLY_BEAN_MR1)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'16'" ] ; then echo "-- targetSdkVersion:'16' = Android 4.1, 4.1.1 (JELLY_BEAN)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'15'" ] ; then echo "-- targetSdkVersion:'15' = Android 4.0.3, 4.0.4 (ICE_CREAM_SANDWICH_MR1)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'14'" ] ; then echo "-- targetSdkVersion:'14' = Android 4.0, 4.0.1, 4.0.2 (ICE_CREAM_SANDWICH)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'13'" ] ; then echo "-- targetSdkVersion:'13' = Android 3.2 (HONEYCOMB_MR2)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'12'" ] ; then echo "-- targetSdkVersion:'12' = Android 3.1.x (HONEYCOMB_MR1)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'11'" ] ; then echo "-- targetSdkVersion:'11' = Android 3.0.x (HONEYCOMB)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'10'" ] ; then echo "-- targetSdkVersion:'10' = Android 2.3.3, 2.3.4 (GINGERBREAD_MR1)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'9'" ] ;  then echo "-- targetSdkVersion:'9'  = Android 2.3, 2.3.1, 2.3.2 (GINGERBREAD)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'8'" ] ;  then echo "-- targetSdkVersion:'8'  = Android 2.2.x (FROYO)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'7'" ] ;  then echo "-- targetSdkVersion:'7'  = Android 2.1.x (ECLAIR_MR1)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'6'" ] ;  then echo "-- targetSdkVersion:'6'  = Android 2.0.1 (ECLAIR_0_1)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'5'" ] ;  then echo "-- targetSdkVersion:'5'  = Android 2.0 (ECLAIR)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'4'" ] ;  then echo "-- targetSdkVersion:'4'  = Android 1.6 (DONUT)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'3'" ] ;  then echo "-- targetSdkVersion:'3'  = Android 1.5 (CUPCAKE)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'2'" ] ;  then echo "-- targetSdkVersion:'2'  = Android 1.1 (BASE_1_1)" ; fi
        if [ "$targetSdkVersion" = "targetSdkVersion:'1'" ] ;  then echo "-- targetSdkVersion:'1'  = Android 1.0 (BASE)" ; fi
    
      done
    }
    
### contact

                 _   _     _      _         
      __ _  ___ | |_| |__ | | ___| |_ _   _ 
     / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
    | (_| | (_) | |_| |_) | |  __/ |_| |_| |
     \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
     |___/                                  

- http://www.youtube.com/user/gotbletu
- https://twitter.com/gotbletu
- https://github.com/gotbletu
- gotbletu@gmail.com


