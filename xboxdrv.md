# Xboxdrv
xboxdrv  is  a  driver  for  Xbox  and Xbox360 gamepads. It works by reading the raw data from the controller with the userspace library libusb and then passes the interpreted data to the kernel via uinput. This allows xboxdrv to provide regular joystick and event devices, which makes it compatible with all Linux software.
* tutorial video: [Link](https://www.youtube.com/watch?v=JfcSMRooHLU)
* offical website: [Link](http://pingus.seul.org/~grumbel/xboxdrv/)

### hardware requirements
    xbox 360 wireless controller
    xbox 360 wireless gaming receiver (support up to 4 controllers)
    
    Note: if you want to see a list of other supported devices
    xboxdrv --list-supported-devices 

### install requirements
    xboxdrv

### uninstall requirements
    xf86-input-joystick
    
    (might also be called: xserver-xorg-input-joystick )
    
    Note: uninstall this because we want to disable the joystick from moving the mouse cursor

### disable services
    sudo vim /etc/modprobe.d/blacklist.conf
   

    blacklist xpad
    
    Note: add that line into the conf file to disable xpad so it will not interfere with the xbox controller

### configuration
    sudo vim /etc/default/xboxdrv


    [xboxdrv]
    silent = true
    
    # controller 1
    trigger-as-button = true
    dpad-as-button = true
    deadzone = 4000
    
    # controller 2
    next-controller = true
    trigger-as-button = true
    dpad-as-button = true
    deadzone = 4000
    
    # controller 3
    next-controller = true
    trigger-as-button = true
    dpad-as-button = true
    deadzone = 4000
    
    # controller 4
    next-controller = true
    trigger-as-button = true
    dpad-as-button = true
    deadzone = 4000
    
    [xboxdrv-daemon]
    dbus = disabled


### start services
    sudo systemctl enable xboxdrv.service
    sudo systemctl start xboxdrv.service

    Note: just to be sure restart your computer to apply all the changes
    
### extra information
    The Xbox 360 controller does not have an "off" button
    It will auto shutoff when it idles for about 5-10mins
    To turn it on just hold the middle Xbox logo button

### references
https://www.lumalab.net/index/trans/en/page/post/t/266/f/7/#0

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


