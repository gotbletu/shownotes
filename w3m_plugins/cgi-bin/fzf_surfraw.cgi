#!/usr/bin/env sh
# AUTHOR: gotbletu (@gmail|twitter|youtube|github|lbry)
#         https://www.youtube.com/user/gotbletu
# DESC:   interactive surfraw smart prefix search engine
# DEMO:   https://youtu.be/p5NZb8f8AHA | updated https://youtu.be/0j3pUfZjCeQ
# DEPEND: surfraw fzf gawk coreutils grep
# REQD:   1. chmod +x ~/.w3m/cgi-bin/fzf_surfraw.cgi
#         2. chmod +x ~/.w3m/cgi-bin/goto_w3m_clipboard.cgi
#         3. sed -i 's@cgi_bin.*@cgi_bin ~/.w3m/cgi-bin:/usr/lib/w3m/cgi-bin:/usr/local/libexec/w3m/cgi-bin@g' ~/.w3m/config
#         4. sed -i 's@default_url.*@default_url 1@g' ~/.w3m/config
#         5. $EDITOR ~/.w3m/keymap
#            # search with surfraw (no clipboard required)
#            keymap  xs  COMMAND "READ_SHELL ~/.w3m/cgi-bin/fzf_surfraw.cgi ; BACK ; GOTO file:/cgi-bin/goto_w3m_clipboard.cgi"
#            keymap  XS  COMMAND "READ_SHELL ~/.w3m/cgi-bin/fzf_surfraw.cgi ; BACK ; TAB_GOTO file:/cgi-bin/goto_w3m_clipboard.cgi"

# CLOG:   2021-05-23 detect if tmux is running then use fzf-tmux split pane
#         2021-05-22 fzf --tiebreak to sort, no longer require any clipboard use tmpfile instead
#         2021-04-11 remove read command for posix compatible (good idea by https://github.com/NapoleonWils0n)
#                    new keymap use READ_SHELL and tmux load-buffer to avoid unnecessary prompt
#         2021-02-05 copy to all 3 clipboard at once; xsel primary/system clipboard, tmux clipboard
#         2020-05-08 surfraw -p instead of echo
#         2020-04-27 starting point

# clear screen
printf "\033c"

# check if tmux is running on current window
if [ "$TERM_PROGRAM" = tmux ]; then
  PREFIX=$(surfraw -elvi | grep -v 'LOCAL\|GLOBAL' | fzf-tmux -d 30% -e --prompt='Pick search engine: ' --info=inline --layout=reverse --tiebreak=index | awk '{print $1}')
  [ -z "$PREFIX" ] && exit
  INPUT=$(printf "\n" | fzf-tmux -d 30% --print-query --prompt="Enter keyword(s) to search ${PREFIX}: " --info=inline --layout=reverse)
else
  PREFIX=$(surfraw -elvi | grep -v 'LOCAL\|GLOBAL' | fzf -e --prompt='Pick search engine: ' --info=inline --layout=reverse --tiebreak=index | awk '{print $1}')
  [ -z "$PREFIX" ] && exit
  INPUT=$(printf "\n" | fzf --print-query --prompt="Enter keyword(s) to search ${PREFIX}: " --info=inline --layout=reverse)
fi

# NOTE: dont quote $INPUT it will mess up results
# surfraw -p "$PREFIX" $INPUT | xsel -p                     # xsel primary (aka shift-insert or middle click to paste)
# surfraw -p "$PREFIX" $INPUT | xsel -b                     # xsel system (aka ctrl-v to paste)
# surfraw -p "$PREFIX" $INPUT | tmux load-buffer -
surfraw -p "$PREFIX" $INPUT > /tmp/clipbrd.txt              # clipboard using tmpfile
