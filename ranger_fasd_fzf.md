# Ranger Open File and Folder Quicker with Fasd
Fasd is a program to open commonly used directory and files quicker.
Ranger is a great file manager, but now we can combine the two to be even more powerful.

* tutorial video: [Link](https://www.youtube.com/watch?v=V9T2G7eGzgc)
* offical website: [Link](https://github.com/clvv/fasd)

### install requirements
    ranger fasd fzf

### what is fasd?

https://www.youtube.com/watch?v=ur81Y-mV5Us

### keybinding
    vim ~/.config/ranger/rc.conf
    
    
    map zz   fzf_fasd
    map zo   console fasd%space

### commands
    vim ~/.config/ranger/commands.py
    

    # fzf_fasd - Fasd + Fzf + Ranger (Interactive Style)
    class fzf_fasd(Command):
        """
        :fzf_fasd
    
        Jump to a file or folder using Fasd and fzf
    
        URL: https://github.com/clvv/fasd
        URL: https://github.com/junegunn/fzf
        """
        def execute(self):
            import subprocess
            if self.quantifier:
                command="fasd | fzf -e -i --tac --no-sort | awk '{ print substr($0, index($0,$2)) }'"
            else:
                command="fasd | fzf -e -i --tac --no-sort | awk '{ print substr($0, index($0,$2)) }'"
            fzf = self.fm.execute_command(command, stdout=subprocess.PIPE)
            stdout, stderr = fzf.communicate()
            if fzf.returncode == 0:
                fzf_file = os.path.abspath(stdout.decode('utf-8').rstrip('\n'))
                if os.path.isdir(fzf_file):
                    self.fm.cd(fzf_file)
                else:
                    self.fm.select_file(fzf_file)
    
    # Fasd with ranger (Command Line Style)
    # https://github.com/ranger/ranger/wiki/Commands
    class fasd(Command):
        """
        :fasd
    
        Jump to directory using fasd
        URL: https://github.com/clvv/fasd
        """
        def execute(self):
            import subprocess
            arg = self.rest(1)
            if arg:
                directory = subprocess.check_output(["fasd", "-d"]+arg.split(), universal_newlines=True).strip()
                self.fm.cd(directory)



### references
- https://www.youtube.com/watch?v=V9T2G7eGzgc
- fasd from cli: https://www.youtube.com/watch?v=ur81Y-mV5Us
- [fzf playlist](https://www.youtube.com/playlist?list=PLqv94xWU9zZ2fMsMMDF4PjtNHCeBFbggD)
- [ranger playlist](https://www.youtube.com/playlist?list=PLqv94xWU9zZ18QJz2Ev8mSeHlICJbejzK)
- https://github.com/ranger/ranger/wiki/Custom-Commands
- https://github.com/clvv/fasd
- https://github.com/junegunn/fzf

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


