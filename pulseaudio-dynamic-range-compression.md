# Pulseaudio Dynamic Range Compression (LADSPA swh-plugins)
Dynamic range compression (DRC) or simply compression reduces the volume of loud sounds or amplifies quiet sounds by narrowing or "compressing" an audio signal's dynamic range. Compression is commonly used in sound recording and reproduction and broadcasting[1] and on instrument amplifiers.
Audio compression reduces loud sounds which are above a certain threshold while quiet sounds remain unaffected. The dedicated electronic hardware unit or audio software used to apply compression is called a compressor. In recorded and live music, compression parameters may be adjusted by an audio engineer to change the way the effect sounds.

common names: audio compressor, automatic gain control, volume normalization

* tutorial video: [Link](https://www.youtube.com/watch?v=NXE-kSrhk_w)
* offical website: [Link](http://plugin.org.uk/)

### install requirements
    pulseaudio
    pavucontrol
    swh-plugins   # might also be called ladspa-swh-plugins

### autostart
    sudo nano /etc/pulse/default.pa
    
    .ifexists module-ladspa-sink.so
    .nofail
    load-module module-ladspa-sink sink_name=compressor plugin=sc4m_1916 label=sc4m control=1,1.5,401,-30,20,5,12
    .fail
    .endif


- reboot
- then play some music/video
- open pavucontrol and change the stream to the LADSPA compressor

### references
- http://askubuntu.com/a/44012
- http://askubuntu.com/a/44151
- http://plugin.org.uk/ladspa-swh/docs/ladspa-swh.html#tth_sEc2.92
- https://www.bfccomputing.com/dynamic-range-compression-for-pulseaudio/
- https://en.wikipedia.org/wiki/Dynamic_range_compression

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



