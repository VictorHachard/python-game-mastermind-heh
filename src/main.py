import pygame, json
import sys
from os import path
from settings import *
from pygame import locals as const
from game import Game
from difficultyMenu import DifficultyMenu
from mainMenu import MainMenu
from winMenu import WinMenu
from sprites import *

class Main(object):
    """docstring for Main."""

    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 4, 2048)
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        imgage_folder = path.join(game_folder, 'imgage')
        sound_folder = path.join(game_folder, 'sound')
        music_folder = path.join(game_folder, 'music')

    def new(self):
        self.change = ''
        self.tasks = []
        self.tasks.append(['mainMenu', True, MainMenu(self, self.screen)])
        self.tasks.append(['difficultyMenu', False, DifficultyMenu(self, self.screen)])
        self.tasks.append(['winMenu', False, WinMenu(self, self.screen)])
        self.tasks.append(['game', False, Game(self, self.screen)])

    def getTask(self, id):
        for task in self.tasks:
            if task[0] == id:
                return task

    def run(self):
        # game loop - set self.playing = False to end the game
        self.running = True
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000.0
            if self.change != '':
                self.getTask(self.change)[1] = not task[1]
                self.change = ''
            for task in self.tasks:
                if task[1]:
                    self.events(task[2])
                    if self.change != '':
                        task[1] = not task[1]
                    self.update(task[2])
                    self.draw(task[2])

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self, task):
        task.update()

    def draw(self, task):
        pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(BLACK)
        task.draw()
        pygame.display.flip()

    def events(self, task):
        # catch all events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
            task.events(event)

m = Main()
#while True:
m.new()
m.run()
m.quit()
