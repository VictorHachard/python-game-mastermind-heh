import pygame
from pygame import locals as const
from button import Button

class Menu(object):
    """docstring for Menu."""

    def __init__(self, screen, items):
        super(Menu, self).__init__()
        self.items = []
        self.item = 0
        self.screen = screen
        self.height = 640 - items * 25 - 40
        self.itemsPos = [(self.height / items * x) for x in range(items)]
        self.itemsPos = [self.itemsPos[x] + 40 for x in range(items)]

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            for button in self.items:
                if button[0] == 'button' and button[1].isMouseIn(pygame.mouse.get_pos()):
                    return button[2]

    def addButton(self, text, id):
        self.items.append(['button', Button(self.screen).center().createButton([0, self.itemsPos[self.item]], text, 60), id])
        self.item = self.item + 1
        return self

    def addText(self, text, fontSize = 40):
        font = pygame.font.SysFont('comicsans', fontSize)
        textR = font.render(text, 1, (255, 255, 255))
        self.screen.blit(textR, (640/2 - textR.get_width()/2, self.itemsPos[self.item]))
        self.items.append(['text', textR])
        self.item = self.item + 1
        return self

    def render(self):
        for item in self.items:
            if item[0] == 'button':
                item[1].render()
        return self
