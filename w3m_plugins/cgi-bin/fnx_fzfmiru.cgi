#!/usr/bin/env sh
# AUTHOR: gotbletu (@gmail|twitter|youtube|github|lbry)
#         https://www.youtube.com/user/gotbletu
# DESC:   execute w3m commands via fzf
# DEMO:   https://youtu.be/drzMQuLE4BM
# DEPEND: fzf gawk coreutils
# REFF:   inspired by NapoleonWils0n https://www.youtube.com/watch?v=dyXcYxZOa9M
# REQD:   1. chmod +x ~/.w3m/cgi-bin/fnx_fzfmiru.cgi
#         2. chmod +x ~/.w3m/cgi-bin/fnx_execute.cgi
#         3. sed -i 's@cgi_bin.*@cgi_bin ~/.w3m/cgi-bin:/usr/lib/w3m/cgi-bin:/usr/local/libexec/w3m/cgi-bin@g' ~/.w3m/config
#         4. $EDITOR ~/.w3m/keymap
#            keymap  xx  COMMAND "READ_SHELL ~/.w3m/cgi-bin/fnx_fzfmiru.cgi ; BACK ; GOTO file:/cgi-bin/fnx_execute.cgi ; BACK"

# CLOG:
#         2021-08-02 tmux if statement for popup/split/no terminal

