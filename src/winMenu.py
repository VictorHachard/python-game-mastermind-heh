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
        self.main = main
        self.screen = screen
        self.new()

    def new(self):
        self.difficultyLvl = 0
        self.winMenu = Menu(self.screen, 3).addText('win', 60).addButton('Menu', 'm').addButton('Quit', 'q')

    def update(self):
        pass

    def draw(self):
        self.winMenu.render()

    def events(self, event):
        game = False
        res = self.winMenu.update(event)
        if res == 'm':
            self.main.change = 'mainMenu'
        elif res == 'q':
            self.main.running = False
