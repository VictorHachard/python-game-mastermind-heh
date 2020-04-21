import pygame, time
from settings import *
from pygame import locals as const
from button import Button
from text import Text
from menu import Menu

class ScoreMenu(object):
    """docstring for ScoreMenu."""

    def __init__(self, main, screen):
        self.main = main
        self.screen = screen
        self.start = time.time()
        self.file = "score.txt"
        self.score = 0
        self.score = self.read_file()
        self.new()

    def addScore(self, i = 1):
        self.score += i
        self.new()
        self.write_file()

    def write_file(self):
        prev = self.read_file()
        if prev < self.score:
            with open(self.file, 'w') as fp:
                fp.write(str(self.score))

    def read_file(self):
        with open(self.file) as fp:
            score = int(fp.read())
            return score

    def new(self):
        self.scoreMenu = Menu(self.screen, 5).addText('High score', 60).addText(str(self.score), 40).addButton('Menu', 'm')

    def update(self):
        pass

    def draw(self):
        #self.screen.blit(self.main.background_image, (0, 0))
        self.scoreMenu.render()

    def events(self, event):
        res = self.scoreMenu.update(event)
        if res == 'm':
            self.main.change = 'mainMenu'
