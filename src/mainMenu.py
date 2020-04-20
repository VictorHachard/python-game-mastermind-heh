import pygame
from settings import *
from pygame import locals as const
from button import Button
from text import Text
from menu import Menu

class MainMenu(object):
    """docstring for MainMenu."""

    def __init__(self, main, screen):
        self.main = main
        self.screen = screen
        self.colorMode = False
        self.vsPlayer = False
        self.new()

    def new(self):
        self.mainMenu = Menu(self.screen, 5).addText('Mastermind', 60).addButton('Play', 'p')
        if self.colorMode:
            self.mainMenu.addButton('multiple colors: On', 'm')
        else:
            self.mainMenu.addButton('multiple colors: Off', 'm')
        if self.vsPlayer:
            self.mainMenu.addButton('vs: Player 2', 'v')
        else:
            self.mainMenu.addButton('vs: IA', 'v')
        self.mainMenu.addButton('Quit', 'q')

    def update(self):
        pass

    def draw(self):
        self.mainMenu.render()

    def events(self, event):
        res = self.mainMenu.update(event)
        if res == 'q':
            self.main.running = False
        elif res == 'p':
            self.main.change = 'difficultyMenu'
        elif res == 'm':
            self.colorMode = not self.colorMode
            self.new()
        elif res == 'v':
            self.vsPlayer = not self.vsPlayer
            self.new()
