#!/bin/sh

cat $QUTE_HTML | grep -Po "/channel/.[^\"]*" | grep -v "livestreaming" | sed 's/\/channel\///g' | sort | uniq > ~/.config/ytsubs-channels

cat $QUTE_HTML | grep -Po "/user/.[^\"]*" | grep -v "livestreaming" | sed 's/\/user\///g' | sort | uniq > ~/.config/ytsubs-users

