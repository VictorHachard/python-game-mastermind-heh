import pygame
from settings import *
from pygame import locals as const
from Items.button import Button
from Items.text import Text
from Menus.menu import Menu
from Menus.game import Game


class WinMenu(object):
    """docstring for WinMenu."""

    def __init__(self, main, screen):
        """"Dans ce constructeur on initialise les variables de classe et on appelle la méthode new(self)"""
        self.main = main
        self.screen = screen
        self.newUpdate = False
        self.new()

    def new(self):
        """cette méthode sert a ajouter les bouttons et textes au menu en fonction des variables de classe dans le constructeur"""
        self.winMenu = Menu(self.screen, self.main, 7).addText('Win', 60).addText('Special unlock', 50).addText('').addText('').addText('')
        if self.main.getTask('game') != None and self.main.getTask('game')[2].vsPlayer2:
            if self.main.getTask('game')[2].player1Score < self.main.getTask('game')[2].player2Score:
                self.winMenu.addText('Player 2 has win', 40)
            elif self.main.getTask('game')[2].player1Score > self.main.getTask('game')[2].player2Score:
                self.winMenu.addText('Player 1 has win', 40)
            else:
                self.winMenu.addText('Player 1 and 2 have the same score', 40)
        self.winMenu.addButton('Menu', 'm')

    """les 3 méthodes suivantes sont les méthodes dans lesquelles les tacks sont gérés, ces méthodes sont appellée depuis la méthode run du main"""

    def update(self):
        if self.newUpdate:
            self.main.effects_sounds['victory'].play()
            self.newUpdate = not self.newUpdate

    def draw(self):
        """cette méthode permet de placer les element a render"""
        bg = self.main.background_image_b if self.main.getTask('settingsMenu')[2].biere else self.main.background_image
        self.screen.blit(bg, (0, 0))
        self.screen.blit(self.main.bottle[self.main.getTask('game')[2].boss - 1], (300, 220))
        self.winMenu.render()

    def events(self, event):
        """cette méthode gere les input du clavier et les traite en conséquence"""
        game = False
        res = self.winMenu.update(event)
        if res == 'm':
            self.main.change = 'mainMenu'
