import pygame
import os

pygame.font.init()
pygame.init()

class Game:
    def __init__(self, win):
        self.width = 1350
        self.height = 700
        self.win = win
        self.pause = True
        self.music_on = True
