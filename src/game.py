import pygame, sys, math, random
from settings import *
from pygame import locals as const
from button import Button
from text import Text
from circle import Circle

class Game(object):
    """docstring for Game."""

    def __init__(self, main, screen, column = 4, row = 6, radius = 20, color = 5):
        self.main = main
        self.screen = screen
        self.column, self.row = column, row
        self.color = color
        self.colors = COLORS[:color]
        self.radius = radius

        self.font = pygame.font.SysFont('comicsans', 20)
        self.secret = []
        self.circles = []
        self.buttons = []
        self.texts = []
        self.j = 1
        self.new()

    def new(self):
        self.vsPlayer = self.main.getTask('mainMenu')[2].vsPlayer #To Move
        if not self.vsPlayer:
            self.colorMode = self.main.getTask('mainMenu')[2].colorMode #To Move
            secrets = [random.randint(0, len(self.colors) - 1) for i in range(self.column)] if self.colorMode else random.sample(range(0, len(self.colors)), self.column)
            for secret in secrets:
                self.secret.append([self.colors[secret][0], ''])

        for j in range(self.row + 1):
            self.circles.append([])
            for i in range(self.column):
                self.createCircle(i, j)
        self.buttons.append(['Enter', Button(self.screen).createButton([WIDTH / 4, HEIGHT - 60], 'Enter', 60)])
        self.buttons.append(['Menu', Button(self.screen).createButton([WIDTH / 2, HEIGHT - 60], 'Menu', 60)])

    def update(self):
        pass

    def showSecret(self):
        i = 0
        for circle in self.circles[0]:
            for color in self.colors:
                if color[0] == self.secret[i][0]:
                    circle.fill(color[0])
                    break
            i += 1

    def createCircle(self, i, j):
        marginX = int((WIDTH - (self.radius * self.column)) / (self.column + 2))
        marginY = int((HEIGHT - 40 - (self.radius * (self.row + 1))) / (self.row + 2))
        circle = Circle(self.screen, self.colors).horizontal(marginX + i * (marginX + self.radius)).vertical(marginY + j * (marginY + self.radius)).size(self.radius)
        if j == 0 and not self.vsPlayer:
            circle.fill(DARKGREY)
        elif j != 0 and self.vsPlayer:
            circle.fill(DARKGREY)
        self.circles[j].append(circle)

    def createText(self, text1, text2):
        """Set the result text after rool the turn"""
        text1 = self.font.render('Placement : ' + text1, 1, WHITE)
        text2 = self.font.render('Present   : ' + text2, 1, WHITE)
        marginX = int((HEIGHT - 30 - (self.radius * (self.column))) / (self.column + 2))
        marginY = int((WIDTH - 40 - (self.radius * (self.row + 1))) / (self.row + 2))
        x = marginX + self.column * (marginX + self.radius)
        self.texts.append([text1, (x, marginY + self.j * (marginY + self.radius) - text1.get_height())])
        self.texts.append([text2, (x, marginY + self.j * (marginY + self.radius) + 12 - text2.get_height())])

    def draw(self):
        for j in range(self.row + 1):
            for circle in self.circles[j]:
                circle.render()
        for button in self.buttons:
            button[1].render()
        for text in self.texts:
            self.screen.blit(text[0], text[1])

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                self.showSecret()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if self.vsPlayer:
                right = event.button == 3 if True else False
                for circle in self.circles[0]:
                    sqx = (pos[0] - circle.horizontal())**2
                    sqy = (pos[1] - circle.vertical())**2
                    if math.sqrt(sqx + sqy) < self.radius:
                        circle.switch("desc" if right else "asc")
            else:
                if self.j <= self.row:
                    right = event.button == 3 if True else False
                    for circle in self.circles[self.j]:
                        sqx = (pos[0] - circle.horizontal())**2
                        sqy = (pos[1] - circle.vertical())**2
                        if math.sqrt(sqx + sqy) < self.radius:
                            circle.switch("desc" if right else "asc")
            for button in self.buttons:
                if button[0] == 'Menu' and button[1].isMouseIn(pos):
                    self.main.change = 'mainMenu'
                if button[0] == 'Enter' and button[1].isMouseIn(pos) and self.j <= self.row:
                    if self.vsPlayer:
                        for circle in self.circles[0]:
                            if circle.fill() == 'grey':
                                return
                        self.vsPlayer = not self.vsPlayer
                        for circle in self.circles[0]:
                            i = 0
                            for color in self.colors:
                                if color[0] == circle.fill():
                                    self.secret.append([color[0], ''])
                                i += 1
                            circle.fill(DARKGREY)
                        for j in range(1, self.row + 1):
                            for circle in self.circles[j]:
                                circle.fill(GREY)
                    else:
                        for secret in self.secret:
                            secret[1] = ''
                        for circle in self.circles[self.j]:
                            if circle.fill() == 'grey':
                                return
                        place, present, i = 0, 0, 0
                        for circle in self.circles[self.j]:
                            if circle.fill() == self.secret[i][0]:
                                place += 1
                                self.secret[i][1] = 'bien'
                                circle.done(True)
                            i += 1
                        for circle in self.circles[self.j]:
                            for secret in self.secret:
                                if secret[1] == '' and not circle.done() and secret[0] == circle.fill():
                                    secret[1] = 'place'
                                    circle.done(True)
                                    present += 1
                        self.createText(str(place), str(present))
                        self.j += 1
                        if (place == self.column): #win
                            self.main.getTask('difficultyMenu')[2].difficultyLvl += 1
                            self.main.getTask('difficultyMenu')[2].new()
                            self.main.change = 'winMenu'
                        if (self.j >= self.row + 1): #lose
                            self.buttons.pop(0)
                            self.showSecret()
