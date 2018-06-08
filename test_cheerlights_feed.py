# Cheerlights feed test
# Author: David Bradway (david.bradway@gmail.com)
#
# Direct port of N0HIO's python script: https://github.com/koernerd/CheerlightsPi
import time
import requests

# I'm going to use a var to check if I've seen the color before
color = 'black'
cheerlights = color


# Main program logic follows:
if __name__ == '__main__':
    # Read the thingspeak feed to get the current color
    try:
        cheerlights = requests.get('http://api.thingspeak.com/channels/1417/field/1/last.json').json()['field1']
    except:
        print('error')
        pass
    if cheerlights != color:
        #New color, do stuff
        if cheerlights == 'red':
            print('match red')
        elif cheerlights == 'green':
            print('match green')
        elif cheerlights == 'blue':
            print('match blue')
        elif cheerlights == 'purple':
            print('match purple')
        elif cheerlights == 'cyan':
            print('match cyan')
        elif cheerlights == 'magenta':
            print('match magenta')
        elif cheerlights == 'yellow':
            print('match yellow')
        elif cheerlights == 'orange':
            print('match orange')
        elif (cheerlights == 'white' or cheerlights == 'warmwhite'):
            print('match (warm)white')
        elif (cheerlights == 'black' or cheerlights == 'off'):
            print('match black/off')
        else:
            print('non-match!')
        print(cheerlights)
        color = cheerlights
    time.sleep(0.1)
