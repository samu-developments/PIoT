from sense_hat import SenseHat
from random import randint
import time


class SenseDie:
    def __init__(self):
        self.sense = SenseHat()
        self.sense.low_light = True

    # roll dice; detect big changes in accelerometer
    # get two readings from accelerometer (with a small pause between) and detect difference
    def detect_roll(self) -> int:
        self.sense.clear()
        accelerometer = self.get_acc()
        time.sleep(.05)
        accelerometer2 = self.get_acc()

        while not SenseDie.was_shaken(accelerometer, accelerometer2):
            time.sleep(.05)
            accelerometer = accelerometer2
            accelerometer2 = self.get_acc()

        roll = randint(1, 6)
        self.display_roll(roll)
        return roll

    def get_acc(self) -> (float, float, float):
        acc = self.sense.get_accelerometer_raw()
        return acc['x'], acc['y'], acc['z']

    @staticmethod
    def was_shaken(acc_1: tuple, acc_2: tuple) -> bool:
        x1, y1, z1 = acc_1
        x2, y2, z2 = acc_2
        return abs(sum([x1 - x2, y1 - y2, z1 - z2])) > 2.5

    # show rolled die. TODO: add fancy dices and rolling graphic
    def display_roll(self, number):
        self.sense.show_letter(str(number))


die = SenseDie()

while True:
    die.detect_roll()
    time.sleep(3)
