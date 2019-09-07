# VMPK - Virtual MIDI Piano Keyboard
turn your computer keyboard into a piano keyboard
* tutorial video: [Link](https://www.youtube.com/watch?v=OG-xDIRnLLU)
* offical website: [Link](http://vmpk.sourceforge.net/)

### install requirements
    vmpk fluidsynth qsynth soundfont-fluid

### qsynth settings
    1. start the program
    2. setup > audio > audio driver > [pulseaudio]
    3. setup > MIDI > MIDI Client Name ID > [qsynth]
    4. setup > soundfonts > open > [/usr/share/soundfonts/FluidR3_GM2-2.sf2]
    5. Options > Output peak level meters [Check]
    6. might have to restart the qsynth program
    
### vmpk settings
    1. start the program
    2. edit > midi connections > output midi connections > 
       MIDI OUT Driver: > [ALSA]
       Output MIDI Connection: > [FLUID Synth (qsynth):0] > OK

### references
- http://vmpk.sourceforge.net/
- https://en.wikipedia.org/wiki/Synthesizer


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



