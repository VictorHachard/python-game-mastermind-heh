import pygame
from settings import *
from pygame import locals as const

class Button(object):
    """docstring for Button."""

    def __init__(self, screen, main):
        self.screen = screen
        self.main = main
        self.x = 0
        self.y = 0

    def createButton(self, point, text, fontSize = 40, colorRect = GREY, colorText = BLACK, menu = True, petit = False, test = 4):
        """Create the object Text, return this"""
        if self.x == 0:
            self.x = point[0]
        self.y = point[1]
        self.menu = menu
        self.petit = petit
        self.test = test
        self.colorRect = colorRect
        font = pygame.font.SysFont('comicsans', fontSize)
        self.text = font.render(text, 1, colorText)
        self.textWidth = self.text.get_width()
        self.textHeight = self.text.get_height()
        if self.x == -1:
            self.x = WIDTH/2 - self.text.get_width()/2
        return self

    def render(self):
        """Render this object, return this"""
        if self.menu:
            self.rect = pygame.draw.rect(self.screen, self.colorRect, (WIDTH // 2 - 316 // 2, self.y - 14, 316, 73), 0)
            btn = self.main.button_b if self.main.getTask('settingsMenu')[2].biere else self.main.button
            self.screen.blit(btn, (WIDTH // 2 - 316 // 2, self.y - 14))
        else:
            btn = self.main.pbutton_b if self.main.getTask('settingsMenu')[2].biere else self.main.pbutton
            self.rect = pygame.draw.rect(self.screen, self.colorRect, (WIDTH / self.test - 20, HEIGHT - 75, 160, 70), 0)
            self.screen.blit(btn, (WIDTH / self.test - 20, HEIGHT - 75))
        self.screen.blit(self.text, (self.x, self.y))
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

    def getButton(self):
        """Return the pygame Button"""
        return self.rect
