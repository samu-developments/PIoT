from sense_hat import SenseHat
from json import JSONDecodeError

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

    def __init__(self, sense: SenseHat, json_file: str):
        try:
            with open(json_file, "r+") as f:
                self.temps = json.load(f)
                f.close()
        except FileNotFoundError:
            raise RuntimeError('Error, config file not found')
        except JSONDecodeError:
            raise RuntimeError('Error, could not read config')
        self.sense = sense

    def get_temp_level(self, temperature):
        if temperature < self.temps['cold_max']:
            return SenseTemp.cold
        elif temperature < self.temps['comfortable_max']:
            return SenseTemp.comfortable
        else:
            return SenseTemp.hot

    # TODO: calibrate a bit better?
    def get_real_temperature(self) -> int:
        return round(self.sense.get_temperature() - 10)

    def display_temp(self):
        temp = self.get_real_temperature()
        display_temp = SenseTemp.led_displays[self.get_temp_level(temp)]
        self.sense.show_message(str(temp), text_colour=display_temp)
        logging.info("Temp: {}, level: {}".format(temp, self.get_temp_level(temp)))


if __name__ == '__main__':
    sense = SenseHat()
    try:
        senseTemp = SenseTemp(sense, 'config.json')
        while True:
            senseTemp.display_temp()
            time.sleep(10)
    except Exception as e:
        logging.info(e)
        sense.show_message(e.args[0])
