#!/usr/bin/env python

import unicornhathd
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
    drawRow(7, row, darkGrey)
    unicornhathd.set_pixel(8, row, 100, 100, 100)
    unicornhathd.set_pixel(9, row, 100, 100, 100)
    unicornhathd.set_pixel(10, row, 100, 100, 100)
    unicornhathd.set_pixel(11, row, 100, 100, 100)

    row+=1
    unicornhathd.set_pixel(5, row, 100, 100, 100)
    unicornhathd.set_pixel(6, row, 100, 100, 100)
    unicornhathd.set_pixel(7, row, 150, 150, 150)
    unicornhathd.set_pixel(8, row, 150, 150, 150)
    unicornhathd.set_pixel(9, row, 150, 150, 150)
    unicornhathd.set_pixel(10, row, 255, 255, 255)
    unicornhathd.set_pixel(11, row, 255, 255, 255)
    unicornhathd.set_pixel(12, row, 100, 100, 100)
    unicornhathd.set_pixel(13, row, 100, 100, 100)
    unicornhathd.show()

    time.sleep(5)


def drawRow(col, row, color):
    unicornhathd.set_pixel(col, row, color[0], color[1], color[2])