# VIM Mouse Grid
GUI vimium style hinting mode grid with mouse hotkeys navigation using keynav and xmousless

* tutorial video: [Link](https://youtu.be/h080D6-dgt4)

### install requirements
- [xmouseless](https://github.com/jbensmann/xmouseless)
- [keynav](https://github.com/jordansissel/keynav)

### xmouseless config ( config.h )
----
    /* the rate at which the mouse moves in Hz
     * does not change its speed */
    static const unsigned int move_rate = 50;
    
    /* the default speed of the mouse pointer
     * in pixels per second */
    static const unsigned int default_speed = 500;
    
    /* changes the speed of the mouse pointer */
    static SpeedBinding speed_bindings[] = {
        /* key             speed */  
        { XK_Control_L,         3000 },
        { XK_Alt_L,             1500 },
        { XK_space,             100  },
        { XK_b,                 10   },
        { XK_semicolon,         1500 },
        { XK_apostrophe,        3000 },
    };
    
    /* moves the mouse pointer
     * you can also add any other direction (e.g. diagonals) */
    static MoveBinding move_bindings[] = {
        /* key         x      y */
        { XK_h,        -1,     0 },
        { XK_l,         1,     0 },
        { XK_k,         0,    -1 },
        { XK_j,         0,     1 },
        { XK_a,        -1,     0 },
        { XK_d,         1,     0 },
        { XK_w,         0,    -1 },
        { XK_s,         0,     1 },
    };
    
    /* 1: left
     * 2: middle
     * 3: right */
    static ClickBinding click_bindings[] = {
        /* key         button */  
        { XK_u,        1 },
        { XK_i,        2 },
        { XK_o,        3 },
        { XK_e,        1 },
        { XK_r,        2 },
        { XK_q,        3 },
    };
    
    /* scrolls up, down, left and right
     * a higher value scrolls faster */
    // list of keysym by name https://www.cl.cam.ac.uk/~mgk25/ucs/keysymdef.h
    static ScrollBinding scroll_bindings[] = {
        /* key        x      y */
        { XK_m,        0 ,    25 },   // scroll down
        { XK_comma,    0 ,   -25 },   // scroll up
        { XK_n,        25,    0  },   // scroll left
        { XK_period,  -25,    0  },   // scroll right
        { XK_plus,     0 ,    80 },   // scroll 
        { XK_minus,    0 ,   -80 },   // scroll 
        { XK_x,        0 ,    25 },   // scroll down
        { XK_c,        0 ,   -25 },   // scroll up
        { XK_z,        25,    0  },   // scroll left
        { XK_v,       -25,    0  },   // scroll right
    };
    
    /* executes shell commands */
    static ShellBinding shell_bindings[] = {
        /* key         command */  
        { XK_g,        "xdotool mousedown 1" },   // highlight | drag&drop (begin)
        { XK_t,        "xdotool mouseup 1" },     // highlight | drag&drop (end)
    };
    
    /* exits on key release which allows click and exit with one key */
    static KeySym exit_keys[] = {
        XK_Escape, XK_backslash
    };
----

### keynav config
----
    vim ~/.keynavrc
    
    F12 start, grid-nav on, grid 20x20    # activate grid
    space warp,sh "xmouseless",end        # jump on grid then exit and launch xmouseless
----

### autostart keynav config
----
    vim ~/.xprofile
    
    keynav daemonize &
----

### references
- https://youtu.be/h080D6-dgt4
- https://github.com/jordansissel/keynav
- https://github.com/jbensmann/xmouseless
- list of keysym by name https://www.cl.cam.ac.uk/~mgk25/ucs/keysymdef.h
- Keyboard Ninja Playlist: https://www.youtube.com/playlist?list=PLqv94xWU9zZ1cXfg3ED24G6RSt4NbFBfO

### Contact

                 _   _     _      _
      __ _  ___ | |_| |__ | | ___| |_ _   _
     / _` |/ _ \| __| '_ \| |/ _ \ __| | | |
    | (_| | (_) | |_| |_) | |  __/ |_| |_| |
     \__, |\___/ \__|_.__/|_|\___|\__|\__,_|
     |___/

- https://www.youtube.com/user/gotbletu
- https://odysee.com/@gotbletu
- https://twitter.com/gotbletu
- https://github.com/gotbletu

