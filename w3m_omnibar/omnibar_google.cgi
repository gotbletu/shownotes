#!/usr/bin/env sh
# AUTHOR: gotbletu (@gmail|twitter|youtube|github|lbry|odysee)
#         https://www.youtube.com/user/gotbletu
# DESC:   use the address bar to do search engine searches
# DEMO:   https://youtu.be/77qhjaoj_2k
# REQD:   1. chmod +x ~/.w3m/cgi-bin/omnibar_google.cgi
#         2. sed -i 's@^cgi_bin.*@cgi_bin ~/.w3m/cgi-bin:/usr/lib/w3m/cgi-bin:/usr/local/libexec/w3m/cgi-bin@g' ~/.w3m/config
#         3. sed -i 's@^use_dictcommand.*@use_dictcommand 1@g' ~/.w3m/config
#         4. $EDITOR ~/.w3m/keymap
#            ############################ Execute omnibar command (DICT_WORD)
#            keymap  sg      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_google.cgi ; DICT_WORD"
#            ############################ Execute omnibar command for word at cursor (DICT_WORD_AT)
#            keymap  sG      COMMAND "SET_OPTION dictcommand=file:///cgi-bin/omnibar_google.cgi ; DICT_WORD_AT"

echo "w3m-control: BACK"
echo "w3m-control: TAB_GOTO https://www.google.com/search?q=$QUERY_STRING"
