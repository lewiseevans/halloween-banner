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

    row = 2
    util.drawManyPixels(5, row, lightGrey, 6)

    row = 3
    util.drawPixel(4, row, lightGrey)
    util.drawManyPixels(5, row, white, 4)
    util.drawPixel(9, row, lightGrey)
    util.drawPixel(10, row, white)
    util.drawPixel(11, row, lightGrey)

    row = 4
    util.drawPixel(3, row, lightGrey)
    util.drawPixel(4, row, white)
    util.drawManyPixels(5, row, lightGrey, 3)
    util.drawManyPixels(8, row, white, 2)
    util.drawPixel(10, row, darkGrey)
    util.drawPixel(11, row, white)
    util.drawPixel(12, row, lightGrey)

    row = 5
    util.drawPixel(2, row, lightGrey)
    util.drawManyPixels(3, row, white, 2)
    util.drawPixel(5, row, lightGrey)
    util.drawPixel(6, row, darkGrey)
    util.drawPixel(7, row, lightGrey)
    util.drawPixel(8, row, white)
    util.drawPixel(9, row, darkGrey)
    util.drawManyPixels(10, row, lightGrey, 2)  
    util.drawPixel(12, row, white)
    util.drawPixel(13, row, lightGrey)

    row = 6
    util.drawPixel(2, row, lightGrey)
    util.drawPixel(3, row, white)
    util.drawPixel(4, row, lightGrey)
    util.drawManyPixels(5, row, darkGrey, 2)
    util.drawManyPixels(7, row, white, 2)
    util.drawPixel(9, row, darkGrey)
    util.drawPixel(10, row, white)
    util.drawPixel(11, row, lightGrey)
    util.drawPixel(12, row, white)
    util.drawPixel(13, row, lightGrey)

    row = 7
    util.drawPixel(2, row, lightGrey)
    util.drawPixel(3, row, white)
    util.drawPixel(4, row, lightGrey)
    util.drawPixel(5, row, darkGrey)
    util.drawPixel(6, row, lightGrey)
    util.drawPixel(7, row, white)
    util.drawPixel(8, row, lightGrey)
    util.drawManyPixels(9, row, darkGrey, 2)
    util.drawManyPixels(11, row, white, 2)
    util.drawPixel(13, row, lightGrey)

    row = 8
    util.drawPixel(2, row, lightGrey)
    util.drawPixel(3, row, white)
    util.drawManyPixels(4, row, darkGrey, 3)
    util.drawPixel(7, row, white)
    util.drawManyPixels(8, row, darkGrey, 3)
    util.drawPixel(11, row, lightGrey)
    util.drawPixel(12, row, white)
    util.drawPixel(13, row, lightGrey)

    row = 9
    util.drawPixel(2, row, lightGrey)
    util.drawPixel(3, row, white)
    util.drawManyPixels(4, row, darkGrey, 3)
    util.drawManyPixels(7, row, white, 2)
    util.drawManyPixels(9, row, darkGrey, 2)
    util.drawPixel(11, row, lightGrey)
    util.drawPixel(12, row, white)
    util.drawPixel(13, row, lightGrey)

    row = 10
    util.drawPixel(2, row, lightGrey)
    util.drawManyPixels(3, row, white, 2)
    util.drawPixel(5, row, darkGrey)
    util.drawPixel(6, row, lightGrey)
    util.drawPixel(7, row, white)
    util.drawManyPixels(8, row, lightGrey, 2)
    util.drawPixel(10, row, white)
    util.drawPixel(11, row, darkGrey)
    util.drawPixel(12, row, white)
    util.drawPixel(13, row, lightGrey)

    row = 11
    util.drawPixel(3, row, lightGrey)
    util.drawPixel(4, row, white)
    util.drawPixel(5, row, lightGrey)
    util.drawPixel(6, row, white)
    util.drawManyPixels(7, row, darkGrey, 2)
    util.drawPixel(9, row, white)
    util.drawPixel(10, row, darkGrey)
    util.drawPixel(11, row, white)
    util.drawPixel(12, row, lightGrey)

    row = 12
    util.drawPixel(4, row, lightGrey)
    util.drawManyPixels(5, row, white, 2)
    util.drawManyPixels(7, row, darkGrey, 2)
    util.drawManyPixels(9, row, white, 2)
    util.drawPixel(11, row, lightGrey)

    row = 13
    util.drawManyPixels(5, row, lightGrey, 6)

    unicornhathd.show()
    time.sleep(5)