from sense_hat import SenseHat
import json, time, logging

logging.basicConfig(filename="monitorAndDisplay.log", level=logging.INFO)


class SenseTemp:

    # colors
    R = [255, 0, 0]
    G = [0, 255, 0]
    B = [0, 0, 255]

    # temperature levels
    cold = 'cold'
    comfortable = 'comfortable'
    hot = 'hot'

    led_displays = {
        cold: B,
        comfortable: G,
        hot: R
    }

    def __init__(self, json_file):
        with open(json_file, "r+") as f:
            self.temps = json.load(f)
        f.close()
        self.sense = SenseHat()

    def get_temp_level(self, temperature):
        if temperature < self.temps['cold_max']:
            return SenseTemp.cold
        elif temperature < self.temps['comfortable_max']:
            return SenseTemp.comfortable
        else:
            return SenseTemp.hot

    def display_temp(self):
        temp = round(self.sense.get_temperature())
        display_temp = SenseTemp.led_displays[self.get_temp_level(temp)]
        self.sense.show_message(str(temp), text_colour=display_temp)
        logging.info("Temp: {}, level: {}".format(temp, self.get_temp_level(temp)))


if __name__ == '__main__':
    senseTemp = SenseTemp('config.json')
    while True:
        senseTemp.display_temp()
        time.sleep(10)
