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
    darkGrey = (100, 100, 100)
    black = (0, 0, 0)

    row = 0
    util.drawManyPixels(0, row, green, 16)

    row += 1
    util.drawManyPixels(1, row, green, 14)

    row += 1
    util.drawManyPixels(2, row, darkGrey, 12)

    row += 1
    util.drawManyPixels(2, row, darkGrey, 12)

    row += 1
    util.drawManyPixels(2, row, darkGrey, 12)

    row += 1
    util.drawManyPixels(2, row, darkGrey, 12)

    row +=1
    util.drawManyPixels(2, row, darkGrey, 12)
    util.drawPixel(3, row, black)
    util.drawPixel(5, row, black)
    util.drawPixel(7, row, black)
    util.drawPixel(10, row, black)

    row += 1
    util.drawPixel(2, row, darkGrey)
    util.drawManyPixels(5, row, darkGrey, 2)
    util.drawManyPixels(8, row, darkGrey, 2)
    util.drawPixel(13, row, darkGrey)

    row += 1 
    util.drawPixel(2, row, darkGrey)
    util.drawPixel(4, row, darkGrey)
    util.drawPixel(6, row, darkGrey)
    util.drawManyPixels(8, row, darkGrey, 2)
    util.drawPixel(11, row, darkGrey)
    util.drawPixel(13, row, darkGrey)
    
    row += 1
    util.drawPixel(2, row, darkGrey)
    util.drawManyPixels(5, row, darkGrey, 2)
    util.drawManyPixels(8, row, darkGrey, 2)
    util.drawPixel(13, row, darkGrey)

    row += 1
    util.drawManyPixels(2, row, darkGrey, 12)

    row += 1
    util.drawManyPixels(3, row, darkGrey, 10)

    row += 1
    util.drawManyPixels(3, row, darkGrey, 10)

    row += 1
    util.drawManyPixels(4, row, darkGrey, 8)

    unicornhathd.show()

    time.sleep(5)