#!/usr/bin/env sh
# AUTHOR: gotbletu (@gmail|twitter|youtube|github|lbry|odysee)
#         https://www.youtube.com/user/gotbletu
# DESC:   online dictionary lookup using curl
# DEMO:   https://youtu.be/77qhjaoj_2k
# REQD:   1. chmod +x ~/.w3m/cgi-bin/dictionary.cgi
#         2. sed -i 's@^cgi_bin.*@cgi_bin ~/.w3m/cgi-bin:/usr/lib/w3m/cgi-bin:/usr/local/libexec/w3m/cgi-bin@g' ~/.w3m/config
#         3. sed -i 's@^use_dictcommand.*@use_dictcommand 1@g' ~/.w3m/config
#         4. $EDITOR ~/.w3m/keymap
#            ############################ Execute dictionary command (DICT_WORD)
#            keymap  \\\d    COMMAND "SET_OPTION dictcommand=file:///cgi-bin/dictionary.cgi ; DICT_WORD"
#            ############################ Execute dictionary command for word at cursor (DICT_WORD_AT)
#            keymap  \\\w    COMMAND "SET_OPTION dictcommand=file:///cgi-bin/dictionary.cgi ; DICT_WORD_AT"


echo "w3m-control: READ_SHELL curl -s dict://dict.org/d:$QUERY_STRING"
echo "w3m-control: DELETE_PREVBUF"
echo "w3m-control: REDRAW"
