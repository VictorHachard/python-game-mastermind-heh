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
        """dans le constructeur on initialise les settings liées a pygame jusqu'a la ligne 21. Ensuite on crée un tableau tasks dans lequel on y mettra toutes les
        tasks. Dans ce constructeur on y append déja les les tacks mainMenu, difficultyMenu ... .Seul le mainMenu est set sur true (c'est lui qui donc s'afficher en 1er)"""
        pygame.mixer.pre_init(44100, -16, 4, 2048)
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()
        self.change = ''
        self.tasks = []
        self.tasks.append(['mainMenu', True, MainMenu(self, self.screen)])
        self.tasks.append(['difficultyMenu', False, DifficultyMenu(self, self.screen)])
        self.tasks.append(['winMenu', False, WinMenu(self, self.screen)])
        self.tasks.append(['game', False, None])

    def load_data(self):
        """charge le path de tout les assets"""
        game_folder = path.dirname(__file__)
        game_folder = path.join(game_folder, 'game_assets')
        image_folder = path.join(game_folder, 'image')
        sound_folder = path.join(game_folder, 'sound')
        music_folder = path.join(game_folder, 'music')
        print(path.join(image_folder, 'bg.jpg'))
        self.background_image = pygame.transform.scale(pygame.image.load(path.join(image_folder, 'bg.jpg')).convert(), (800, 800))

    def getTask(self, id):
        for task in self.tasks:
            if task[0] == id:
                return task


    def run(self):
        """Pour gérer les events on a réalisé une gameLoop (while) dans laquelle on charge la task actuelle grace aux event réalisés dans celle-ci,
         au début le mainMenu est chargé en task par défault. La méthode run sert donc a appeller les méthodes update et draw de la task actuelle en pour chaque event
         de cette task grace a la variable de classe tasks (ligne 58,59). """
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
        """chaque task (par exemple mainMenu) a une méthode update, cette méthode sert donc a appeller la méthode update de la task concernée"""
        task.update()

    def draw(self, task):
        """chaque task (par exemple mainMenu) a une méthode draw, cette méthode sert donc a appeller la méthode draw de la task concernée."""
        pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(BLACK)
        task.draw()
        pygame.display.flip()

    def events(self, task):
        """chaque task (par exemple mainMenu) a une méthode events, cette méthode sert donc a appeller la méthode events de la task concernée."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
            task.events(event)

m = Main()
m.run()
m.quit()
