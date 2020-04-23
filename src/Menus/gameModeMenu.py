import pygame
from settings import *
from pygame import locals as const
from Items.button import Button
from Items.text import Text
from Menus.menu import Menu
from Menus.game import Game

class GameModeMenu(object):
    """docstring for GameModeMenu."""

    def __init__(self, main, screen):
        """"Dans ce constructeur on initialise les variables de classe et on appelle la méthode new(self)"""
        self.main = main
        self.screen = screen
        self.colorMode = False
        self.vsPlayer = False
        self.vsPlayer2 = False
        self.new()

    def new(self):
        """cette méthode sert a ajouter les bouttons et textes au menu en fonction des variables de classe dans le constructeur"""
        self.gameModeMenu = Menu(self.screen, self.main, 6).addText('Game mode', 60)
        if self.vsPlayer2:
            self.gameModeMenu.addButton('2 players', 'v2')
        else:
            self.gameModeMenu.addButton('1 player', 'v2')
        if self.vsPlayer:
            if self.vsPlayer2:
                self.gameModeMenu.addButton('VS: Player', 'v').addText('', 0)
            else:
                self.gameModeMenu.addButton('Sandbox', 'v').addText('', 0)
        else:
            self.gameModeMenu.addButton('VS: IA', 'v')
            if self.colorMode:
                self.gameModeMenu.addButton('MultiColor: On', 'm')
            else:
                self.gameModeMenu.addButton('MultiColor: Off', 'm')
        self.gameModeMenu.addButton('Menu', 'menu')

    """les 3 méthodes suivantes sont les méthodes dans lesquelles les tacks sont gérés, ces méthodes sont appellée depuis la méthode run du main"""

    def update(self):
        pass

    def draw(self):
        """cette méthode permet de placer les element a render"""
        bg = self.main.background_image_b if self.main.getTask('settingsMenu')[2].biere else self.main.background_image
        self.screen.blit(bg, (0, 0))
        self.gameModeMenu.render()

    def events(self, event):
        """cette méthode gere les input du clavier et les traite en conséquence"""
        res = self.gameModeMenu.update(event)
        if res == 'menu':
            self.main.change = 'mainMenu'
        elif res == 'm':
            self.colorMode = not self.colorMode
            self.new()
        elif res == 'v':
            self.vsPlayer = not self.vsPlayer
            self.new()
        elif res == 'v2':
            self.vsPlayer2 = not self.vsPlayer2
            self.new()
