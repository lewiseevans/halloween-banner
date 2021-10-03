#!/usr/bin/env python


import stocking
import rainbow
import pumpkin
import unicornhathd
import signal


def shutdownHandler(sig, frame):
    print('Shutting down')
    unicornhathd.off()
    sys.exit(0)


signal.signal(signal.SIGINT, shutdownHandler)

while True:
    pumpkin.draw()