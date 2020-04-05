from typing import List
from time import sleep

from sense_hat import SenseHat


class SenseEmoji:
    def __init__(self, sense: SenseHat, face: List[List[int]]):
        self.sense = sense
        self.face = face

    def display(self):
        self.sense.set_pixels(self.face)


if __name__ == '__main__':
    sense = SenseHat()

    y = [60, 60, 0]  # Yellow, a bit duller so easier to see rest of the emoji..
    r = [255, 0, 0]   #Red
    c = [0, 255, 255]  #Cyan
    
    smile = [
       y, y, y, y, y, y, y, y,
       y, y, y, y, y, y, y, y,
       y, c, c, y, y, c, c, y,
       y, c, c, y, y, c, c, y,
       y, y, y, y, y, y, y, y,
       y, r, r, y, y, r, r, y,
       y, y, y, r, r, y, y, y,
       y, y, y, y, y, y, y, y
    ]
    tongue_out = [
       y, y, y, y, y, y, y, y,
       y, y, y, y, y, y, y, y,
       y, r, r, y, y, r, r, y,
       y, r, r, y, y, r, r, y,
       y, y, y, y, y, y, y, y,
       y, r, r, r, r, r, r, y,
       y, y, y, c, c, y, y, y,
       y, y, y, c, c, y, y, y
    ]
    sad = [
       y, y, y, y, y, y, y, y,
       y, y, y, y, y, y, y, y,
       y, c, c, y, y, c, c, y,
       y, c, c, y, y, c, c, y,
       y, y, y, y, y, y, y, y,
       y, y, y, r, r, y, y, y,
       y, r, r, y, y, r, r, y,
       y, y, y, y, y, y, y, y
    ]
    emojis = [
        SenseEmoji(sense, smile),
        SenseEmoji(sense, tongue_out),
        SenseEmoji(sense, sad)
    ]

    while len(sense.stick.get_events()) == 0:
        for emoji in emojis:
            emoji.display()
            sleep(3)
    sense.clear()
