# rDesktop: Remote Desktop into Windows Operating system

## On Windows XP Machine

### 1. Enable Windows Remote Desktop ( Windows XP )
- Right Click "My Computer" > Properties > Remote
- Checkmark "Allow users to connect remotely to this computer"
- Select Remote Users > Add > Advanced > Find Now
- Select a user and hit OK to exit

### 2. Get ip address using command prompt ( Windows XP )
- Win+R > type cmd > $ ipconfig

	ex: 192.168.1.105
	default port is: 3389


## On Windows 7 Machine

### 1. Enable Windows Remote Desktop ( Windows 7 )
- Start > Right Click "Computer" > Properties > Remote Settings
- Checkmark "Allow connections from computers...(less secure)"
- Select Users > Add > Advanced > Find Now
- Select a user and hit OK to exit



## On Linux Machine

### 1. install
- $ sudo apt-get install rdesktop
- $ sudo pacman -S rdesktop

### 2. Useage
- $ rdesktop -u administrator -g 1920x1040 192.168.1.105
- $ rdesktop -u administrator -g 1920x1040 192.168.1.105:3389
	+ take 40px off the height to fit the taskbar
- $ rdesktop -u heoyea -g 100% 192.168.1.105:3389
- $ rdesktop -u heoyea -g 100% 192.168.1.105:3389 -r sound:local
	+ redirect sound (not working)
- toggle fullscreen: Ctrl+Alt+Enter
	+ this will give you the taskbar in windows
