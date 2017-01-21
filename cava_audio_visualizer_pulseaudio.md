# Cava v0.4+ Audio Visualizer - PulseAudio Setup
* tutorial video: [Link](https://www.youtube.com/watch?v=ud_8Up2E_PE)
* offical website: [Link](https://github.com/karlstav/cava)

### install requirements
    cava pulseaudio

### list pulseaudio sources

    pacmd list-sources | awk '/index:/ ||/name:/ || /device.description/'


    # example output:
    index: 4
        name: <alsa_input.usb-NA_Lenovo_Wireless_Headset_W770-00.analog-mono>
                device.description = "Lenovo Wireless Headset W770 Analog Mono"
    index: 5
        name: <alsa_output.pci-0000_00_14.2.analog-stereo.monitor>
                device.description = "Monitor of Built-in Audio Analog Stereo"


### configuration
    vim ~/.config/cava/config
    

    # you can use the index number or by name for the source
    method = pulse
    source = alsa_output.pci-0000_00_14.2.analog-stereo.monitor
    ; source = 5

### references
- https://www.youtube.com/watch?v=ud_8Up2E_PE
- https://github.com/karlstav/cava

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


