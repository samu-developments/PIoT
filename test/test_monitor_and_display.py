import unittest, sys, os

from unittest.mock import Mock

sys.modules['sense_hat'] = Mock()  # mock whole sense-hat module, which is imported below

from task_b.monitor_and_display import SenseTemp


test_dir = os.path.abspath(os.path.dirname(__file__))


class TestMonitor(unittest.TestCase):

    def test_validate_config_wrong_config_filename(self):
        try:
            SenseTemp(Mock(), test_dir + '/wrong_filename')
        except RuntimeError as e:
            self.assertEqual(e.args[0], 'Error, config file not found')

    def test_validate_config_wrong_config_parameters(self):
        try:
            SenseTemp(Mock(), test_dir + '/config_corrupt.json')
        except RuntimeError as e:
            self.assertEqual(e.args[0], 'Error, could not read config')

        try:
            SenseTemp(Mock(), test_dir + '/config_wrong_key.json')
        except ValueError as e:
            self.assertEqual(e.args[0], 'Config values are wrong')

        try:
            SenseTemp(Mock(), test_dir + '/config_wrong_value_type.json')
        except ValueError as e:
            self.assertEqual(e.args[0], 'Config values are wrong')

        try:
            SenseTemp(Mock(), test_dir + '/config_wrong_value.json')
        except ValueError as e:
            self.assertEqual(e.args[0], 'Config values are wrong')

    def test_validate_config_valid_config(self):
        try:
            SenseTemp(Mock(), test_dir + '/config.json')
        except Exception:
            self.fail("Failed initializing valid config.json")