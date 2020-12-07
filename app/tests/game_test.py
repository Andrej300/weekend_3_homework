import unittest
from app.models.game import *

class TestGame(unittest.TestCase):

    def test_game_1(self):
        self.assertEqual("The winner is Tom", play_game_and_compare("Rock","Paper")

    # def test_game_2(self):
    #     self.assertEqual("The winner is Tom", play_game_and_compare("Rock","Scissors")

    # def test_game_3(self):
    #     self.assertEqual("The winner is Tom", play_game_and_compare("Scissors","Paper")

    # def test_game_4(self):
    #     self.assertEqual("None", play_game_and_compare("Scissors", "Scissors")