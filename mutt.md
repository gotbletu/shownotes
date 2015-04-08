# Mutt - Terminal Email Client
Mutt  is a small but very powerful text based program for reading and sending electronic mail under unix operating systems, including support for color terminals, MIME, OpenPGP, and a threaded sorting mode.

* tutorial video: [Link](https://www.youtube.com/watch?v=_Unn7fysiE0)
* offical website: [Link](http://www.mutt.org/)

### install requirements
    mutt

### create folder

    mkdir ~/.mutt

### add email accounts
- create the text files for each account you want to use
- replace gotbletu with your username
- edit PASSWORD


GMAIL

    vim ~/.mutt/account.com.gmail.gotbletu


    set imap_user = "gotbletu@gmail.com"                       
    set imap_pass = "PASSWORD"                                    
    set smtp_url = "smtp://gotbletu@smtp.gmail.com:587/"       
    set smtp_pass = "PASSWORD"                                    
    set from = "gotbletu@gmail.com"                            
    set realname = "Lord Mizukage"                                  
    set folder = "imaps://imap.gmail.com:993"                     
    set spoolfile = "+INBOX"                                      
    set postponed = "+[Gmail]/Drafts"                             
    set header_cache = ~/.mutt/com.gmail.gotbletu/cache/headers            
    set message_cachedir = ~/.mutt/com.gmail.gotbletu/cache/bodies         
    set certificate_file = ~/.mutt/com.gmail.gotbletu/certificates  

YAHOO

    vim ~/.mutt/account.com.yahoo.gotbletu
    

    set imap_user = "gotbletu@yahoo.com"
    set imap_pass = "PASSWORD"
    set smtp_url = "smtps://gotbletu@smtp.mail.yahoo.com:465"                                                               
    set smtp_pass = "PASSWORD"                                    
    set from = "gotbletu@yahoo.com"                            
    set realname = "Lord Raikage"                                  
    set folder = "imaps://imap.mail.yahoo.com:993"
    set spoolfile = "+INBOX"
    set postponed = "+[Yahoo]/Drafts"                             
    set header_cache = ~/.mutt/com.yahoo.gotbletu/cache/headers            
    set message_cachedir = ~/.mutt/com.yahoo.gotbletu/cache/bodies         
    set certificate_file = ~/.mutt/com.yahoo.gotbletu/certificates  

LIVE/msn/hotmail/outlook
    
    vim ~/.mutt/account.com.live.gotbletu


    set imap_user = "gotbletu@live.com"
    set imap_pass = "PASSWORD"
    set smtp_url = "smtp://gotbletu@live.com@smtp.live.com:587/"
    set smtp_pass = "PASSWORD"
    set from = "gotbletu@live.com"
    set realname = "Lord Kazekage"
    set folder = "imaps://imap-mail.outlook.com:993"
    set spoolfile = "+INBOX"
    set postponed = "+[Live]/Drafts"
    set header_cache = ~/.mutt/com.live.gotbletu/cache/headers            
    set message_cachedir = ~/.mutt/com.live.gotbletu/cache/bodies         
    set certificate_file = ~/.mutt/com.live.gotbletu/certificates  
    set ssl_force_tls = yes

Hotmail example

    vim ~/.mutt/account.com.hotmail.gotbletu
    

    set imap_user = "gotbletu@hotmail.com"
    set imap_pass = "PASSWORD"
    set smtp_url = "smtp://gotbletu@hotmail.com@smtp.live.com:587/"
    set smtp_pass = "PASSWORD"
    set from = "gotbletu@hotmail.com"
    set realname = "Lord Hokage"
    set folder = "imaps://imap-mail.outlook.com:993"
    set spoolfile = "+INBOX"
    set postponed = "+[Hotmail]/Drafts"
    set header_cache = ~/.mutt/com.hotmail.gotbletu/cache/headers            
    set message_cachedir = ~/.mutt/com.hotmail.gotbletu/cache/bodies         
    set certificate_file = ~/.mutt/com.hotmail.gotbletu/certificates  
    set ssl_force_tls = yes
    
Openmailbox https://www.openmailbox.org/
    
    vim ~/.mutt/account.org.openmailbox.gotbletu


    # imaps
    set spoolfile = "imaps://imap.openmailbox.org:993/INBOX"
    set folder = "imaps://imap.openmailbox.org:993"
    set imap_user = "gotbletu@openmailbox.org"
    set imap_pass = "PASSWORD"
    set imap_authenticators = "login"
    set imap_passive = "no"
    set imap_check_subscribed = "yes"
    set imap_list_subscribed = "yes"
    set mail_check = 60
    
    #smtps
    set smtp_url = "smtps://user@openmailbox.org@openmailbox.org:465"
    set smtp_pass = "XXX"
    set from = "user@openmailbox.org"

    # charset
    set charset	= "utf-8"
    set assumed_charset = "utf-8"
    set send_charset = "utf-8:iso-8859-15:us-ascii"
    
    # force SSL
    set ssl_starttls = "yes"
    set ssl_force_tls = "yes"
    

     
### configuration
set your folder hooks, macros hotkey, default account and text editor

    
    vim ~/.muttrc



    # Folder hooks
    folder-hook 'account.com.gmail.gotbletu' 'source ~/.mutt/account.com.gmail.gotbletu'
    folder-hook 'account.com.yahoo.gotbletu' 'source ~/.mutt/account.com.yahoo.gotbletu'
    folder-hook 'account.com.live.gotbletu' 'source ~/.mutt/account.com.live.gotbletu'
    folder-hook 'account.com.hotmail.gotbletu' 'source ~/.mutt/account.com.hotmail.gotbletu'
    
    # Default account
    source ~/.mutt/account.com.gmail.gotbletu
    
    # Macros for switching accounts
    
    macro index <F12> '<sync-mailbox><enter-command>source ~/.mutt/account.com.gmail.gotbletu<enter><change-folder>!<enter>'
    macro index <F11> '<sync-mailbox><enter-command>source ~/.mutt/account.com.yahoo.gotbletu<enter><change-folder>!<enter>'
    macro index <F10> '<sync-mailbox><enter-command>source ~/.mutt/account.com.live.gotbletu<enter><change-folder>!<enter>'
    macro index <F9> '<sync-mailbox><enter-command>source ~/.mutt/account.com.hotmail.gotbletu<enter><change-folder>!<enter>'
    
    # Set default text editor
    set editor = "$EDITOR"
    
    #-------- Basic Config {{{
    #------------------------------------------------------
    set imap_check_subscribed
    # set hostname = gmail.com
    set mail_check = 120
    set timeout = 300
    set imap_keepalive = 300
    # set record = "+[GMail]/Sent Mail"
    set move = no
    set include
    set sort = 'threads'
    set sort_aux = 'reverse-last-date-received'
    set auto_tag = yes
    ignore "Authentication-Results:"
    ignore "DomainKey-Signature:"
    ignore "DKIM-Signature:"
    hdr_order Date From To Cc
    alternative_order text/plain text/html *
    auto_view text/html
    bind editor <Tab> complete-query
    bind editor ^T complete
    bind editor <space> noop 
    # }}}
    #-------- Color Theme {{{
    #------------------------------------------------------
    
    color hdrdefault cyan default
    color attachment yellow default
    
    color header brightyellow default "From: "
    color header brightyellow default "Subject: "
    color header brightyellow default "Date: "
    
    color quoted green default
    color quoted1 cyan default
    color quoted2 green default
    color quoted3 cyan default
    
    color error     red             default         # error messages
    color message   white           default         # message  informational messages
    color indicator white           red             # indicator for the "current message"
    color status    white           blue            # status lines in the folder index sed for the mini-help line
    color tree      red             default         # the "tree" display of threads within the folder index
    color search    white           blue            # search matches found with search within the internal pager
    color markers   red             default         # The markers indicate a wrapped line hen showing messages with looong lines
    
    color index     yellow default  '~O'
    color index     yellow default  '~N'
    color index     brightred       default '~F'    # Flagged Messages are important!
    color index     blue default    '~D'            # Deleted Mails - use dark color as these are already "dealt with"
    # }}} 


### hotkeys to remember
    Ctrl+g = cancle a prompt
    F1-F12 = switch email account
    y = change to different mailboxes
    $ = sync-mailbox

### references
- https://gist.github.com/miguelmota/9456162
- https://github.com/narkoleptik/dotfiles/blob/master/.mutt/account.yahoo
- http://profectium.blogspot.com/2013/12/how-to-set-up-hotmail-in-mutt.html
- http://lifehacker.com/5574557/how-to-use-the-fast-and-powerful-mutt-email-client-with-gmail
    
    
### contact

                 _   _     _      _         
      __ _  ___ | |_| |__ | | ___| |_ _   _ 
     / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
    | (_| | (_) | |_| |_) | |  __/ |_| |_| |
     \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
     |___/                                  

- http://www.youtube.com/user/gotbletu
- https://twitter.com/gotbletu
- https://www.facebook.com/gotbletu
- https://plus.google.com/+gotbletu
- https://github.com/gotbletu
- gotbletu@gmail.com


