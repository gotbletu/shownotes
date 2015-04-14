Notes for video: https://www.youtube.com/watch?v=g31cCEervTw


## 1. requirements (depends on what u using)
* python2-pip (needed to install using pip)
* flexget (sudo pip2 install flexget==1.2.128)
* any torrent client you want to use

## 2. commands used
    # help page
    flexget movie-queue -h
    flexget movie-queue list -h
    # add to queue
    flexget movie-queue add "TITLE of MOVIE"
    # remove from queue
    flexget movie-queue del <id> 
    # list waiting and downloaded list
    flexget movie-queue list waiting && flexget movie-queue list waiting
    # check config file
    flexget check

## 3. config (nano ~/.flexget/config.yml)
    tasks:
      movie_queue_release:
        movie_queue: yes
        quality:
          - <=1080p hdrip+
        content_size:
          min: 400
          max: 2800
          strict: no
        download: ~/Downloads/
        verify_ssl_certificates: no
        inputs:
          - rss: https://torrentz.eu/feed_verified?q=movies
          - rss: https://kickass.so/usearch/seeds%3A100%20is_safe%3A1%20verified%3A1%20category%3Amovies/?rss=1

## 4. cronjob setup (crontab -e)
    @hourly flexget execute --cron

## 5. Links
* how to use pip ( https://www.youtube.com/watch?v=3Mokyx5J2c4 )
* flexget playlist ( https://www.youtube.com/watch?v=T2GJOL4gb20&list=PLqv94xWU9zZ0pVGrgKtMuhFHun8-MahSY )
* http://flexget.com/wiki/Qualities
* http://flexget.com/wiki/Plugins/movie_queue?version=19
