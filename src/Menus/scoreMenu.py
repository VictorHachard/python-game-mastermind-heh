import pygame, time
from settings import *
from pygame import locals as const
from Items.button import Button
from Items.text import Text
from Menus.menu import Menu
from Menus.game import Game

class ScoreMenu(object):
    """docstring for ScoreMenu."""

    def __init__(self, main, screen):
        """"Dans ce constructeur on initialise les variables de classe et on appelle la méthode new(self)"""
        self.main = main
        self.screen = screen
        self.start = time.time()
        self.file = "./score.txt"
        self.file2 = "./bottle.txt"
        self.score = 0
        self.score = self.read_file(self.file)
        self.bottle = 0
        self.bottle = self.read_file(self.file2)
        self.new()

    def addScore(self, i = 1):
        self.score += i
        self.new()
        self.write_file()

    def addBottle(self, i = 1):
        self.bottle += i
        self.new()
        self.write_file()

    def write_file(self):
        prev = self.read_file(self.file)
        if prev < self.score:
            with open(self.file, 'w') as fp:
                fp.write(str(self.score))
        with open(self.file2, 'w') as fp:
            fp.write(str(self.bottle))

    def read_file(self, file):
        with open(file) as fp:
            score = int(fp.read())
            return score

    def new(self):
        """cette méthode sert a ajouter les bouttons et textes au menu en fonction des variables de classe dans le constructeur"""
        self.scoreMenu = Menu(self.screen, self.main, 6).addText('High score', 60).addText(str(self.score), 40).addText('Special unlock', 50).addText('').addText('').addButton('Menu', 'm')

    """les 3 méthodes suivantes sont les méthodes dans lesquelles les tacks sont gérés, ces méthodes sont appellée depuis la méthode run du main"""

    def update(self):
        pass

    def draw(self):
        """cette méthode permet de placer les element a render"""
        bg = self.main.background_image_b if self.main.getTask('settingsMenu')[2].biere else self.main.background_image
        self.screen.blit(bg, (0, 0))
        for i in range(self.bottle):
            self.screen.blit(self.main.bottle[i], ((((WIDTH - 200) //4) + i * ((WIDTH - 200) //4)) - 150, 320))
        self.scoreMenu.render()

    def events(self, event):
        """cette méthode gere les input du clavier et les traite en conséquence"""
        res = self.scoreMenu.update(event)
        if res == 'm':
            self.main.change = 'mainMenu'
