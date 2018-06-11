#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Raspberry Pi Neopixel Cheerlights
# Author: David Bradway
# 
# Uses NeoPixel Python library wrapper by Tony DiCola (tony@tonydicola.com)
#  and NeoPixel/ rpi_ws281x library created by Jeremy Garff.
# This Raspberry Pi port is based on Arduino and Python code by Dave Koerner https://hexenwarg.wordpress.com
import time
import requests

from neopixel import *

# LED strip configuration:
LED_COUNT   = 12      # CHANGEME! Number of LED pixels.
LED_PIN     = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA     = 5       # DMA channel to use for generating signal (try 5)
LED_INVERT  = False   # True to invert the signal (when using NPN transistor level shift)

# I'm going to use a var to check if I've seen the color before
color = 'black'
cheerlights = color

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel(((i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def historyChase(strip, light_history, wait_ms=50):
    """Wipe last three Cheerlights colors across display ten pixels at a time."""
    for q in range(3):
        for head in range(strip.numPixels()+10):
            if head < strip.numPixels():
                strip.setPixelColor(head, light_history[q])
            tail = head - 10
            if tail >= 0:
                strip.setPixelColor(tail, Color(0,0,0))
            strip.show()
            time.sleep(wait_ms/1000.0)


# Main program logic follows:
if __name__ == '__main__':

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    # Introduce a list for keeping the last three Cheerlight Colors
    light_history = [Color(0, 0, 0),Color(0, 0, 0),Color(0, 0, 0)];

    print 'Press Ctrl-C to quit.'
    while True:
        # Read the thingspeak feed to get the current color
        try:
            cheerlights = requests.get('http://api.thingspeak.com/channels/1417/field/1/last.json').json()['field1']
        except:
            pass
        if cheerlights != color:
            #New color, do stuff
            if cheerlights == 'red':
                match = True
                newColor = Color(255, 0, 0)
            elif cheerlights == 'green':
                match = True
                newColor = Color(0, 255, 0)
            elif cheerlights == 'blue':
                match = True
                newColor = Color(0, 0, 255)
            elif cheerlights == 'purple':
                match = True
                newColor = Color(102, 51, 204)
            elif cheerlights == 'cyan':
                match = True
                newColor = Color(0, 255, 255)
            elif cheerlights == 'magenta':
                match = True
                newColor = Color(255, 0, 255)
            elif cheerlights == 'yellow':
                match = True
                newColor = Color(255, 255, 0)
            elif cheerlights == 'orange':
                match = True
                newColor = Color(255, 153, 0)
            elif cheerlights == 'pink':
                match = True
                newColor = Color(255, 192, 203)
            elif (cheerlights == 'white' or cheerlights == 'warmwhite' or cheerlights == 'oldlace'):
                match = True
                newColor = Color(255, 255, 255)
            elif (cheerlights == 'black' or cheerlights == 'off'):
                match = True
                newColor = Color(0, 0, 0)
            else:
                match = False
                print 'non-match!'
            if match == True:
                match = False
                #theaterChase(strip, newColor)
                colorWipe(strip, newColor)
                print newColor

                # remove oldest color in history
                #light_history.pop()
                # add new color to top of history
                #light_history.insert(0,newColor)
                # print color list in decimal integer format
                print light_history
                # chase the history across the lights
                #historyChase(strip, light_history)

                color = cheerlights
                time.sleep(16)

        # Theater chase animations. (Use with above or use randomly)
        #theaterChase(strip, Color(127, 127, 127))  # White theater chase
        #theaterChase(strip, Color(127,   0,   0))  # Red theater chase
        #theaterChase(strip, Color(  0, 127,   0))  # Green theater chase
        # Rainbow animations.
        #rainbow(strip)
        #rainbowCycle(strip)
        #theaterChaseRainbow(strip)
        time.sleep(0.1)
