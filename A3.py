from microbit import *
from gesture import *
import music
import neopixel
import radio

#Sets array value to a non-existing value; -1
i = -1
#Read
gesture = Gesture()
#neopixel is attached to pin0 and set 15 pixels to light
np = neopixel.NeoPixel(pin0, 15)
#turn on radio
radio.on()

#Set an array of notes to display
notes = ["E", "A", "D", "G", "B", "e"]
#Set an array of tunes to based on notes array; in format of notes:duration of notes being played
#tune = ["E4:8", "A4:8", "D4:8", "G4:8", "B4:8", "E5:8"]
#set neopixel light value to be blank at the start of the code
blank = (0, 0, 0)

#displays music quaver
display.show(Image.MUSIC_QUAVERS)
#display neopixel
np.show()

while True:
    #reads gesture activity
    g = gesture.read()

    #if gesture reads "none", pixel_id will show blank in descending order of neopixel location every 0.1 second
    if g == 'none':
        for pixel_id in reversed(range(0, len(np))):
            if len(np) > (pixel_id):
                np[pixel_id] = blank
                np.show()
                sleep(100)

    #in section below, it will read the gesture (up or down) and increase/decrease in index value
    #if gesture reads "up" and is smaller than amount of notes it will go up by 1
    if g == 'down' and i < (len(notes) - 1):
        i = i + 1
        display.scroll(notes[i])
        radio.send(str(i))

    #if gesture reads "down" and is bigger than 0 it will go down by 1
    elif g == 'up' and i > 0:
        i = i - 1
        display.scroll(notes[i])
        radio.send(str(i))

    #if gesture reads "up" and is exactly amount of notes, the index value will reset to 0
    elif g == 'down' and i == (len(notes) - 1):
        i = 0
        display.scroll(notes[i])
        radio.send(str(i))


    #if gesture reads "down" and is exactly 0, the index value will reset to it's maximum value
    #if gesture reads "down" and is exactly -1 (non-existing value), it will reset to maximum value
    elif g == 'up' and i == 0 or g == 'up' and i == -1:
        i = (len(notes) - 1)
        display.scroll(notes[i])
        radio.send(str(i))

    #this code only works if i have an existing value and is not -1
    #if the value exists and gesture reads left, it will take the i value
    if g == 'right' and i != -1:
        i = i
        radio.send('up')
        #loops the pixels and light them up in ascending order
        for pixel_id in range(0, len(np)):
            if len(np) > (pixel_id):
                #red
                color = [(255 - (pixel_id * 15),pixel_id * 3,pixel_id * 2),
                #green
                (pixel_id * 3 ,255 - (pixel_id * 15), pixel_id * 3),
                #blue
                (pixel_id * 3 , pixel_id * 3, 255 - (pixel_id * 15)),
                #purple
                (100 + (pixel_id * 10), pixel_id * 12, 150 + (pixel_id * 6)),
                #IDK WHAT COLOR
                (100, 150, 54),
                #turquoise
                (pixel_id * 10, 120 + (pixel_id * 8), 83 + (pixel_id * 7))]
                np[pixel_id] = color[i]
                np.show()
                sleep(100)
            #loops the pixels and remove the lights in ascending order
            if len(np) == (pixel_id + 1):
                for pixel_id in range(0, len(np)):
                    np[pixel_id] = blank
                    np.show()
                    sleep(100)
            #if the neopixel is not lighted up
            #loops the pixels and light neopixel in descending order
            if np[pixel_id] == blank:
                for pixel_id in reversed(range(0, (len(np)))):
                    #red
                    color = [(255 - (pixel_id * 15),pixel_id * 3,pixel_id * 2),
                    #green
                    (pixel_id * 3 ,255 - (pixel_id * 15), pixel_id * 3),
                    #blue
                    (pixel_id * 3 , pixel_id * 3, 255 - (pixel_id * 15)),
                    #purple
                    (100 + (pixel_id * 10), pixel_id * 12, 150 + (pixel_id * 6)),
                    #IDK WHAT COLOR
                    (100, 150, 54),
                    #turquoise
                    (pixel_id * 10, 120 + (pixel_id * 8), 83 + (pixel_id * 7))]
                    np[pixel_id] = color[i]
                    np.show()
                    sleep(100)
        #plays a tune and ensure that it is only being played once after all light has been turned
        #music.play(tune[i])