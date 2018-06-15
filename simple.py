#!/usr/bin/env python
# -*- coding: latin-1 -*-

#  NeoPixel/ rpi_ws281x library created by Jeremy Garff.
import time
from neopixel import *

from animations import *

# LED strip configuration:
LED_COUNT   = 12      # CHANGEME! Number of LED pixels.
LED_PIN     = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA     = 5       # DMA channel to use for generating signal (try 5)
LED_INVERT  = False   # True to invert the signal (when using NPN transistor level shift)

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

# Main program logic follows:
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("cheerlights", help="enter a color")
    args = parser.parse_args()
    anim = args.cheerlights

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    if anim == 'off':
        off = Color(0, 0, 0)
        colorWipe(strip, off, 0)
    elif anim == 'makeGreen':
        makeGreen(strip)
    elif anim == 'waiting':
        waiting(strip, 0, 0, 255, 50, 5)
    elif anim == 'sleepAnimation':
        sleepAnimation(strip)
    elif anim== 'getAttention':
        getAttention(strip)
    time.sleep(0.1)
