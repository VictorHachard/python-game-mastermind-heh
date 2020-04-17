import pygame
from pygame import locals as const

class Text(object):

    # Button(screen, 'ENTER', 20, (128, 128, 128), (255, 255, 255), (100, 450))
    def __init__(self, screen):
        super(Text, self).__init__()
        self.screen = screen
        self.x = 0
        self.y = 0

    def createText(self, point, text, fontSize = 40, colorText = (255, 255, 255)):
        if self.x == 0:
            self.x = point[0]
        self.y = point[1]
        font = pygame.font.SysFont('comicsans', fontSize)
        self.text = font.render(text, 1, colorText)
        self.textWidth = self.text.get_width()
        self.textHeight = self.text.get_height()
        if self.x == -1:
            self.x = 640/2 - self.text.get_width()/2
        return self

    def render(self):
        self.show = self.screen.blit(self.text, (self.x, self.y))
        return self

    def center(self):
        self.x = -1
        return self

    def getText(self):
        return self.show
