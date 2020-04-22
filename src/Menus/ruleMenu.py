import pygame
from settings import *
from pygame import locals as const
from Items.button import Button
from Items.text import Text
from Menus.menu import Menu
from Menus.game import Game


class RuleMenu(object):
    """docstring for RuleMenu."""

    def __init__(self, main, screen):
        """"Dans ce constructeur on initialise les variables de classe et on appelle la méthode new(self)"""
        self.main = main
        self.screen = screen
        self.new()

    def new(self):
        """cette méthode sert a ajouter les bouttons et textes au menu en fonction des variables de classe dans le constructeur"""
        self.ruleMenu = Menu(self.screen, self.main, 6)\
                                                        .addText('Rules', 60)\
                                                        .addImage(self.main.load_image(RULES_IMAGES[0]), [800,326])\
                                                        .addText("")\
                                                        .addText("")\
                                                        .addButton('Menu', 'm')

    """les 3 méthodes suivantes sont les méthodes dans lesquelles les tacks sont gérés, ces méthodes sont appellée depuis la méthode run du main"""

    def update(self):
        pass

    def draw(self):
        """cette méthode permet de placer les element a render"""
        bg = self.main.background_image_b if self.main.getTask('settingsMenu')[2].biere else self.main.background_image
        self.screen.blit(bg, (0, 0))
        self.ruleMenu.render()

    def events(self, event):
        """cette méthode gere les input du clavier et les traite en conséquence"""
        res = self.ruleMenu.update(event)
        if res == 'm':
            self.main.change = 'mainMenu'
