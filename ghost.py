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
    
    row += 1
    drawManyPixels(5, row, darkGrey, 2)
    drawManyPixels(7, row, lightGrey, 3)
    drawManyPixels(10, row, white, 2)
    drawManyPixels(12, row, darkGrey, 2)
    
    row += 1
    drawPixel(5, row, darkGrey)
    drawManyPixels(6, row, lightGrey, 2)
    drawManyPixels(8, row, white, 3)
    drawPixel(11, row, darkGrey)
    drawPixel(12, row, white)
    drawPixel(13, row, darkGrey)

    row += 1

    drawManyPixels(2, row, darkGrey, 4)
    drawManyPixels(6, row, white, 4)
    drawPixel(10, row, lightGrey)
    drawManyPixels(11, row, darkGrey, 4)

    row += 1
    drawPixel(2, row, darkGrey)
    drawPixel(3, row, white)
    drawPixel(4, row, darkGrey)
    drawPixel(5, row, lightGrey)
    drawManyPixels(6, row, white, 4)
    drawManyPixels(10, row, lightGrey, 2)
    drawPixel(12, row, darkGrey)
    drawPixel(13, row, white)
    drawPixel(14, row, darkGrey)
    
    row += 1
    drawPixel(2, row, darkGrey)
    drawPixel(3, row, white)
    drawPixel(4, row, lightGrey)
    drawManyPixels(5,row, white, 7)
    drawPixel(12, row, lightGrey)
    drawPixel(13, row, white)
    drawPixel(14, row, darkGrey)

    row += 1
    drawPixel(2, row, darkGrey)
    drawManyPixels(3,row, white, 11)
    drawPixel(14, row, darkGrey)
    
    row += 1
    drawManyPixels(2, row, darkGrey, 3)
    drawManyPixels(5, row, white, 6)
    drawPixel(11, row, lightGrey)
    drawManyPixels(12, row, darkGrey, 3)

    row += 1
    drawPixel(4, row, darkGrey)
    drawManyPixels(5, row, white, 2)
    drawManyPixels(9, row, white, 3)
    drawPixel(12, row, darkGrey)

    row += 1
    drawPixel(3, row, darkGrey)
    drawPixel(4, row, lightGrey)
    drawPixel(5, row, white)
    drawManyPixels(9, row, white, 2)
    drawPixel(11, row, lightGrey)
    drawPixel(12, row, darkGrey)

    row += 1
    drawManyPixels(3, row, darkGrey, 10)
    drawManyPixels(4, row, white, 8)
    drawPixel(12, row, lightGrey)


    row += 1
    drawPixel(3, row, darkGrey)
    drawPixel(4, row, white)
    drawPixel(7, row, white)
    drawPixel(10, row, white)
    drawPixel(11, row, lightGrey)
    drawPixel(12, row, darkGrey)

    row += 1
    drawPixel(3, row, darkGrey)
    drawManyPixels(4, row, white, 2)
    drawPixel(7, row, white)
    drawManyPixels(9, row, white, 2)
    drawManyPixels(11, row, darkGrey, 2)

    row += 1
    drawManyPixels(3, row, darkGrey, 2)
    drawManyPixels(5, row, white, 5)
    drawPixel(10, row, lightGrey)
    drawPixel(11, row, darkGrey)

    row += 1
    drawPixel(5, row, darkGrey)
    drawManyPixels(6, row, lightGrey, 4)
    drawManyPixels(10, row, darkGrey, 2)

    row += 1
    drawManyPixels(5, row, darkGrey, 6)

    unicornhathd.show()

    time.sleep(5)

def drawManyPixels(col, row, color, numToDraw):
    i = 0
    while i < numToDraw:
        drawPixel(col, row, color)
        col += 1
        i += 1

def drawPixel(col, row, color):
    unicornhathd.set_pixel(col, row, color[0], color[1], color[2])