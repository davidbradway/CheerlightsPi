CheerlightsPi
=============

Control Adafruit NeoPixels using a RaspberryPi and the [Cheerlights](http://www.cheerlights.com) feed!

Clone or download this project at [Github](https://github.com/davidbradway/CheerlightsPi).

## Desription
Last year, I was inspired by [Dave Koerner's NØHIO LOGBOOK](http://n0hio.wordpress.com/2013/12/06/cheerlights-project).

Then I put together a Cheerlights display using a Ubuntu computer, Adafruit FLORA Arduino, and 8 FLORA NeoPixels:
https://www.youtube.com/watch?v=lJNamwgsGlE
https://plus.google.com/photos?pid=5957627945770423090&oid=116675413971505814200

This year, thanks to Tony DiCola's Python wrapper for the the excellent rpi_ws281x library created by Jeremy Garff, I could redo the project and cut out the Arduino!
[Follow the Adafruit guide here to get your NeoPixels working with Raspberry Pi](https://learn.adafruit.com/neopixels-on-raspberry-pi/overview)

## Installation, with some of the Requirements listed
    ./install.sh

## Test Library
    sudo python rpi_ws281x/python/examples/strandtest.py 

## Usage
    sudo python simple.py [COMMAND]
