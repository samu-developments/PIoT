from sense_hat import SenseHat
from json import JSONDecodeError

import sys, json, time, logging

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

    # keys in config.json
    config_values = [
        'cold_max',
        'comfortable_min',
        'comfortable_max',
        'hot_min'
    ]

    led_displays = {
        cold: B,
        comfortable: G,
        hot: R
    }

    def __init__(self, sense: SenseHat, json_file: str):
        try:
            with open(json_file, "r+") as f:
                temps: dict = json.load(f)
                f.close()
                self.temps = self.validate_config(temps)
        except FileNotFoundError:
            raise RuntimeError('Error, config file not found')
        except JSONDecodeError:
            raise RuntimeError('Error, could not read config')
        self.sense = sense

    @staticmethod
    def validate_config(temps: dict) -> dict:
        if all(k in SenseTemp.config_values for k in temps.keys()) and \
                all(isinstance(temps[t], int) for t in SenseTemp.config_values):
            return temps
        else:
            raise ValueError("Config values are wrong")

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
        # use provided argument if exists, otherwise default to 'config.json'.
        # eg. python3 my_custom_temp_file.json. TODO: document in README.md
        config = sys.argv[1] if len(sys.argv) > 1 else 'config.json'
        logging.info(config)
        senseTemp = SenseTemp(sense, config)
        while True:
            senseTemp.display_temp()
            time.sleep(10)
    except Exception as e:
        logging.info(e)
        sense.show_message(e.args[0])
