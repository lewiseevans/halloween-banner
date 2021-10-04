#!/usr/bin/env python

import unicornhathd

def drawManyPixels(col, row, color, numToDraw):
    i = 0
    while i < numToDraw:
        drawPixel(col, row, color)
        col += 1
        i += 1

def drawPixel(col, row, color):
    unicornhathd.set_pixel(col, row, color[0], color[1], color[2])