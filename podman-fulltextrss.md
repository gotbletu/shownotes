# Full Text RSS Container
* tutorial video: [Link](https://youtu.be/QE03OcuEBcM)
* offical website: [Link](https://github.com/heussd/fivefilters-full-text-rss-docker)

Extract the full article content from a web page or a summary-only RSS feed.

### install requirements
    podman

### podman cli
    podman run -d \
      --name=fulltextrss \
      -p 49161:80 \
      --restart always \
      docker.io/heussd/fivefilters-full-text-rss:latest
    mkdir -vp ~/.config/systemd/user
    podman generate systemd fulltextrss > ~/.config/systemd/user/container-fulltextrss.service
    systemctl enable --user container-fulltextrss.service

### references
- https://youtu.be/QE03OcuEBcM
- https://github.com/heussd/fivefilters-full-text-rss-docker
- https://github.com/heussd/fivefilters-full-text-rss-docker/blob/master/docker-compose.yml

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

