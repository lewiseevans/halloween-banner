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

    green = (0, 180, 0)
    orange = (255, 136, 33)

    row = 1
    util.drawManyPixels(4, row, orange, 8)

    row += 1
    util.drawManyPixels(3, row, orange, 10)
    
    row += 1
    util.drawManyPixels(2, row, orange, 2)
    util.drawManyPixels(12, row, orange, 2)
    
    row += 1
    util.drawManyPixels(1, row, orange, 4)
    util.drawManyPixels(11, row, orange, 4)
    
    row += 1
    util.drawManyPixels(1, row, orange, 5)
    util.drawManyPixels(7, row, orange, 2)
    util.drawManyPixels(10, row, orange, 5)
    
    row += 1
    util.drawManyPixels(1, row, orange, 14)
        
    row += 1
    util.drawManyPixels(1, row, orange, 14)
    

    row += 1
    util.drawManyPixels(1, row, orange, 5)
    util.drawManyPixels(7, row, orange, 2)
    util.drawManyPixels(10, row, orange, 5)

    row += 1
    util.drawManyPixels(1, row, orange, 4)
    util.drawManyPixels(7, row, orange, 2)
    util.drawManyPixels(11, row, orange, 4)

    row += 1
    util.drawManyPixels(2, row, orange, 2)
    util.drawManyPixels(6, row, orange, 4)
    util.drawManyPixels(12, row, orange, 2)
        
    row += 1
    util.drawManyPixels(3, row, orange, 10)

    row += 1
    util.drawManyPixels(4, row, orange, 8)

    row += 1
    util.drawManyPixels(7, row, green, 2)

    row += 1
    util.drawPixel(8, row, green)

    unicornhathd.show()

    time.sleep(5)