#!/usr/bin/env python

import unicornhathd
import util
import time

# Get the width and height of the display
width, height = unicornhathd.get_shape()

white = (255, 255, 255)
darkGrey = (100, 100, 100)
lightGrey = (150, 150, 150)

def draw():

    # Clear the display
    unicornhathd.off()

    # Clear the buffer
    unicornhathd.clear()

    # Set the rotation of the display
    unicornhathd.rotation(270)

    time.sleep(0.5)

    row = 0
    util.drawManyPixels(7, row, darkGrey, 5)
    
    row += 1
    util.drawManyPixels(5, row, darkGrey, 2)
    util.drawManyPixels(7, row, lightGrey, 3)
    util.drawManyPixels(10, row, white, 2)
    util.drawManyPixels(12, row, darkGrey, 2)
    
    row += 1
    util.drawPixel(5, row, darkGrey)
    util.drawManyPixels(6, row, lightGrey, 2)
    util.drawManyPixels(8, row, white, 3)
    util.drawPixel(11, row, darkGrey)
    util.drawPixel(12, row, white)
    util.drawPixel(13, row, darkGrey)

    row += 1

    util.drawManyPixels(2, row, darkGrey, 4)
    util.drawManyPixels(6, row, white, 4)
    util.drawPixel(10, row, lightGrey)
    util.drawManyPixels(11, row, darkGrey, 4)

    row += 1
    util.drawPixel(2, row, darkGrey)
    util.drawPixel(3, row, white)
    util.drawPixel(4, row, darkGrey)
    util.drawPixel(5, row, lightGrey)
    util.drawManyPixels(6, row, white, 4)
    util.drawManyPixels(10, row, lightGrey, 2)
    util.drawPixel(12, row, darkGrey)
    util.drawPixel(13, row, white)
    util.drawPixel(14, row, darkGrey)
    
    row += 1
    util.drawPixel(2, row, darkGrey)
    util.drawPixel(3, row, white)
    util.drawPixel(4, row, lightGrey)
    util.drawManyPixels(5,row, white, 7)
    util.drawPixel(12, row, lightGrey)
    util.drawPixel(13, row, white)
    util.drawPixel(14, row, darkGrey)

    row += 1
    util.drawPixel(2, row, darkGrey)
    util.drawManyPixels(3,row, white, 11)
    util.drawPixel(14, row, darkGrey)
    
    row += 1
    util.drawManyPixels(2, row, darkGrey, 3)
    util.drawManyPixels(5, row, white, 6)
    util.drawPixel(11, row, lightGrey)
    util.drawManyPixels(12, row, darkGrey, 3)

    row += 1
    util.drawPixel(4, row, darkGrey)
    util.drawManyPixels(5, row, white, 2)
    util.drawManyPixels(9, row, white, 3)
    util.drawPixel(12, row, darkGrey)

    row += 1
    util.drawPixel(3, row, darkGrey)
    util.drawPixel(4, row, lightGrey)
    util.drawPixel(5, row, white)
    util.drawManyPixels(9, row, white, 2)
    util.drawPixel(11, row, lightGrey)
    util.drawPixel(12, row, darkGrey)

    row += 1
    util.drawManyPixels(3, row, darkGrey, 10)
    util.drawManyPixels(4, row, white, 8)
    util.drawPixel(12, row, lightGrey)


    row += 1
    util.drawPixel(3, row, darkGrey)
    util.drawPixel(4, row, white)
    util.drawPixel(7, row, white)
    util.drawPixel(10, row, white)
    util.drawPixel(11, row, lightGrey)
    util.drawPixel(12, row, darkGrey)

    row += 1
    util.drawPixel(3, row, darkGrey)
    util.drawManyPixels(4, row, white, 2)
    util.drawPixel(7, row, white)
    util.drawManyPixels(9, row, white, 2)
    util.drawManyPixels(11, row, darkGrey, 2)

    row += 1
    util.drawManyPixels(3, row, darkGrey, 2)
    util.drawManyPixels(5, row, white, 5)
    util.drawPixel(10, row, lightGrey)
    util.drawPixel(11, row, darkGrey)

    row += 1
    util.drawPixel(5, row, darkGrey)
    util.drawManyPixels(6, row, lightGrey, 4)
    util.drawManyPixels(10, row, darkGrey, 2)

    row += 1
    util.drawManyPixels(5, row, darkGrey, 6)

    unicornhathd.show()

    time.sleep(5)