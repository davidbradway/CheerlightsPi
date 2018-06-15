def makeGreen(strip):
    """Make is all green"""
    colorWipe(strip, Color(0, 255, 0), 0)

def waiting(strip, R, G, B, wait_ms=50, iterations=1):
    """Spinning waiting animation."""
    # number of times to spin around
    for j in range(iterations):
        # shift which pixel to start on
        for i in range(0, strip.numPixels()):
            # set the color/brightness of the pixels
            for k in range(0, strip.numPixels()):
                strip.setPixelColor(i+k % strip.numPixels, 
                                    Color(floor(R*k/(strip.numPixels()-1)),
                                          floor(G*k/(strip.numPixels()-1)),
                                          floor(B*k/(strip.numPixels()-1))))
            strip.show()
            time.sleep(wait_ms/1000.0)

def sleepAnimation(strip, wait_ms=50, iterations=1):
    """Fade in and out blue."""
    for k in range(0, strip.numPixels()):
        strip.setPixelColor(k, Color(0, 0, 255))
    for j in range(iterations):
        # set the color/brightness of the pixels
        for brightness in range(0, 255):
            # set the brightness of the pixels
            setBrightness(brightness)
            strip.show()
            time.sleep(wait_ms/1000.0)
        for brightness in range(255, 0, -1):
            # set the brightness of the pixels
            setBrightness(brightness)
            strip.show()
            time.sleep(wait_ms/1000.0)

def getAttention(strip, wait_ms=50, iterations=10):
    """Alternate green and yellow"""
    for j in range(iterations):
        # half of the pixels shall be green
        for k in range((0 + j) % 2, strip.numPixels(), 2):
            strip.setPixelColor(k, Color(0, 255, 0))
        # and the other half yellow
        for k in range((1 + j) % 2, strip.numPixels(), 2):
            strip.setPixelColor(k, Color(255, 255, 0))
        strip.show()
        time.sleep(wait_ms/1000.0)
