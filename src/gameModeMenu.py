import pygame, time
from settings import *
from pygame import locals as const
from button import Button
from text import Text
from menu import Menu

class GameModeMenu(object):
    """docstring for GameModeMenu."""

    def __init__(self, main, screen):
        self.main = main
        self.screen = screen
        self.colorMode = False
        self.vsPlayer = False
        self.new()

    def new(self):
        self.gameModeMenu = Menu(self.screen, 4).addText('Game mode', 60)
        if self.vsPlayer:
            self.gameModeMenu.addButton('vs: Player 2', 'v')
        else:
            self.gameModeMenu.addButton('vs: IA', 'v')
            if self.colorMode:
                self.gameModeMenu.addButton('multiple colors: On', 'm')
            else:
                self.gameModeMenu.addButton('multiple colors: Off', 'm')
        self.gameModeMenu.addButton('Menu', 'menu')

    def update(self):
        pass

    def draw(self):
        #self.screen.blit(self.main.background_image, (0, 0))
        self.gameModeMenu.render()

    def events(self, event):
        res = self.gameModeMenu.update(event)
        if res == 'menu':
            self.main.change = 'mainMenu'
        elif res == 'm':
            self.colorMode = not self.colorMode
            self.new()
        elif res == 'v':
            self.vsPlayer = not self.vsPlayer
            self.new()
