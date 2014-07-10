# xrdp - remote desktop protocol server

- http://askubuntu.com/a/289672
- http://ozkaya84.wordpress.com/2013/03/30/remote-desktop-to-linux-servers/
- http://c-nergy.be/blog/?p=4448
- http://www.linuxplanet.com/linuxplanet/tutorials/7249/1
- http://www.humans-enabled.com/2013/02/how-to-install-xrdp-on-ubuntu-1204.html

## 1. install require packages

    xrdp

## 2. configuration

    nano ~/.xsession

    # add in the session for your desktop
    gnome-session --session=gnome-fallback
    gnome-session --session=ubuntu-2d
    mate-session
    xfce4-session
    openbox-session
    startlxde
    startkde
    startxfce4
    cinnamon

## 3. change port (optional)

    sudo nano /etc/xrdp/xrdp.ini
    
- default port: 3389 (TCP)
- open ports on firewall/router if needed
- restart services

## 4. enable xrdp server

    # debian/ubuntu
    sudo service xrdp start

    # systemd
    sudo systemctl enable xrdp
    sudo systemctl start xrdp
     
    # fedora
    http://www.scottalanmiller.com/linux/2013/08/18/installing-xrdp-on-fedora-19/
    
    sudo systemctl enable xrdp
    sudo systemctl start xrdp
    sudo systemctl enable xrdp-sesman
    sudo systemctl start xrdp-sesman
    sudo firewall-cmd --permanent --add-port=3389/tcp

## 5. find ip and username

    # find local ip
    ip a
    
    # find external ip (real ip)
    curl ifconfig.me
    
    # find username
    whoami
    

## 6. Test it out

### On Windows Machine
use windows remote desktop

### On Linux Machine

    rdesktop 192.168.1.XXX
    rdesktop -u username -g 90% 192.168.1.XXX

- rdesktop tutorial: https://www.youtube.com/watch?v=460l2ZN_WQY
