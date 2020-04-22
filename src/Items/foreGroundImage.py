import pygame
from settings import *
from pygame import locals as const

class ForeGroundImage(object):
    """docstring for Image."""

    def __init__(self, screen, main):
        self.screen = screen
        self.main = main
        self.x = 0
        self.y = 0

    def createImage(self, point, image, size):
        """Create the object Text, return this"""
        self.image = pygame.transform.scale(image, (size[0], size[1]))
        if self.x == 0:
            self.x = point[0]
        self.y = point[1]
        if self.x == -1:
            self.x = WIDTH/2 - self.image.get_width()/2
        return self

    def render(self):
        """Render this object, return this"""
        self.screen.blit(self.image, (self.x, self.y))
        return self

    def center(self):
        """Center the Button on the horizontal axis, return this"""
        self.x = -1
        return self

    def isMouseIn(self, pos):
        """Return true if the mouse is colliding with the button"""
        if self.rect.collidepoint(pos):
            return True
        else:
            return False

    def getImage(self):
        """Return the pygame Button"""
        return self.rect
