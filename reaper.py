#!/usr/bin/env python

import unicornhathd
import time
import util

# Get the width and height of the display
width, height = unicornhathd.get_shape()

def draw():

    # Clear the display
    unicornhathd.off()

    # Clear the buffer
    unicornhathd.clear()

    # Set the rotation of the display
    unicornhathd.rotation(270)

    time.sleep(0.5)

    darkGrey = (100, 100, 100)
    lightGrey = (150, 150, 150) 
    brown = (90, 50, 20)
    white = (255, 255, 255)

    row = 0
    util.drawPixel(0, row, lightGrey)
    util.drawManyPixels(10, row, lightGrey, 5)

    unicornhathd.show()

    time.sleep(5)