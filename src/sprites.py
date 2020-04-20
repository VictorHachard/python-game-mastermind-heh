import pygame, sys, math, random, copy
from settings import *
from pygame import locals as const

class Circle(pygame.sprite.Sprite):
    """docstring for Circle."""

    def __init__(self, main, x, y):
        self.groups = main.sprites, main.circle
        self.main = main
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(DARKGREY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * 16
        self.rect.y = y * 16
