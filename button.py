import pygame
from pygame import locals as const

class Button(object):

    # Button(screen, 'ENTER', 20, (128, 128, 128), (255, 255, 255), (100, 450))
    def __init__(self, screen):
        super(Button, self).__init__()
        self.screen = screen
        self.x = 0
        self.y = 0

    def createButton(self, point, text, fontSize = 40, colorRect = (128, 128, 128), colorText = (255, 255, 255)):
        if self.x == 0:
            self.x = point[0]
        self.y = point[1]
        self.colorRect = colorRect
        font = pygame.font.SysFont('comicsans', fontSize)
        self.text = font.render(text, 1, colorText)
        self.textWidth = self.text.get_width()
        self.textHeight = self.text.get_height()
        if self.x == -1:
            self.x = 640/2 - self.text.get_width()/2
        return self

    def render(self):
        self.rect = pygame.draw.rect(self.screen, self.colorRect, (self.x, self.y, self.text.get_width(), self.text.get_height()), 0)
        self.button = self.screen.blit(self.text, (self.x, self.y))
        return self

    def center(self):
        self.x = -1
        return self

    def isMouseIn(self, pos):
        if self.button.collidepoint(pos):
            return True
        else:
            return False

    def getButton(self):
        return self.button
