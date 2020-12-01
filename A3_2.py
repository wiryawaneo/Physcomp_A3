from microbit import *
import music
import radio
import speech

radio.on() #required to turn on bluetooth


#do two different variable, one to show the notes, the other to do the solfa
#notes change through left/right while solfa only plays when up
notes = ["E", "A", "D", "G", "B", "e"]
newNote = -1
solfa = [
    "#94PLAEYYY #94LOHWWWW #94IYIYIYIYIY #94NAATTTT",    # Mi/LOW E
    "#70PLAEYYY #70DHEHEH #70AEAEAEAE #70NAATTTT",  # La /  A
    "#52PLAEYYY #52DHEHEH #52DIYIYIYIY #52NAATTTTTT",    # Rey / D
    "#39PLAEYYY #39DHEHEH #39GIYIYIY #39NAATTTTTT",    # So / G
    "#31PLAEYYY #31DHEHEH #31BIYIYIY #31NAATTTTT",    # Ti / B
    "#23PLAEYY #23/HAYYYYY #23IYIYIYIY #23NAATTTTTT",    # Mi/ High E
]
display.show(Image.MUSIC_QUAVERS)

while True:
    incoming = radio.receive()
    if incoming != None and incoming != 'up':
        newNote = int(incoming)
        display.show(notes[newNote])
    if incoming == 'up' and newNote != -1:
        speech.sing(solfa[newNote])