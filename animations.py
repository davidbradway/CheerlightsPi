def makeGreen(strip):
    """Make is all green"""
    colorWipe(strip, Color(0, 255, 0), 0)

def wait(strip, R, G, B, wait_ms=50, iterations=1):
    """Spinning waiting animation."""
    // number of times to spin around
    for j in range(iterations):
        // shift which pixel to start on
        for i in range(0, strip.numPixels()):
            // set the color/brightness of the pixels
            for k in range(0, strip.numPixels()):
                strip.setPixelColor(i+k % strip.numPixels, 
                                    Color(floor(R*k/(strip.numPixels()-1)),
                                          floor(G*k/(strip.numPixels()-1)),
                                          floor(B*k/(strip.numPixels()-1))))
            strip.show()
            time.sleep(wait_ms/1000.0)
