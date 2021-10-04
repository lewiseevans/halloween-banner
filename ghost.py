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
    drawRow(8, row, darkGrey)
    drawRow(9, row, darkGrey)
    drawRow(10, row, darkGrey)
    drawRow(11, row, darkGrey)

    row+=1
    drawRow(5, row, darkGrey)
    drawRow(6, row, darkGrey)
    drawRow(7, row, white)
    drawRow(8, row, white)
    drawRow(9, row, white)
    drawRow(10, row, white)
    drawRow(11, row, white)
    drawRow(12, row, darkGrey)
    drawRow(13, row, darkGrey)
    unicornhathd.show()

    time.sleep(5)


def drawRow(col, row, color):
    unicornhathd.set_pixel(col, row, color[0], color[1], color[2])