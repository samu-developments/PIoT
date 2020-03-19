from sense_hat import SenseHat
import threading
import time
 
# to execute sense function

def t1():
    sense = SenseHat()

# display is 8x8 pixels

O = [0, 0, 255]

# cold blue

temperature_cold = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
]

sense.set_pixels(temperature_cold)

O = [0, 255, 0]

# comfortable green

temperature_comfortable = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
]

sense.set_pixels(temperature_comfortable)

O = [255, 0, 0]

# hot red

temperature_hot = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
]

sense.set_pixels(temperature_hot)
 
# to make it everty 10 seconds
def t2():
    while 1:
        t1()
        time.sleep(10)
 
if __name__ == '__main__':
    t = threading.Thread(target=t2)
    t.start()


