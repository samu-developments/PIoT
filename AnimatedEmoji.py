from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

y = (255, 255, 0) #Yellow
r = (255, 0, 0)   #Red
c = (0, 255, 255) #Cyan
    
smiley_face = [
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

sad_face = [
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, c, c, y, y, c, c, y,
   y, c, c, y, y, c, c, y,
   y, y, y, y, y, y, y, y,
   y, y, y, r, r, y, y, y,
   y, r, r, y, y, r, r, y,
   y, y, y, y, y, y, y, y
]
    

while True:
    sense.set_pixels(smiley_face)
    sleep(3)
    sense.set_pixels(tongue_out)
    sleep(3)
    sense.set_pixels(sad_face)
    sleep(3)