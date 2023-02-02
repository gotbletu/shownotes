# PODMAN
* tutorial video: [Link](https://youtu.be/NAvxX9RWLB4)
* offical website: [Link](https://podman.io/)

### What is Podman?
Podman is a daemonless, open source, Linux native tool designed to make it easy to find, run, build, share and deploy applications using Open Containers Initiative (OCI) Containers and Container Images. Podman provides a command line interface (CLI) familiar to anyone who has used the Docker Container Engine. Most users can simply alias Docker to Podman (alias docker=podman) without any problems. Similar to other common Container Engines (Docker, CRI-O, containerd), Podman relies on an OCI compliant Container Runtime (runc, crun, runv, etc) to interface with the operating system and create the running containers. This makes the running containers created by Podman nearly indistinguishable from those created by any other common container engine.

### install requirements
    podman

### commands used
    # enable search results using podman
    sudo vim /etc/containers/registries.conf
    unqualified-search-registries = ["registry.fedoraproject.org", "registry.access.redhat.com", "quay.io", "registry.redhat.io", "docker.io"]
    
    # get id
    id
    
    # show local ip address
    ip a
    
    # list timezone
    timedatectl list-timezones
    
    # https://hub.docker.com/r/linuxserver/freshrss
    mkdir -vp /media/alfa/freshrss
    podman run -d \
      --name=freshrss \
      -e PUID=1000 \
      -e PGID=1000 \
      -e TZ=America/Los_Angeles \
      -p 49160:80 \
      -v /media/alfa/freshrss:/config \
      --restart unless-stopped \
      lscr.io/linuxserver/freshrss:latest
    mkdir -vp ~/.config/systemd/user/
    podman generate systemd freshrss > ~/.config/systemd/user/container-freshrss.service
    systemctl enable --user container-freshrss.service
    
    # autostart podman container at boot without login
    loginctl enable-linger $USER
    
    # list containers
    podman ps
    podman ps -a
    
    # update
    podman stop freshrss
    podman rm freshrss
    podman pull lscr.io/linuxserver/freshrss:latest

### port rules
    - System Ports (0-1023): Avoid standard ports, it is used by many common services.
    - User Ports (1024-49151): Avoid IANA reserve ports for applications.
    - Dynamic and/or Private Ports (49152-65535): Ideal for custom port numbers.


### references
- https://youtu.be/NAvxX9RWLB4
- https://hub.docker.com/r/linuxserver/freshrss
- https://podman.io/

### contact

                 _   _     _      _         
      __ _  ___ | |_| |__ | | ___| |_ _   _ 
     / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
    | (_| | (_) | |_| |_) | |  __/ |_| |_| |
     \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
     |___/                                  

- http://www.youtube.com/user/gotbletu
- https://odysee.com/@gotbletu
- https://twitter.com/gotbletu
- https://github.com/gotbletu
- gotbletu@gmail.com

