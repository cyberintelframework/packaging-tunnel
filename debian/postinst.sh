#!/bin/sh -e

# Source debconf library.
. /usr/share/debconf/confmodule

db_version 2.0

# This conf script is capable of backing up
db_capb backup

STATE=1 
while [ "$STATE" != 0 -a "$STATE" != 4 ]; do
    case "$STATE" in
    1)
        db_input high surfids-tunnel/keysize
    ;;
    
    2)
        db_get surfids-tunnel/keysize
        key_size = $RET
        db_input high surfids-tunnel/keycountry
    ;;
    3)
        db_get surfids-tunnel/keycountry
        echo "RET: $RET"
    ;;
    4)
        
    esac

    if db_go; then
        STATE=$(($STATE + 1))
    else
        STATE=$(($STATE - 1))
    fi
done
