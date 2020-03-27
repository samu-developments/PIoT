import unittest, sys, os

from unittest.mock import Mock

sys.modules['sense_hat'] = Mock()  # mock whole sense-hat module, which is imported below

from monitor_and_display import SenseTemp


class TestMonitor(unittest.TestCase):

    def test_wrong_config(self):
        try:
            SenseTemp(Mock(), 'wrong_filename')
        except RuntimeError as e:
            self.assertEqual(e.args[0], 'Error, config file not found')

        try:
            SenseTemp(Mock(), os.getcwd() + '/config_corrupt.json')
        except RuntimeError as e:
            self.assertEqual(e.args[0], 'Error, could not read config')

        try:
            SenseTemp(Mock(), os.getcwd() + '/config_wrong_key.json')
        except RuntimeError as e:
            self.assertEqual(e.args[0], 'Config values are wrong')

        try:
            SenseTemp(Mock(), 'config_wrong_value.json')
        except RuntimeError as e:
            self.assertEqual(e.args[0], 'Config values are wrong')

        try:
            SenseTemp(Mock(), os.getcwd() + 'config.json')
        except Exception:
            self.fail("Failed initializing valid config.json")