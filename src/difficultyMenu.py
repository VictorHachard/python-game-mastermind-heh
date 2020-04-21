import pygame
from settings import *
from pygame import locals as const
from button import Button
from text import Text
from menu import Menu
from game import Game

class DifficultyMenu(object):
    """docstring for DifficultyMenu. Cette classe est le menu de gestion des difficultée il est """

    def __init__(self, main, screen):
        """"Dans ce constructeur on initialise les variables de classe et on appelle la méthode new(self)"""
        self.main = main
        self.screen = screen
        self.difficultyLvl = 0
        self.new()

    def new(self):
        """cette méthode sert a ajouter les bouttons et textes au menu en fonction des variables de classe dans le constructeur (difficltyLVL)"""
        self.difficultyMenu = Menu(self.screen, 7, 2).addText('Difficulty', 60).addButton('Easy', 'e', GREEN if self.difficultyLvl >= 0 else GREY).addButton('Medium', 'm', GREEN if self.difficultyLvl >= 1 else GREY).addButton('Hard', 'h', GREEN if self.difficultyLvl >= 2 else GREY).addButton('Extreme', 'ex', GREEN if self.difficultyLvl >= 3 else GREY).addButton('Armand', 'a', GREEN if self.difficultyLvl >= 4 else GREY).addButton('Menu', 'menu')

    """les 3 méthodes suivantes sont les méthodes dans lesquelles les tacks sont gérés, ces méthodes sont appellée depuis la méthode run du main"""

    """les 3 méthodes suivantes sont les méthodes dans lesquelles les tacks sont gérés, ces méthodes sont appellée depuis la méthode run du main"""

    def update(self):
        pass

    def draw(self):
        """cette méthode permet de placer les element a render"""
        self.difficultyMenu.render()

    def events(self, event):
        """cette méthode gere les input du clavier et les traite en conséquence"""
        game = False
        res = self.difficultyMenu.update(event)
        if res == 'menu':
            self.main.change = 'mainMenu'
        elif res == 'e' and self.difficultyLvl >= 0:
            game = Game(self.main, self.screen)
        elif res == 'm' and self.difficultyLvl >= 1:
             game = Game(self.main, self.screen, column = 4, row = 4)
        elif res == 'h' and self.difficultyLvl >= 2:
            game = Game(self.main, self.screen, column = 5, row = 5)
        elif res == 'ex' and self.difficultyLvl >= 3:
            game = Game(self.main, self.screen, column = 6, row = 6)
        elif res == 'a' and self.difficultyLvl >= 4:
            game = Game(self.main, self.screen, column = 7, row = 6)
        if res == 'e' or res == 'm' or res == 'h' or res == 'ex' or res == 'a':
            if game:
                self.main.getTask('game')[2] = game
                self.main.change = 'game'
