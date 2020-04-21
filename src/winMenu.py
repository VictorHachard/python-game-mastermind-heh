import pygame
from settings import *
from pygame import locals as const
from button import Button
from text import Text
from menu import Menu
from game import Game

class WinMenu(object):
    """docstring for WinMenu."""

    def __init__(self, main, screen):
        """"Dans ce constructeur on initialise les variables de classe et on appelle la méthode new(self)"""
        self.main = main
        self.screen = screen
        self.new()

    def new(self):
        """cette méthode sert a ajouter les bouttons et textes au menu en fonction des variables de classe dans le constructeur"""
        self.difficultyLvl = 0
        self.winMenu = Menu(self.screen, 6).addText('win', 60).addButton('Menu', 'm')

    """les 3 méthodes suivantes sont les méthodes dans lesquelles les tacks sont gérés, ces méthodes sont appellée depuis la méthode run du main"""

    def update(self):
        pass

    def draw(self):
        """cette méthode permet de placer les element a render"""
        self.winMenu.render()

    def events(self, event):
        """cette méthode gere les input du clavier et les traite en conséquence"""
        game = False
        res = self.winMenu.update(event)
        if res == 'm':
            self.main.change = 'mainMenu'