fnx_database() {
# $ = built-in functions ; & = custom ; * = favorites
cat <<EOF
ABORT#@ABORT\$#-- Quit at once
ACCESSKEY#@ACCESSKEY\$#-- Pop up accesskey menu
ADD_BOOKMARK#@ADD_BOOKMARK\$#-- Add current page to bookmarks
ALARM#@ALARM\$#-- Set alarm
BACK#@BACK\$#-- Close current buffer and return to the one below in stack
BEGIN#@BEGIN\$#-- Go to the first line
BOOKMARK#@BOOKMARK\$#-- View bookmarks
CENTER_H#@CENTER_H\$#-- Center on cursor column
CENTER_V#@CENTER_V\$#-- Center on cursor line
CHARSET#@CHARSET\$#-- Change the character encoding for the current document
CLOSE_TAB#@CLOSE_TAB\$#-- Close tab
CLOSE_TAB_MOUSE#@CLOSE_TAB_MOUSE\$#-- Close tab at mouse pointer
COMMAND#@COMMAND\$#-- Invoke w3m function(s)
COOKIE#@COOKIE\$#-- View cookie list
CURSOR_TOP#@CURSOR_TOP\$#-- Move cursor to the top line on the screen
CURSOR_MIDDLE#@CURSOR_MIDDLE\$#-- Move cursor to the middle line on the screen
CURSOR_BOTTOM#@CURSOR_BOTTOM\$#-- Move cursor to the bottom line on the screen
DEFAULT_CHARSET#@DEFAULT_CHARSET\$#-- Change the default character encoding
DEFINE_KEY#@DEFINE_KEY\$#-- Define a binding between a key stroke combination and a command
DELETE_PREVBUF#@DELETE_PREVBUF\$#-- Delete previous buffer (mainly for local CGI-scripts)
DICT_WORD#@DICT_WORD\$#-- Execute dictionary command (see README.dict)
DICT_WORD_AT#@DICT_WORD_AT\$#-- Execute dictionary command for word at cursor
DISPLAY_IMAGE#@DISPLAY_IMAGE\$#-- Restart loading and drawing of images
DOWN#@DOWN\$#-- Scroll the screen down one line
DOWNLOAD#@DOWNLOAD\$#-- Save document source
DOWNLOAD_LIST#@DOWNLOAD_LIST\$#-- Display downloads panel
EDIT#@EDIT\$#-- Edit local source
EDIT_SCREEN#@EDIT_SCREEN\$#-- Edit rendered copy of document
END#@END\$#-- Go to the last line
EXEC_SHELL#@EXEC_SHELL\$#-- Execute shell command and display output
EXIT#@EXIT\$#-- Quit at once
EXTERN#@EXTERN\$#-- Display using an external browser
EXTERN_LINK#@EXTERN_LINK\$#-- Display target using an external browser
FRAME#@FRAME\$#-- Toggle rendering HTML frames
GOTO#@GOTO\$*#-- Open specified document in a new buffer
GOTO_HOME#@GOTO_HOME\$#-- Return to the homepage (specified HTTP_HOME or WWW_HOME variable)
GOTO_LINE#@GOTO_LINE\$#-- Go to the specified line
GOTO_LINK#@GOTO_LINK\$#-- Follow current hyperlink in a new buffer
GOTO_RELATIVE#@GOTO_RELATIVE\$#-- Go to relative address
HELP#@HELP\$#-- Show help panel
HISTORY#@HISTORY\$#-- Show browsing history
INFO#@INFO\$#-- Display information about the current document
INTERRUPT#@INTERRUPT\$#-- Suspend w3m to background
ISEARCH#@ISEARCH\$#-- Incremental search forward
ISEARCH_BACK#@ISEARCH_BACK\$#-- Incremental search backward
LEFT#@LEFT\$#-- Shift screen one column left
LINE_BEGIN#@LINE_BEGIN\$#-- Go to the beginning of the line
LINE_END#@LINE_END\$#-- Go to the end of the line
LINE_INFO#@LINE_INFO\$#-- Display current position in document
LINK_BEGIN#@LINK_BEGIN\$#-- Move to the first hyperlink
LINK_END#@LINK_END\$#-- Move to the last hyperlink
LINK_MENU#@LINK_MENU\$#-- Pop up link element menu
LIST#@LIST\$*#-- Show all URLs referenced
LIST_MENU#@LIST_MENU\$#-- Pop up menu for hyperlinks to browse to
LOAD#@LOAD\$#-- Open local file in a new buffer
MAIN_MENU#@MAIN_MENU\$#-- Pop up menu
MARK#@MARK\$#-- Set/unset mark
MARK_MID#@MARK_MID\$#-- Turn Message-ID-like strings into hyperlinks
MARK_URL#@MARK_URL\$#-- Turn URL-like strings into hyperlinks
MARK_WORD#@MARK_WORD\$#-- Turn current word into hyperlink
MENU#@MENU\$#-- Pop up menu
MENU_MOUSE#@MENU_MOUSE\$#-- Pop up menu at mouse pointer
MOUSE_TOGGLE#@MOUSE_TOGGLE\$#-- Toggle mouse support
MOVE_DOWN#@MOVE_DOWN\$#-- Cursor down
MOVE_DOWN1#@MOVE_DOWN1\$#-- Cursor down. With edge touched, slide
MOVE_LEFT#@MOVE_LEFT\$#-- Cursor left
MOVE_LEFT1#@MOVE_LEFT1\$#-- Cursor left. With edge touched, slide
MOVE_LIST_MENU#@MOVE_LIST_MENU\$*#-- Pop up menu to navigate between hyperlinks
MOVE_MOUSE#@MOVE_MOUSE\$#-- Move cursor to mouse pointer
MOVE_RIGHT#@MOVE_RIGHT\$#-- Cursor right
MOVE_RIGHT1#@MOVE_RIGHT1\$#-- Cursor right. With edge touched, slide
MOVE_UP#@MOVE_UP\$#-- Cursor up
MOVE_UP1#@MOVE_UP1\$#-- Cursor up. With edge touched, slide
MSGS#@MSGS\$#-- Display error messages
NEW_TAB#@NEW_TAB\$#-- Open a new tab (with current document)
NEXT#@NEXT\$#-- Switch to the next buffer
NEXT_DOWN#@NEXT_DOWN\$#-- Move downward to the next hyperlink
NEXT_HALF_PAGE#@NEXT_HALF_PAGE\$#-- Scroll down half a page
NEXT_LEFT#@NEXT_LEFT\$#-- Move left to the next hyperlink
NEXT_LEFT_UP#@NEXT_LEFT_UP\$#-- Move left or upward to the next hyperlink
NEXT_LINK#@NEXT_LINK\$#-- Move to the next hyperlink
NEXT_MARK#@NEXT_MARK\$#-- Go to the next mark
NEXT_PAGE#@NEXT_PAGE\$#-- Scroll down one page
NEXT_RIGHT#@NEXT_RIGHT\$#-- Move right to the next hyperlink
NEXT_RIGHT_DOWN#@NEXT_RIGHT_DOWN\$#-- Move right or downward to the next hyperlink
NEXT_TAB#@NEXT_TAB\$#-- Switch to the next tab
NEXT_UP#@NEXT_UP\$#-- Move upward to the next hyperlink
NEXT_VISITED#@NEXT_VISITED\$#-- Move to the next visited hyperlink
NEXT_WORD#@NEXT_WORD\$#-- Move to the next word
NOTHING#@NOTHING\$#-- Do nothing
NULL#@NULL\$#-- Do nothing
OPTIONS#@OPTIONS\$#-- Display options setting panel
PEEK#@PEEK\$#-- Show current address
PEEK_IMG#@PEEK_IMG\$#-- Show image address
PEEK_LINK#@PEEK_LINK\$#-- Show target address
PIPE_BUF#@PIPE_BUF\$#-- Pipe current buffer through a shell command and display output
PIPE_SHELL#@PIPE_SHELL\$#-- Execute shell command and display output
PREV#@PREV\$#-- Switch to the previous buffer
PREV_HALF_PAGE#@PREV_HALF_PAGE\$#-- Scroll up half a page
PREV_LINK#@PREV_LINK\$#-- Move to the previous hyperlink
PREV_MARK#@PREV_MARK\$#-- Go to the previous mark
PREV_PAGE#@PREV_PAGE\$#-- Scroll up one page
PREV_TAB#@PREV_TAB\$#-- Switch to the previous tab
PREV_VISITED#@PREV_VISITED\$#-- Move to the previous visited hyperlink
PREV_WORD#@PREV_WORD\$#-- Move to the previous word
PRINT#@PRINT\$#-- Save rendered document
QUIT#@QUIT\$#-- Quit with confirmation request
READ_SHELL#@READ_SHELL\$#-- Execute shell command and display output
REDO#@REDO\$#-- Cancel the last undo
REDRAW#@REDRAW\$#-- Draw the screen anew
REG_MARK#@REG_MARK\$#-- Mark all occurences of a pattern
REINIT#@REINIT\$#-- Reload configuration file
RELOAD#@RELOAD\$#-- Load current document anew
RESHAPE#@RESHAPE\$#-- Re-render document
RIGHT#@RIGHT\$#-- Shift screen one column right
SAVE#@SAVE\$#-- Save document source
SAVE_IMAGE#@SAVE_IMAGE\$#-- Save inline image
SAVE_LINK#@SAVE_LINK\$#-- Save hyperlink target
SAVE_SCREEN#@SAVE_SCREEN\$#-- Save rendered document
SEARCH#@SEARCH\$#-- Search forward
SEARCH_BACK#@SEARCH_BACK\$#-- Search backward
SEARCH_FORE#@SEARCH_FORE\$#-- Search forward
SEARCH_NEXT#@SEARCH_NEXT\$#-- Continue search forward
SEARCH_PREV#@SEARCH_PREV\$#-- Continue search backward
SELECT#@SELECT\$#-- Display buffer-stack panel
SELECT_MENU#@SELECT_MENU\$*#-- Pop up buffer-stack menu
SETENV#@SETENV\$#-- Set environment variable
SET_OPTION#@SET_OPTION\$#-- Set option
SHELL#@SHELL\$#-- Execute shell command and display output
SHIFT_LEFT#@SHIFT_LEFT\$#-- Shift screen left
SHIFT_RIGHT#@SHIFT_RIGHT\$#-- Shift screen right
SOURCE#@SOURCE\$#-- Toggle between HTML shown or processed
STOP_IMAGE#@STOP_IMAGE\$#-- Stop loading and drawing of images
SUBMIT#@SUBMIT\$#-- Submit form
SUSPEND#@SUSPEND\$#-- Suspend w3m to background
TAB_GOTO#@TAB_GOTO\$*#-- Open specified document in a new tab
TAB_GOTO_RELATIVE#@TAB_GOTO_RELATIVE\$#-- Open relative address in a new tab
TAB_LEFT#@TAB_LEFT\$#-- Move left along the tab bar
TAB_LINK#@TAB_LINK\$#-- Follow current hyperlink in a new tab
TAB_MENU#@TAB_MENU\$*#-- Pop up tab selection menu
TAB_MOUSE#@TAB_MOUSE\$#-- Select tab by mouse action
TAB_RIGHT#@TAB_RIGHT\$#-- Move right along the tab bar
UNDO#@UNDO\$#-- Cancel the last cursor movement
UP#@UP\$#-- Scroll the screen up one line
VERSION#@VERSION\$#-- Display the version of w3m
VIEW#@VIEW\$#-- Toggle between HTML shown or processed
VIEW_BOOKMARK#@VIEW_BOOKMARK\$#-- View bookmarks
VIEW_IMAGE#@VIEW_IMAGE\$#-- Display image in viewer
WHEREIS#@WHEREIS\$#-- Search forward
WRAP_TOGGLE#@WRAP_TOGGLE\$#-- Toggle wrapping mode in searches
/usr/share/doc/w3m/README#@README_INTRO&#-- Readme intro page
/usr/share/doc/w3m/README.cookie#@README_COOKIE&#-- Readme cookie page
/usr/share/doc/w3m/README.cygwin#@README_CYGWIN&#-- Readme cygwin page
/usr/share/doc/w3m/README.dict#@README_DICT&#-- Readme dictionary page
/usr/share/doc/w3m/README.func#@README_FUNC&#-- Readme function page
/usr/share/doc/w3m/README.img#@README_IMG&#-- Readme inline image page
/usr/share/doc/w3m/README.m17n#@README_M17N&#-- Readme muntilingualizaion page
/usr/share/doc/w3m/README.mouse#@README_MOUSE&#-- Readme mouse page
/usr/share/doc/w3m/README.passwd#@README_PASSWD&#-- Readme password page
/usr/share/doc/w3m/README.pre_form#@README_PRE_FORM&#-- Readme pre-fill form page
/usr/share/doc/w3m/README.siteconf#@README_SITECONF&#-- Readme siteconf page
/usr/share/doc/w3m/README.sixel#@README_SIXEL&#-- Readme sixel image page
/usr/share/doc/w3m/README.tab#@README_TAB&#-- Readme tab browsing page
/usr/share/doc/w3m/FAQ.html#@README_FAQ&#-- Readme FAQ page
/usr/share/doc/w3m/MANUAL.html#@README_MANUAL&#-- Readme manual page
/usr/share/doc/w3m/STORY.html#@README_STORY&#-- Readme story history of W3M page
fn_click_next.cgi#@CLICK_NEXT&#-- Click next page button 'Next'
fn_click_prev.cgi#@CLICK_PREV&#-- Click previous page button 'Previous'
fn_click_next_arrow.cgi#@CLICK_NEXT_ARROW&#-- Click next page button '>'
fn_click_prev_arrow.cgi#@CLICK_PREV_ARROW&#-- Click previous page button '<'
fn_closetab_stash.cgi#@CLOSE_TAB_STASH&#-- Close tab (Stash URL to ~/.w3m/RestoreTab.txt)
fn_dict_curl.cgi#@DICT_WORD_CURL&#-- Online dictionary for word at cursor
fn_display_borders.cgi#@BORDERS&#-- Toggle table boarders
fn_display_image.cgi#@DISPLAY_IMAGE_TOGGLE&#-- Toggle display image
fn_display_link_number.cgi#@LINK_NUMBER&#-- Toggle link number (hinting mode e.g press 3[ to jump to link 3)
fn_edit_bookmark.cgi#@EDIT_BOOKMARK&#-- Edit bookmark
fn_edit_config.cgi#@EDIT_CONFIG&#-- Edit W3M configuration
fn_edit_keymap.cgi#@EDIT_KEYMAP&#-- Edit W3M keymap
fn_edit_mailcap.cgi#@EDIT_MAILCAP&#-- Edit W3M mailcap
fn_edit_menu.cgi#@EDIT_MENU&#-- Edit W3M context menu
fn_edit_restoretab.cgi#@EDIT_RESTORETAB&#-- Edit W3M restoretab ~/.w3m/RestoreTab.txt
fn_edit_searchengine.cgi#@EDIT_SEARCHENGINES&#-- Edit search engine alias ~/.w3m/cgi-bin/search_engines.cgi
fn_edit_siteconf.cgi#@EDIT_SITECONF&#-- Edit W3M siteconf
fn_edit_surfraw.cgi#@EDIT_SURFRAW&#-- Edit surfraw bookmark ~/.surfraw/bookmark
fn_edit_urimethodmap.cgi#@EDIT_URIMETHODMAP&#-- Edit W3M urimethodmap
fn_engine_duckduckgo.cgi#@ENGE_DDG&*#-- Search the web via duckduckgo
fn_engine_geminispace.cgi#@ENGE_GEMSPC&#-- Search gemini capsules via geminispace
fn_engine_google.cgi#@ENGE_GOOGLE&*#-- Search the web via google
fn_engine_invidious.cgi#@ENGE_INVIDIOUS&#-- Search youtube videos via invidious
fn_engine_1337x.cgi#@ENGE_1337X&*#-- Search 1337x for torrents
fn_engine_piratebay.cgi#@ENGE_TPB&*#-- Search piratebay for torrents
fn_engine_nyaasi.cgi#@ENGE_NYAASI&#-- Search nyaa for anime torrents
fn_engine_xdcceu.cgi#@ENGE_XDCCEU&*#-- Search xdcceu for xdcc (irc dcc files)
fn_engine_veronica2.cgi#@ENGE_V2&#-- Search gopherspace via veronica-2
fn_engine_wikipedia.cgi#@ENGE_WIKIPEDIA&#-- Search wikipedia for articles
fn_engine_yahoo.cgi#@ENGE_YAHOO&#-- Search the web via yahoo
fn_engine_commandlinefu.cgi#@ENGE_CMDFU&#-- Search for commandline one liners via commandlinefu
fn_goto_tmux_clipboard.cgi#@GOTO_CLIP_TMUX&&#-- Paste URL and go (via tmux clipboard)
fn_goto_w3m_clipboard.cgi#@GOTO_CLIP_W3M&#-- Paste URL and go (via W3M clipboard /tmp/clipbrd.txt)
fn_goto_x11_clipboard.cgi#@GOTO_CLIP_X11&#-- Paste URL and go (via xsel X11 clipboard)
fn_open_link_in_gui_browser.cgi#@GUI_BROWSER_LINK&#-- Open link at cursor in external browser ($BROWSER)
fn_open_page_in_gui_browser.cgi#@GUI_BROWSER_URL&#-- Open page URL in external browser ($BROWSER)
fn_readerview_rdrview.cgi#@RDRVIEW_RDRVIEW&*#-- Reader view using rdrview (c/c++)
fn_readerview_readable.cgi#@RDRVIEW_READABLE&#-- Reader view using readability-cli (nodejs)
fn_readerview_readability.cgi#@RDRVIEW_READABILITY&#-- Reader view using python-readability-lxml (python3)
fn_restore_tab.cgi#@RESTORE_TAB&#-- Restore tab from ~/.w3m/RestoreTab.txt
fn_show_input_line_editing_mode_key_binding.cgi#@LIST_EDIT_MODE_KEY&#-- Show input editing mode key binding
fn_show_user_defined_key_binding.cgi#@LIST_DEFINED_KEY&*#-- Show user custom key binding
fn_toggle_color.cgi#@COLOR&#-- Toggle color
fn_toggle_line_number.cgi#@LINE_NUMBER&*#-- Toggle line number
fn_treat_url_like_strings.cgi#@TREAT_URL&*#-- Toggle plain text to clickable link
fn_user_agent_clear.cgi#@USER_AGENT_CLEAR&#-- Clear user agent string
fn_user_agent_set.cgi#@USER_AGENT_SET&#-- Set user agent string
fn_yank_current_link.cgi#@YANK_LINK&*#-- Copy link at cursor to clipboard
fn_yank_page_url.cgi#@YANK_URL&*#-- Copy page URL to clipboard
fn_save_session.cgi#@SAVE_SESSION&*#-- Save session and ask to quit (run 'w3mlastsession' command to restore)
fn_tts_espeak_page.cgi#@TTS_ESPEAK_PAGE&*#-- Espeak-ng text to speech whole page (Press Ctrl+C to continue browsing)
fn_tts_espeak_word.cgi#@TTS_ESPEAK_WORD&#-- Espeak-ng text to speech single word
fn_tts_festival_page.cgi#@TTS_FESTIVAL_PAGE&#-- Festival text to speech whole page (Press Ctrl+C to continue browsing)
fn_tts_festival_word.cgi#@TTS_FESTIVAL_WORD&#-- Festival text to speech single word
fn_tts_svoxpico_page.cgi#@TTS_SVOXPICO_PAGE&#-- SVOX Pico text to speech whole page (Press Ctrl+C to continue browsing)
fn_tts_svoxpico_word.cgi#@TTS_SVOXPICO_WORD&#-- SVOX Pico text to speech single word
fn_tts_kill.cgi#@TTS_KILL&*#-- Killall text to speech playback in progress
fn_diana_add.cgi#@DIANA_ADD&*#-- Add to aria2 daemon for downloading
fn_diana_addpaused.cgi#@DIANA_ADDPAUSED&*#-- Add to aria2 daemon for downloading (paused state)
fn_aria2p.cgi#@TUI_ARIA2P&#-- Aria2p TUI aria2 daemon download manager (python3)
fn_aria2t.cgi#@TUI_ARIA2T&#-- Aria2t TUI aria2 daemon download manager (c/c++)
http://wttr.in#@WWW_WTTR&#-- Check weather forecast
https://text.npr.org#@WWW_NPR&#-- NPR latest news
http://lite.cnn.io/en#@WWW_CNN&#-- Breaking news
http://68k.news/#@WWW_68k&#-- Headlines from the future
https://news.ycombinator.com#@WWW_HN&#-- Hacker news
https://thepiratebay10.org/top/all#@WWW_TPB&#-- Piratebay top 100 torrents
https://1337x.to/top-100#@WWW_1337X&#-- 1337x top 100 torrents
https://raw.githubusercontent.com/tats/w3m/master/ChangeLog#@WWW_W3MCLOG&#-- W3M updated changelog
https://github.com/tats/w3m/issues#@WWW_W3MISSUE&#-- W3M open issue
https://www.reddit.com/r/w3m/.mobile#@WWW_W3M&#-- W3M subreddit
https://www.reddit.com/r/commandline/.mobile#@WWW_CLI&#-- Commandline subreddit
https://www.reddit.com/r/linux/.mobile#@WWW_GNU&#-- GNU/Linux subreddit
gopher://bitreich.org/1/lawn#@WWW_LAWN&#-- Gopher list of popular gopherhole
~/Downloads#@DIR_DL&#-- Open ~/Downloads directory
/media#@DIR_MEDIA&#-- Open /media directory
EOF
}

