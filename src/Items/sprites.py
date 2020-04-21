import pygame, sys, math, random, copy
from settings import *
from pygame import locals as const

class Circle(pygame.sprite.Sprite):
    """docstring for Circle."""

    def __init__(self, main, x, y):
        self.main = main
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(DARKGREY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * 16
        self.rect.y = y * 16

    def draw(self):
        if time.time() - self.start > self.delay:
            if self.n == 2:
                self.n = 0
            else:
                self.n += 1
            self.start = time.time()
        self.screen.blit(self.main.anim[self.n], (0, 0))
