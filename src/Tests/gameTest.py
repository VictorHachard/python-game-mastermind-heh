import unittest, pygame, random
import sys
sys.path.append('C:\\Users\\benjamin patte\\PycharmProjects\\python-game-heh\\src')
from Menus.game import Game
from main import Main

class GameTest(unittest.TestCase):
    """cette classe test le module game"""

    self.main = Main()
    self.game = Game()

    def testSecretCombi(self):
        a = 4
        b = 6
        self.assertEqual(a , b)

    def testLineValidation(self):
        place, present = game.verification()
        self.assertEqual(place, present)



#la commande a tapper dans le cmd est : py -m unittest gameTest (en etant dans le dossier Tests)