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
    drawManyPixels(7, row, darkGrey, 5)
    
    row+=1
    drawManyPixels(5, row, darkGrey, 2)
    
    drawManyPixels(7, row, white, 5)

    drawManyPixels(12, row, darkGrey, 2)
    
    row+=1
    drawPixel(5, row, darkGrey)
    drawManyPixels(6, row, lightGrey, 2)
    drawManyPixels(8, row, white, 3)
    drawPixel(11, row, darkGrey)
    drawPixel(12, row, white)
    drawPixel(13, row, darkGrey)

    unicornhathd.show()

    time.sleep(5)

def drawManyPixels(col, row, color, numToDraw):
    i = 0
    while i < numToDraw:
        drawPixel(col, row, color)
        i += 1

def drawPixel(col, row, color):
    unicornhathd.set_pixel(col, row, color[0], color[1], color[2])