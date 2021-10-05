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

    row = 1
    util.drawPixel(0, row, lightGrey)
    util.drawPixel(7, row, brown)
    util.drawManyPixels(10, row, lightGrey, 4)

    row = 2

    util.drawPixel(0, row, lightGrey)
    util.drawPixel(8, row, brown)
    util.drawManyPixels(10, row, lightGrey, 3)
    util.drawPixel(14, row, darkGrey)

    row = 3
    util.drawManyPixels(0, row, lightGrey, 3)
    util.drawPixel(9, row, brown)
    util.drawPixel(11, row, lightGrey)
    util.drawManyPixels(13, row, darkGrey, 2)

    row = 4
    util.drawManyPixels(0, row, lightGrey, 4)
    util.drawPixel(10, row, brown)
    util.drawManyPixels(12, row, darkGrey, 3)

    row = 5
    util.drawManyPixels(0, row, lightGrey, 5)
    util.drawPixel(11, row, brown)
    util.drawManyPixels(12, row, darkGrey, 2)
    util.drawPixel(15, row, lightGrey)

    row = 6
    util.drawManyPixels(0, row, lightGrey, 3)
    util.drawManyPixels(6, row, white, 3)
    util.drawPixel(10, row, lightGrey)
    util.drawPixel(12, row, brown)
    util.drawManyPixels(14, row, lightGrey, 2)

    row = 7
    util.drawManyPixels(0, row, lightGrey, 3)
    util.drawManyPixels(6, row, white, 3)
    util.drawPixel(11, row, lightGrey)
    util.drawManyPixels(14, row, lightGrey, 2)

    row = 8
    util.drawManyPixels(0, row, lightGrey,2)
    util.drawManyPixels(4, row, white, 7)
    util.drawManyPixels(12, row, lightGrey, 4)

    row = 9
    util.drawPixel(0, row, lightGrey)
    util.drawPixel(4, row, white)
    util.drawPixel(7, row, white)
    util.drawPixel(10, row, white)
    util.drawManyPixels(12, row, lightGrey, 4)

    row = 10
    util.drawPixel(4, row, white)
    util.drawPixel(7, row, white)
    util.drawPixel(10, row, white)
    util.drawManyPixels(12, row, lightGrey, 4)

    row = 11
    util.drawManyPixels(4, row, white, 7)
    util.drawManyPixels(12, row, lightGrey, 4)

    row = 12
    util.drawManyPixels(5, row, white, 5)
    util.drawManyPixels(11, row, lightGrey, 5)

    row = 13
    util.drawManyPixels(0, row, lightGrey, 3)
    util.drawManyPixels(7, row, white, 2)
    util.drawManyPixels(10, row, lightGrey, 6)

    row = 14
    util.drawManyPixels(0, row, lightGrey, 4)
    util.drawManyPixels(9, row, lightGrey, 7)

    row = 15
    util.drawManyPixels(0, row, lightGrey, 16)

    unicornhathd.show()
    time.sleep(5)