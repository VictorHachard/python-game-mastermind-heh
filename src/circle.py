import pygame, sys, math, random
from settings import *
from pygame import locals as const

class Circle(object):
    """docstring for Circle."""

    def __init__(self, screen, colors, x = 0, y = 0, radius = 20):
        super(Circle, self).__init__()
        self.screen = screen
        self.colors = colors
        self.x, self.y = x, y
        self.radius = radius
        self.color = GREY
        self.colorStr = 'grey'
        self.check = False

    def switch(self, order):
        i = 0
        if order == 'desc':
            if self.colorStr == 'grey':
                self.fill(self.colors[len(self.colors) - 1][0]).render()
            else:
                for color in self.colors:
                    if self.colorStr == color[0]:
                        self.fill(self.colors[i-1][0]).render()
                        return
                    i += 1
        elif order == 'asc':
            if self.colorStr == 'grey':
                self.fill(self.colors[0][0]).render()
            else:
                for color in self.colors:
                    if self.colorStr == color[0]:
                        if i+1 >= len(self.colors):
                            self.fill(self.colors[0][0]).render()
                            return
                        else:
                            self.fill(self.colors[i+1][0]).render()
                            return
                    i += 1

    def done(self, check = 0):
        if check == 0:
            return self.check
        else:
            self.check = check
            return self

    def fill(self, color = False):
        if color == False:
            return self.colorStr
        else:
            if isinstance(color, str):
                self.colorStr = color
                for colorInt in self.colors:
                    if colorInt[0] == color:
                        self.color = colorInt[1]
            else:
                self.color = color
            return self

    def size(self, radius = False):
        if radius == False:
            return self.radius
        else:
            self.radius = radius
            return self

    def horizontal(self, x = False):
        if x == False:
            return self.x
        else:
            self.x = x
            return self

    def vertical(self, y = False):
        if y == False:
            return self.y
        else:
            self.y = y
            return self

    def render(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
        return self
