# Ranger File Manager - Find and Locate using Fuzzy Finder (fzf)
* tutorial video: [Link](https://www.youtube.com/watch?v=C64LKCZFzME)
* offical website: [Link](https://www.youtube.com/user/gotbletu)

### install requirements
    ranger fzf findutils mlocate

### configuration
    vim ~/.config/ranger/commands.py
    
    
    
    # https://github.com/ranger/ranger/wiki/Integrating-File-Search-with-fzf
    # Now, simply bind this function to a key, by adding this to your ~/.config/ranger/rc.conf: map <C-f> fzf_select
    class fzf_select(Command):
        """
        :fzf_select
    
        Find a file using fzf.
    
        With a prefix argument select only directories.
    
        See: https://github.com/junegunn/fzf
        """
        def execute(self):
            import subprocess
            if self.quantifier:
                # match only directories
                command="find -L . \( -path '*/\.*' -o -fstype 'dev' -o -fstype 'proc' \) -prune \
                -o -type d -print 2> /dev/null | sed 1d | cut -b3- | fzf +m"
            else:
                # match files and directories
                command="find -L . \( -path '*/\.*' -o -fstype 'dev' -o -fstype 'proc' \) -prune \
                -o -print 2> /dev/null | sed 1d | cut -b3- | fzf +m"
            fzf = self.fm.execute_command(command, stdout=subprocess.PIPE)
            stdout, stderr = fzf.communicate()
            if fzf.returncode == 0:
                fzf_file = os.path.abspath(stdout.decode('utf-8').rstrip('\n'))
                if os.path.isdir(fzf_file):
                    self.fm.cd(fzf_file)
                else:
                    self.fm.select_file(fzf_file)
    # fzf_locate
    class fzf_locate(Command):
        """
        :fzf_locate
    
        Find a file using fzf.
    
        With a prefix argument select only directories.
    
        See: https://github.com/junegunn/fzf
        """
        def execute(self):
            import subprocess
            if self.quantifier:
                command="locate home media | fzf -e -i"
            else:
                command="locate home media | fzf -e -i"
            fzf = self.fm.execute_command(command, stdout=subprocess.PIPE)
            stdout, stderr = fzf.communicate()
            if fzf.returncode == 0:
                fzf_file = os.path.abspath(stdout.decode('utf-8').rstrip('\n'))
                if os.path.isdir(fzf_file):
                    self.fm.cd(fzf_file)
                else:
                    self.fm.select_file(fzf_file)

### hotkey mapping
    vim ~/.config/ranger/rc.conf
    


    map <C-f> fzf_select
    map <C-g> fzf_locate

### to include /media to the locate command database

    sudo vim /etc/updatedb.conf
    
    >>> remove /media from PRUNEPATHS
    >>> save and exit
    

    # refresh database
    sudo updatedb

### extra info

    From the Ranger man page :
    
    map key command
    Assign the key combination to the given command. Whenever you type
    the key/keys, the command will be executed. Additionally, if you use
    a quantifier when typing the key, like 5j, it will be passed to the
    command as the attribute "self.quantifier".
    
    In our case the quantifier is any key before pressing the fzf_select keybinding


### references
- https://www.youtube.com/watch?v=C64LKCZFzME
- http://ranger.nongnu.org/
- https://github.com/junegunn/fzf
- https://github.com/ranger/ranger/wiki/Integrating-File-Search-with-fzf
- fzf playlist: https://www.youtube.com/playlist?list=PLqv94xWU9zZ2fMsMMDF4PjtNHCeBFbggD
- ranger playlist: https://www.youtube.com/playlist?list=PLqv94xWU9zZ18QJz2Ev8mSeHlICJbejzK
- rofi playlist: https://www.youtube.com/playlist?list=PLqv94xWU9zZ0LVP1SEFQsLEYjZC_SUB3m

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


