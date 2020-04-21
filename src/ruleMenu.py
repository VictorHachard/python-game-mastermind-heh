import pygame
from settings import *
from pygame import locals as const
from button import Button
from text import Text
from menu import Menu

class RuleMenu(object):
    """docstring for RuleMenu."""

    def __init__(self, main, screen):
        self.main = main
        self.screen = screen
        self.new()

    def new(self):
        self.ruleMenu = Menu(self.screen, 2).addText('Rules', 60).addButton('Menu', 'm')

    def update(self):
        pass

    def draw(self):
        self.ruleMenu.render()

    def events(self, event):
        res = self.ruleMenu.update(event)
        if res == 'm':
            self.main.change = 'mainMenu'
