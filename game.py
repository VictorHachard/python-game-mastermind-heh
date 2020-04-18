import pygame, sys, math, random
from settings import *
from pygame import locals as const
from button import Button

class Game(object):
    """docstring for Game."""

    array_colors = [['red', RED], ['blue', BLUE], ['green', GREEN], ['orange', ORANGE], ['yellow', YELLOW], ['cyan', CYAN], ['purple', PURPLE]]

    def __init__(self, screen, row, colum, radius, colors = 5):
        super(Game, self).__init__()
        self.font = pygame.font.SysFont('comicsans', 20)
        self.screen = screen
        self.row = row
        self.colors = colors
        self.colum = colum
        self.radius = radius
        self.array_circle = []
        self.array_button = []
        self.array_secret = []
        self.array_secret2 = []
        self.j = 1

    def start(self):
        self.array_button.append(['Enter', Button(self.screen).createButton([WIDTH / 4, HEIGHT - 60], 'Enter', 60).render()])
        self.array_button.append(['Menu', Button(self.screen).createButton([WIDTH / 2, HEIGHT - 60], 'Menu', 60).render()])
        secrets = random.sample(range(0, self.colors), self.row)
        for secret in secrets:
            self.array_secret.append([self.array_colors[secret][0], ''])
            self.array_secret2.append(self.array_colors[secret][0])
        for j in range(self.colum + 1):
            self.array_circle.append([])
            for i in range(self.row):
                self.createCircle(i, j)
        print(str(self.array_secret2).strip('[]'))
        return self

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            return self.mouse(pygame.mouse.get_pos(), event.button == 3 if True else False)

    def mouse(self, pos, right):
        for circle in self.array_circle[self.j]:
            sqx = (pos[0] - circle[0])**2
            sqy = (pos[1] - circle[1])**2
            if math.sqrt(sqx + sqy) < self.radius:
                if right:
                    if circle[2] == 'grey':
                        circle[2] = self.array_colors[len(self.array_colors) - 1][0]
                        pygame.draw.circle(self.screen, self.array_colors[len(self.array_colors) - 1][1], (circle[0], circle[1]), self.radius)
                        return
                    else:
                        i = 0
                        for color in self.array_colors:
                            if circle[2] == color[0]:
                                circle[2] = self.array_colors[i-1][0]
                                pygame.draw.circle(self.screen, self.array_colors[i-1][1], (circle[0], circle[1]), self.radius)
                                return
                            i = i + 1
                else:
                    if circle[2] == 'grey':
                        circle[2] = self.array_colors[0][0]
                        pygame.draw.circle(self.screen, self.array_colors[0][1], (circle[0], circle[1]), self.radius)
                        return
                    else:
                        i = 0
                        for color in self.array_colors:
                            if circle[2] == color[0]:
                                if i+1 >= len(self.array_colors):
                                    circle[2] = self.array_colors[0][0]
                                    pygame.draw.circle(self.screen, self.array_colors[0][1], (circle[0], circle[1]), self.radius)
                                    return
                                else:
                                    circle[2] = self.array_colors[i+1][0]
                                    pygame.draw.circle(self.screen, self.array_colors[i+1][1], (circle[0], circle[1]), self.radius)
                                    return
                            i += 1
        for button in self.array_button:
            if  button[0] == 'Menu' and button[1].isMouseIn(pos):
                return False
            if button[0] == 'Enter' and button[1].isMouseIn(pos):
                for secret in self.array_secret:
                    secret[1] = ''
                for circle in self.array_circle[self.j]:
                    if circle[2] == 'grey':
                        return
                place = 0
                i = 0
                for circle in self.array_circle[self.j]:
                    if circle[2] == self.array_secret[i][0]:
                        place += 1
                        self.array_secret[i][1] = 'bien'
                    i += 1
                present = 0
                for circle in self.array_circle[self.j]:
                    for secret in self.array_secret:
                        if secret[1] == '' and secret[0] == circle[2]:
                            secret[1] = 'place'
                            present += 1
                self.addText(str(place), str(present))
                self.j += 1
                if (place == self.row): #win
                    return True
                if (self.j >= self.colum + 1): #lose
                    for i in range(self.row):
                        for color in self.array_colors:
                            if color[0] == self.array_secret[i][0]:
                                pygame.draw.circle(self.screen, color[1], (self.array_circle[0][i][0], self.array_circle[0][i][1]), self.radius)

        return

    def addText(self, text1, text2):
        text1 = self.font.render('Placement : ' + text1, 1, WHITE)
        text2 = self.font.render('Present : ' + text2, 1, WHITE)
        marginY = int((HEIGHT - (self.radius * (self.colum + 1))) / (self.colum + 2))
        self.screen.blit(text1, (WIDTH - 100,  marginY + self.j * (marginY + self.radius) - text1.get_height()))
        self.screen.blit(text2, (WIDTH - 100,  marginY + self.j * (marginY + self.radius) + 12 - text1.get_height()))

    def createCircle(self, i, j):
        marginX = int((WIDTH - 50 - (self.radius * self.row)) / (self.row + 1))
        marginY = int((HEIGHT - (self.radius * self.colum + 1)) / (self.colum + 1 + 1))
        x = marginX + i * (marginX + self.radius)
        y = marginY + j * (marginY + self.radius)
        self.array_circle[j].append([x, y, 'grey', ''])
        if j == 0:
            pygame.draw.circle(self.screen, DARKGREY, (self.array_circle[j][i][0], self.array_circle[j][i][1]), self.radius)
        else:
            pygame.draw.circle(self.screen, GREY, (self.array_circle[j][i][0], self.array_circle[j][i][1]), self.radius)
