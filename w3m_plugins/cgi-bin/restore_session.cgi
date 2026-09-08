#!/usr/bin/env sh
# AUTHOR: gotbletu (@gmail|twitter|youtube|github|lbry)
#         https://www.youtube.com/user/gotbletu
# DESC:   generate a script for your last w3m session then you can run script to restore all urls in new tabs
# DEMO:   https://youtu.be/qYhNJ3itqWw
# DEPEND: coreutils gawk sed
# REQD:   1. chmod +x ~/.w3m/cgi-bin/restore_session.cgi 
#         2. $EDITOR ~/.bashrc
#               [ -d "$HOME/.w3m/bin" ] && PATH="$HOME/.w3m/bin:$PATH"
#         3. $EDITOR ~/.w3m/keymap
#             ############################ Quit with confirmation request (QUIT)
#             keymap  :q  QUIT
#             keymap  ZZ  QUIT
#             ############################ Quit at once (EXIT)
#             keymap  ZQ  EXIT
#             ############################ Quit at once and save session
#             keymap  Q       COMMAND     "EXTERN 'echo %s > ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; READ_SHELL ~/.w3m/cgi-bin/restore_session.cgi ; EXIT"
#         4. To load w3m with the last session
#               $ w3mlastsession

# CLOG:   2021-05-15 remove multiple -N flag
#         2021-04-17 first draft, no option to jump to tab 1 at the moment

## ---------------------------------------------
# location of generated script of last session
mkdir -p "$HOME/.w3m/bin"
RESTORE_SESSSION="$HOME/.w3m/bin/w3mlastsession"

# add shell header
echo "#!/usr/bin/env sh" > "$RESTORE_SESSSION"
echo "w3m -N \\" >> "$RESTORE_SESSSION"

# remove dupes without sorting and append trailing slash to each url
awk '!x[$0]++' "$HOME/.w3m/RestoreSession.txt" | while read -r line ; do echo "'$line' \\" >> "$RESTORE_SESSSION" ; done

# remove last trailing slash of the last line
sed -i '$ s-.$--' "$RESTORE_SESSSION"

chmod +x "$RESTORE_SESSSION"

## OUTPUT SCRIPT FILE EXAMPLE ~/.w3m/bin/w3mlastsession
## --------------------------------------------------
##  #!/usr/bin/env sh
##  w3m -N \
##  'https://www.reddit.com/r/w3m/.mobile' \
##  'https://www.reddit.com/r/commandline/.mobile' \
##  'https://www.reddit.com/r/linux/.mobile' \
##  'http://lite.cnn.com/en' \
##  'https://raw.githubusercontent.com/tats/w3m/master/ChangeLog' \
##  'https://github.com/gotbletu/shownotes'
## --------------------------------------------------
