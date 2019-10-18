# Loudness Equalizer aka Pulseaudio Dynamic Range Compression (LADSPA swh-plugins)
Dynamic range compression (DRC) or simply compression reduces the volume of loud sounds or amplifies quiet sounds by narrowing or "compressing" an audio signal's dynamic range. Compression is commonly used in sound recording and reproduction and broadcasting and on instrument amplifiers.
Audio compression reduces loud sounds which are above a certain threshold while quiet sounds remain unaffected. The dedicated electronic hardware unit or audio software used to apply compression is called a compressor. In recorded and live music, compression parameters may be adjusted by an audio engineer to change the way the effect sounds.

common names: audio compressor, automatic gain control, volume normalization, sound normalizer, loudness equalization, loudness equalizer

* tutorial video: [Link](https://www.youtube.com/watch?v=NXE-kSrhk_w) | [Update v2](https://www.youtube.com/watch?v=typM_AQUzi4)
* offical website: [Link](http://plugin.org.uk/)

### install requirements
----
    pulseaudio
    swh-plugins               # might also be called ladspa-swh-plugins
    pavucontrol or ncpamixer  # pavucontrol = GUI, ncpamixer = TUI
----

### list all audio
    $ pacmd list-sinks | awk '/index/ || /name:/ || /alsa.card_name/ || /device.description/'
    

       index: 0
           name: <alsa_output.pci-0000_01_00.1.hdmi-stereo>
                   alsa.card_name = "HDA NVidia"
                   device.description = "High Definition Audio Controller Digital Stereo (HDMI)"
       index: 1
           name: <alsa_output.usb-NA_Lenovo_Wireless_Headset_W770-00.analog-stereo>
                   alsa.card_name = "Lenovo Wireless Headset W770"
                   device.description = "Lenovo Wireless Headset W770 Analog Stereo"
       index: 2
          name: <alsa_output.pci-0000_00_14.2.analog-stereo>
                  alsa.card_name = "HDA ATI SB"
                  device.description = "Built-in Audio Analog Stereo"
       index: 3
          name: <compressor-mono>
                device.description = "LADSPA Plugin SC4 mono on Built-in Audio Analog Stereo"
     * index: 4
          name: <compressor-stereo>
                  device.description = "LADSPA Plugin SC4 on Built-in Audio Analog Stereo"


### add to autostart
----
    $ sudo nano /etc/pulse/default.pa
   

    ### Pulseaudio Dynamic Range Compression (LADSPA swh-plugins)
    
    # set primary audio as default
    # Note: We want primary audio first then switch to compressor audio at the end to avoid
    #         having no sound on bootup. Use the command to see your audio list.
    #         $ pacmd list-sinks | awk '/index/ || /name:/ || /alsa.card_name/ || /device.description/'
    #
    #         e.g mine is:  set-default-sink alsa_output.pci-0000_00_14.2.analog-stereo 
    #
    set-default-sink [your_primary_audio_here]
    
    ## load ladspa module
    .ifexists module-ladspa-sink.so
    .nofail
    # mono
    # load-module module-ladspa-sink sink_name=compressor-mono plugin=sc4m_1916 label=sc4m control=1,1.5,401,-30,20,5,12
    # stereo
    load-module module-ladspa-sink sink_name=compressor-stereo plugin=sc4_1882 label=sc4 control=1,1.5,401,-30,20,5,12
    .fail
    .endif

    # set our custom compressor audio as default
    set-default-sink compressor-stereo
----
----
    ## restart pulseaudio
    $ pulseaudio --kill && pulseaudio --start
----
- then play some music/video
- open pavucontrol or ncpamixer and change the stream if you need


### Pulseaudio 12 Bug Fix
- source: https://bugs.freedesktop.org/show_bug.cgi?id=107078
- Note: only do this if the swh-plugin does not load on pulseaudio 12
----
    ## symlink ladspa libraries to pulseaudio (via GNU Stow)
    cd /usr/lib64/ladspa/ && sudo stow -v -R -t /usr/lib64/pulseaudio . && pulseaudio --kill && pulseaudio --start
----



### references
- Update v2 https://www.youtube.com/watch?v=typM_AQUzi4
- [Axel Werner DRC Stereo](https://awerner.myhome-server.de/doku.php?id=it-artikel:linux:how-to-enable-audio-normalization-a.k.a.-audio-compression-a.k.a.-audio-dynamic-range-compression-under-linux)
- [Daniele T found the pulseaudio 12 fix](https://www.youtube.com/user/damnischannel)
- pulseaudio 12 bug https://bugs.freedesktop.org/show_bug.cgi?id=107078
- http://askubuntu.com/a/44012
- http://askubuntu.com/a/44151
- http://plugin.org.uk/ladspa-swh/docs/ladspa-swh.html#tth_sEc2.92
- https://en.wikipedia.org/wiki/Dynamic_range_compression
- Pulseaudio DRC mono https://www.youtube.com/watch?v=NXE-kSrhk_w
- how to use ncpamixer https://www.youtube.com/watch?v=EVaUXlw4oaQ

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

