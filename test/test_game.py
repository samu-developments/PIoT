import unittest, sys, os

from unittest.mock import Mock

sys.modules['sense_hat'] = Mock()  # mock whole sense-hat module, which is imported below

from sense_hat import SenseHat

from task_c.game import DieGame


class TestGame(unittest.TestCase):

    # TODO:
    def test_game(self):
        game = DieGame(SenseHat(), 10)
        self.assertTrue(True)