import pygame, sys, math, random
from settings import *
from pygame import locals as const

class Circle(object):
    """docstring for Circle."""

    def __init__(self, main, screen, colors, x = 0, y = 0, radius = 30):
        self.screen = screen
        self.main = main
        self.colors = colors
        self.x, self.y = x, y
        self.radius = radius
        self.color = GREY
        self.colorStr = 'grey'
        self.check = False

    def switch(self, order):
        """Swith the color in the color list asc or desc, return this"""
        i = 0
        if order == 'desc':
            if self.colorStr == 'grey':
                self.fill(self.colors[len(self.colors) - 1][0]).render()
            else:
                for color in self.colors:
                    if self.colorStr == color[0]:
                        self.fill(self.colors[i-1][0]).render()
                        return self
                    i += 1
        elif order == 'asc':
            if self.colorStr == 'grey':
                self.fill(self.colors[0][0]).render()
            else:
                for color in self.colors:
                    if self.colorStr == color[0]:
                        if i+1 >= len(self.colors):
                            self.fill(self.colors[0][0]).render()
                            return self
                        else:
                            self.fill(self.colors[i+1][0]).render()
                            return self
                    i += 1
        return self

    def done(self, check = 0):
        """Store a bool True if the circle is check, return this"""
        if check == 0:
            return self.check
        else:
            self.check = check
            return self

    def fill(self, color = False):
        """Fill the color in the circle, the color can be given as COLOR or string, return this"""
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
        """Set the radius of the circle, return this"""
        if radius == False:
            return self.radius
        else:
            self.radius = radius
            return self

    def horizontal(self, x = False):
        """Set the horizontal value of the circle, return this"""
        if x == False:
            return self.x
        else:
            self.x = x
            return self

    def vertical(self, y = False):
        """Set the vertical value of the circle, return this"""
        if y == False:
            return self.y
        else:
            self.y = y
            return self

    def render(self):
        """Render the circle, return this"""
        self.screen.blit(pygame.transform.scale(self.main.hole, (self.radius * 2 + self.radius//2, self.radius * 2 + self.radius//2)), (self.x - self.radius, self.y - self.radius))
        if not self.colorStr == 'grey' and not self.color == DARKGREY:
            self.screen.blit(pygame.transform.scale(self.main.balls[self.colorStr], (self.radius * 2 + self.radius//2, self.radius * 2 + self.radius//2)), (self.x - self.radius, self.y - self.radius))
        elif self.color == DARKGREY:
            self.screen.blit(pygame.transform.scale(self.main.balls['darkgrey'], (self.radius * 2 + self.radius//2, self.radius * 2 + self.radius//2)), (self.x - self.radius, self.y - self.radius))
        #pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
        return self
