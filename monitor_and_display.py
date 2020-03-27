from sense_hat import SenseHat
from json import JSONDecodeError

import sys, json, time, logging

logging.basicConfig(filename="monitorAndDisplay.log", level=logging.INFO)


class SenseTemp:

    # temperature levels
    cold = 'cold'
    comfortable = 'comfortable'
    hot = 'hot'

    # temp level keys in config.json
    config_values = [
        'cold_max',
        'comfortable_min',
        'comfortable_max',
        'hot_min'
    ]

    # display colors for different temp levels
    led_displays = {
        cold: [0, 0, 255],
        comfortable: [0, 255, 0],
        hot: [255, 0, 0]
    }

    # Open and validate config file
    def __init__(self, sense: SenseHat, json_file: str):
        try:
            with open(json_file, "r+") as f:
                temps: dict = json.load(f)
                self.temps = self.validate_config(temps)
        except FileNotFoundError:
            raise RuntimeError('Error, config file not found')
        except JSONDecodeError:
            raise RuntimeError('Error, could not read config')
        self.sense = sense

    # Check keys and values in provided dictionary (json file)
    # Keys should be in the list of valid entries (config_values)
    # Values should be int
    @staticmethod
    def validate_config(temps: dict) -> dict:
        if all(k in SenseTemp.config_values for k in temps.keys()) and \
                all(isinstance(temps[t], int) for t in SenseTemp.config_values):
            return temps
        else:
            raise ValueError("Config values are wrong")

    # Based on provided config, return temp level as string
    def get_temp_level(self, temperature: int) -> str:
        if temperature < self.temps['cold_max']:
            return SenseTemp.cold
        elif temperature < self.temps['comfortable_max']:
            return SenseTemp.comfortable
        else:
            return SenseTemp.hot

    # TODO: calibrate a bit better?
    # Helper method to get temperature
    def get_real_temperature(self) -> int:
        return round(self.sense.get_temperature() - 10)

    # Get read and display temperature
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