# clear screen
printf "\033c"

w3m_fnx_clipboard=/tmp/w3m_fnx_clipboard.txt

# not running tmux
if [ "$TMUX_PANE" = "%0" ] || [ -z "$TMUX" ] || [ -z "$TERM_PROGRAM" ] ; then
  selection="$( fnx_database | sort -t '@' -k2 | column -t  -s '#' | \
    fzf -i -e --delimiter '@' --with-nth 2.. --prompt='fzf-miru [$func|&custom|*fav] (run a W3M command): ' \
    --info=default --layout=reverse --tiebreak=index | \
    awk '{print $1}' )"
  [ -z "$selection" ] && echo "" > "$w3m_fnx_clipboard" && exit
# tmux -ge 3.2 popup
elif [ "$TERM_PROGRAM" = tmux ] ; then
  selection="$( fnx_database | sort -t '@' -k2 | column -t  -s '#' | \
    fzf-tmux -p -w 80% -h 70% -i -e --delimiter '@' --with-nth 2.. --prompt='fzf-miru [$func|&custom|*fav] (run a W3M command): ' \
    --info=default --layout=reverse --tiebreak=index | \
    awk '{print $1}' )"
  [ -z "$selection" ] && echo "" > "$w3m_fnx_clipboard" && exit
# tmux -lt 3.2 regular split
elif [ -n "$TMUX" ] ; then
  selection="$( fnx_database | sort -t '@' -k2 | column -t  -s '#' | \
    fzf-tmux -i -e --delimiter '@' --with-nth 2.. --prompt='fzf-miru [$func|&custom|*fav] (run a W3M command): ' \
    --info=default --layout=reverse --tiebreak=index |
    awk '{print $1}' )"
  [ -z "$selection" ] && echo "" > "$w3m_fnx_clipboard" && exit
fi
echo "$selection" > "$w3m_fnx_clipboard"
