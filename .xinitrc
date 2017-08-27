#!/bin/sh
#
# ~/.xinitrc
#
# Executed by startx (run your window manager from here)

if [ -d /etc/X11/xinit/xinitrc.d ]; then
  for f in /etc/X11/xinit/xinitrc.d/*; do
    [ -x "$f" ] && . "$f"
  done
  unset f
fi

xrdb -load ~/.Xresources

xset -dpms
xset s off
xset noblank
xset r rate 200 20

xmodmap -e 'clear lock'

udiskie &

exec i3
