#!/usr/bin/env python

import unicornhathd
import time

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

    row = 0
    unicornhathd.set_pixel(0, row, 255, 255, 255)
    unicornhathd.set_pixel(1, row, 255, 255, 255)
    unicornhathd.set_pixel(2, row, 255, 255, 255)
    unicornhathd.set_pixel(3, row, 255, 255, 255)
    unicornhathd.set_pixel(4, row, 255, 255, 255)
    unicornhathd.set_pixel(5, row, 255, 255, 255)
    unicornhathd.set_pixel(6, row, 255, 255, 255)
    unicornhathd.set_pixel(7, row, 255, 255, 255)
    unicornhathd.set_pixel(8, row, 255, 255, 255)
    unicornhathd.set_pixel(9, row, 255, 255, 255)
    unicornhathd.set_pixel(10, row, 255, 255, 255)
    unicornhathd.set_pixel(11, row, 255, 255, 255)
    unicornhathd.set_pixel(12, row, 255, 255, 255)
    unicornhathd.set_pixel(13, row, 255, 255, 255)
    unicornhathd.set_pixel(14, row, 255, 255, 255)
    unicornhathd.set_pixel(15, row, 255, 255, 255)

    row += 1
    unicornhathd.set_pixel(0, row, 255, 255, 255)
    unicornhathd.set_pixel(1, row, 255, 255, 255)
    unicornhathd.set_pixel(2, row, 255, 255, 255)
    unicornhathd.set_pixel(3, row, 255, 255, 255)
    unicornhathd.set_pixel(4, row, 255, 255, 255)
    unicornhathd.set_pixel(12, row, 255, 255, 255)
    unicornhathd.set_pixel(13, row, 255, 255, 255)
    unicornhathd.set_pixel(14, row, 255, 255, 255)
    unicornhathd.set_pixel(15, row, 255, 255, 255)

    row +=1
    unicornhathd.set_pixel(0, row, 255, 255, 255)
    unicornhathd.set_pixel(1, row, 255, 255, 255)
    unicornhathd.set_pixel(2, row, 255, 255, 255)
    unicornhathd.set_pixel(3, row, 255, 255, 255)
    unicornhathd.set_pixel(4, row, 255, 255, 255)
    unicornhathd.set_pixel(6, row, 128, 128, 128)
    unicornhathd.set_pixel(7, row, 128, 128, 128)
    unicornhathd.set_pixel(8, row, 255, 255, 0) # Yellow
    unicornhathd.set_pixel(9, row, 128, 128, 128) # Grey
    unicornhathd.set_pixel(10, row, 128, 128, 128)
    unicornhathd.set_pixel(13, row, 255, 255, 255)
    unicornhathd.set_pixel(14, row, 255, 255, 255)
    unicornhathd.set_pixel(15, row, 255, 255, 255)

    row +=1
    unicornhathd.set_pixel(0, row, 255, 255, 255)
    unicornhathd.set_pixel(1, row, 255, 255, 255)
    unicornhathd.set_pixel(2, row, 255, 255, 255)
    unicornhathd.set_pixel(3, row, 255, 255, 255)
    unicornhathd.set_pixel(5, row, 128, 128, 128)
    unicornhathd.set_pixel(11, row, 128, 128, 128)
    unicornhathd.set_pixel(12, row, 128, 128, 128)
    unicornhathd.set_pixel(14, row, 255, 255, 255)
    unicornhathd.set_pixel(15, row, 255, 255, 255)

    row +=1
    unicornhathd.set_pixel(0, row, 255, 255, 255)
    unicornhathd.set_pixel(1, row, 255, 255, 255)
    unicornhathd.set_pixel(2, row, 255, 255, 255)
    unicornhathd.set_pixel(4, row, 128, 128, 128)
    unicornhathd.set_pixel(6, row, 255, 255, 255)
    unicornhathd.set_pixel(7, row, 255, 255, 255)
    unicornhathd.set_pixel(8, row, 255, 255, 255)
    unicornhathd.set_pixel(9, row, 255, 255, 255)
    unicornhathd.set_pixel(10, row, 255, 255, 255)
    unicornhathd.set_pixel(13, row, 128, 128, 128)
    unicornhathd.set_pixel(15, row, 255, 255, 255)

    row +=1
    unicornhathd.set_pixel(0, row, 255, 255, 255)
    unicornhathd.set_pixel(1, row, 255, 255, 255)
    unicornhathd.set_pixel(3, row, 128, 128, 128)
    unicornhathd.set_pixel(5, row, 255, 255, 255)
    unicornhathd.set_pixel(6, row, 255, 255, 255)
    unicornhathd.set_pixel(7, row, 255, 0, 0)
    unicornhathd.set_pixel(8, row, 255, 255, 255)
    unicornhathd.set_pixel(9, row, 255, 255, 255)
    unicornhathd.set_pixel(10, row, 255, 255, 255)
    unicornhathd.set_pixel(11, row, 255, 255, 255)
    unicornhathd.set_pixel(14, row, 128, 128, 128)


    row +=1
    unicornhathd.set_pixel(0, row, 255, 255, 255)    
    unicornhathd.set_pixel(2, row, 128, 128, 128)
    unicornhathd.set_pixel(4, row, 255, 255, 255)
    unicornhathd.set_pixel(5, row, 255, 255, 255)
    unicornhathd.set_pixel(6, row, 255, 255, 255)
    unicornhathd.set_pixel(7, row, 255, 0, 0)
    unicornhathd.set_pixel(10, row, 255, 0, 0)
    unicornhathd.set_pixel(11, row, 255, 255, 255)
    unicornhathd.set_pixel(12, row, 255, 255, 255)
    unicornhathd.set_pixel(14, row, 128, 128, 128)

    row +=1
    unicornhathd.set_pixel(0, row, 255, 255, 255)
    unicornhathd.set_pixel(4, row, 255, 255, 255)
    unicornhathd.set_pixel(5, row, 255, 255, 255)
    unicornhathd.set_pixel(6, row, 255, 255, 255)
    unicornhathd.set_pixel(7, row, 255, 255, 255)
    unicornhathd.set_pixel(8, row, 255, 255, 255)
    unicornhathd.set_pixel(9, row, 255, 255, 255)
    unicornhathd.set_pixel(10, row, 255, 255, 255)
    unicornhathd.set_pixel(11, row, 255, 255, 255)
    unicornhathd.set_pixel(12, row, 255, 255, 255)

    row +=1
    unicornhathd.set_pixel(0, row, 255, 255, 255)
    unicornhathd.set_pixel(1, row, 255, 255, 255)
    unicornhathd.set_pixel(2, row, 255, 255, 255)
    unicornhathd.set_pixel(4, row, 255, 255, 255)
    unicornhathd.set_pixel(5, row, 255, 255, 255)
    unicornhathd.set_pixel(7, row, 255, 255, 255)
    unicornhathd.set_pixel(8, row, 255, 255, 255)
    unicornhathd.set_pixel(9, row, 255, 255, 255)
    unicornhathd.set_pixel(10, row, 255, 255, 255)
    unicornhathd.set_pixel(12, row, 255, 255, 255)
    unicornhathd.set_pixel(14, row, 255, 255, 255)
    unicornhathd.set_pixel(15, row, 255, 255, 255)

    row +=1
    unicornhathd.set_pixel(0, row, 255, 255, 255)
    unicornhathd.set_pixel(1, row, 255, 255, 255)
    unicornhathd.set_pixel(2, row, 255, 255, 255)
    unicornhathd.set_pixel(4, row, 255, 255, 255)
    unicornhathd.set_pixel(5, row, 255, 255, 255)
    unicornhathd.set_pixel(6, row, 255, 255, 255)
    unicornhathd.set_pixel(7, row, 255, 255, 255)
    unicornhathd.set_pixel(8, row, 255, 255, 255)
    unicornhathd.set_pixel(9, row, 255, 255, 255)
    unicornhathd.set_pixel(10, row, 255, 255, 255)
    unicornhathd.set_pixel(11, row, 255, 255, 255)
    unicornhathd.set_pixel(12, row, 255, 255, 255)
    unicornhathd.set_pixel(14, row, 255, 255, 255)
    unicornhathd.set_pixel(15, row, 255, 255, 255)

    row +=1
    unicornhathd.set_pixel(0, row, 255, 255, 255)
    unicornhathd.set_pixel(1, row, 255, 255, 255)
    unicornhathd.set_pixel(4, row, 255, 255, 255)
    unicornhathd.set_pixel(5, row, 255, 255, 255)
    unicornhathd.set_pixel(6, row, 255, 255, 255)
    unicornhathd.set_pixel(7, row, 255, 255, 255)
    unicornhathd.set_pixel(10, row, 255, 255, 255)
    unicornhathd.set_pixel(11, row, 255, 255, 255)
    unicornhathd.set_pixel(12, row, 255, 255, 255)
    unicornhathd.set_pixel(14, row, 255, 255, 255)
    unicornhathd.set_pixel(15, row, 255, 255, 255)

    row +=1
    unicornhathd.set_pixel(0, row, 255, 255, 255)
    unicornhathd.set_pixel(1, row, 255, 255, 255)
    unicornhathd.set_pixel(5, row, 255, 255, 255)
    unicornhathd.set_pixel(6, row, 255, 255, 255)
    unicornhathd.set_pixel(11, row, 255, 255, 255)
    unicornhathd.set_pixel(14, row, 255, 255, 255)
    unicornhathd.set_pixel(15, row, 255, 255, 255)

    row +=1
    unicornhathd.set_pixel(0, row, 255, 255, 255)
    unicornhathd.set_pixel(1, row, 255, 255, 255)
    unicornhathd.set_pixel(2, row, 255, 255, 255)
    unicornhathd.set_pixel(13, row, 255, 255, 255)
    unicornhathd.set_pixel(14, row, 255, 255, 255)
    unicornhathd.set_pixel(15, row, 255, 255, 255)

    row +=1
    unicornhathd.set_pixel(0, row, 255, 255, 255)
    unicornhathd.set_pixel(1, row, 255, 255, 255)
    unicornhathd.set_pixel(2, row, 255, 255, 255)
    unicornhathd.set_pixel(3, row, 255, 255, 255)
    unicornhathd.set_pixel(12, row, 255, 255, 255)
    unicornhathd.set_pixel(13, row, 255, 255, 255)
    unicornhathd.set_pixel(14, row, 255, 255, 255)
    unicornhathd.set_pixel(15, row, 255, 255, 255)

    row +=1
    unicornhathd.set_pixel(0, row, 255, 255, 255)
    unicornhathd.set_pixel(1, row, 255, 255, 255)
    unicornhathd.set_pixel(2, row, 255, 255, 255)
    unicornhathd.set_pixel(3, row, 255, 255, 255)
    unicornhathd.set_pixel(4, row, 255, 255, 255)
    unicornhathd.set_pixel(5, row, 255, 255, 255)
    unicornhathd.set_pixel(11, row, 255, 255, 255)
    unicornhathd.set_pixel(12, row, 255, 255, 255)
    unicornhathd.set_pixel(13, row, 255, 255, 255)
    unicornhathd.set_pixel(14, row, 255, 255, 255)
    unicornhathd.set_pixel(15, row, 255, 255, 255)

    row +=1
    unicornhathd.set_pixel(0, row, 255, 255, 255)
    unicornhathd.set_pixel(1, row, 255, 255, 255)
    unicornhathd.set_pixel(2, row, 255, 255, 255)
    unicornhathd.set_pixel(3, row, 255, 255, 255)
    unicornhathd.set_pixel(4, row, 255, 255, 255)
    unicornhathd.set_pixel(5, row, 255, 255, 255)
    unicornhathd.set_pixel(6, row, 255, 255, 255)
    unicornhathd.set_pixel(7, row, 255, 255, 255)
    unicornhathd.set_pixel(8, row, 255, 255, 255)
    unicornhathd.set_pixel(9, row, 255, 255, 255)
    unicornhathd.set_pixel(10, row, 255, 255, 255)
    unicornhathd.set_pixel(11, row, 255, 255, 255)
    unicornhathd.set_pixel(12, row, 255, 255, 255)
    unicornhathd.set_pixel(13, row, 255, 255, 255)
    unicornhathd.set_pixel(14, row, 255, 255, 255)
    unicornhathd.set_pixel(15, row, 255, 255, 255)

    unicornhathd.show()

    time.sleep(5)