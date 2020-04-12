import pygame, sys, math, random
from pygame import locals as const

class Game(object):
    array_colors = [['red', (255, 0, 0)], ['blue', (0, 0, 255)], ['green', (0, 255, 0)], ['orange', (255, 165, 0)], ['yelow', (247, 255, 60)]]
    GREY = (128, 128, 128)

    def __init__(self, row, colum, radius, screen):
        super(Game, self).__init__()
        self.screen = screen
        self.row = row
        self.colum = colum
        self.radius = radius
        self.array_circle = []
        self.array_button = []
        self.array_secret = []
        self.array_secret2 = []
        self.j = 0

    def start(self):
        pygame.draw.rect(self.screen, self.GREY, (100, 450, 100, 50), 0)
        font = pygame.font.SysFont('comicsans', 60)
        text = font.render('Enter', 1, (0,0,0))
        button = self.screen.blit(text, (100 + (100/2 - text.get_width()/2), 450 + (50/2 - text.get_height()/2)))
        self.array_button.append(['Enter', button])
        secrets = random.sample(range(0, len(self.array_colors) - 1), self.row)
        for secret in secrets:
            self.array_secret.append([self.array_colors[secret][0], ''])
            self.array_secret2.append(self.array_colors[secret][0])
        for j in range(self.colum):
            self.array_circle.append([])
            for i in range(self.row):
                self.createCircle(j, i)
        print(self.array_secret)
        print(self.array_circle)

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            return self.mouse(pygame.mouse.get_pos())

    def mouse(self, pos):
        for circle in self.array_circle[self.j]:
            sqx = (pos[0] - circle[0])**2
            sqy = (pos[1] - circle[1])**2
            if math.sqrt(sqx + sqy) < self.radius:
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
                        i = i + 1
        for button in self.array_button:
            if button[1].collidepoint(pos): # L'utilisateur a clicker sur enter
                for circle in self.array_circle[self.j]:
                    if circle[2] == 'grey':
                        return
                place = 0
                i = 0
                for circle in self.array_circle[self.j]:
                    if circle[2] == self.array_secret[i][0]:
                        place = place + 1
                        self.array_secret[i][1] = 'bien'
                    i = i + 1
                present = 0
                for circle in self.array_circle[self.j]:
                    for secret in self.array_secret:
                        if secret[1] != 'bien' and secret[0] == circle[2]:
                            present = present + 1
                marginY = int(self.j * 80 + 20)
                font = pygame.font.SysFont('comicsans', 20)
                text = font.render('Bon: ' + str(place), 1, (255, 0, 0))
                self.screen.blit(text, (560, marginY))
                text = font.render('Là : ' + str(present), 1, (255, 0, 0))
                self.screen.blit(text, (560, marginY + 10))
                self.j = self.j + 1
                if (place == self.row): #win
                    return True
                if (self.j >= self.colum): #lose
                    return False

        return

    def createCircle(self, j, i):
        marginX = int((640 - (self.radius * self.row)) / (self.row + 1))
        marginY = int((480 - (self.radius * self.colum)) / (self.colum + 1))
        self.array_circle[j].append([marginX + i * (marginX + self.radius), marginY + j * (marginY + self.radius), 'grey', ''])
        pygame.draw.circle(self.screen, self.GREY, (self.array_circle[j][i][0], self.array_circle[j][i][1]), self.radius)
