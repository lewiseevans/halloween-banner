#!/usr/bin/env python

import unicornhathd
import signal
import reaper
import grave
import pumpkin
import vampire
import ghost

def shutdownHandler(sig, frame):
    print('Shutting down')
    unicornhathd.off()
    sys.exit(0)


signal.signal(signal.SIGINT, shutdownHandler)

while True:
    reapoer.draw()
    grave.draw()
    pumpkin.draw()
    vampire.draw()
    ghost.draw()