# ViFM as a Rsync Frontend

ViFM and rsync to handle the data transfer, Watch and Task-spooler as a queue and monitor when the job completes

* tutorial video: [Link](https://www.youtube.com/watch?v=zrBUZ2g5_O4)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

### install requirements
    vifm rsync watch task-spooler

    note: the package name might be called tsp or ts or task-spooler

### configuration
    vim ~/.vifm/vifmrc


    " copy files to the opposite pane (using rsync)
    nmap ry :!tsp rsync -a %f %D<cr>
    
    " move files to the opposite pane (using rsync)
    nmap rd :!tsp rsync -a --remove-source-files %f %D && tsp find %f -type d -empty -exec rmdir {} \; && tsp rmdir %f<cr>

### related videos
vifm tutorial
https://www.youtube.com/watch?v=qPg7m90WXMo

rsync tutorial
https://www.youtube.com/watch?v=a2Kvj9ff8Qk

watch tutorial
https://www.youtube.com/watch?v=39rzNcqNq1E

task-spooler tutorial
https://www.youtube.com/watch?v=wv8D8wT20ZY

sshfs tutorial
https://www.youtube.com/watch?v=QWQPL4NfjBM

debtap tutorial
https://www.youtube.com/watch?v=3ZvjXnI_eTU


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


