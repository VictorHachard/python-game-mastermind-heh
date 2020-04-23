import pygame, json
import sys
from os import path
from settings import *
from pygame import locals as const
from Menus.game import Game
from Menus.difficultyMenu import DifficultyMenu
from Menus.mainMenu import MainMenu
from Menus.winMenu import WinMenu
from Menus.scoreMenu import ScoreMenu
from Menus.gameModeMenu import GameModeMenu
from Menus.ruleMenu import RuleMenu
from Menus.loseMenu import LoseMenu
from Menus.settingsMenu import SettingsMenu
from Items.sprites import *

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
        self.tasks.append(['settingsMenu', False, SettingsMenu(self, self.screen)])
        self.tasks.append(['mainMenu', True, MainMenu(self, self.screen)])
        self.tasks.append(['scoreMenu', False, ScoreMenu(self, self.screen)])
        self.tasks.append(['difficultyMenu', False, DifficultyMenu(self, self.screen)])
        self.tasks.append(['winMenu', False, WinMenu(self, self.screen)])
        self.tasks.append(['gameModeMenu', False, GameModeMenu(self, self.screen)])
        self.tasks.append(['ruleMenu', False, RuleMenu(self, self.screen)])
        self.tasks.append(['loseMenu', False, LoseMenu(self, self.screen)])
        self.tasks.append(['game', False, None])
        pygame.mixer.music.play(loops=-1)

    def load_data(self):
        """charge le path de tout les assets"""
        game_folder = path.dirname(__file__)
        game_folder = path.join(game_folder, 'game_assets')
        self.image_folder = path.join(game_folder, 'image')
        sound_folder = path.join(game_folder, 'sound')
        music_folder = path.join(game_folder, 'music')
        self.hole = self.load_image('hole.png').convert_alpha()
        self.hole_b = self.load_image('hole_b.png').convert_alpha()
        #self.anim = [self.load_image('1.jpg'), self.load_image('2.jpg'), self.load_image('3.png')]
        self.background_image = pygame.transform.scale(self.load_image('bg.png').convert(), (800, 800))
        self.background_image_b = pygame.transform.scale(self.load_image('bg_b.jpg').convert(), (800, 800))
        self.button = self.load_image('button.png').convert()
        self.button_b = self.load_image('button_b.png').convert()
        self.pbutton = pygame.transform.scale(self.load_image('button.png').convert(), (160, 70))
        self.pbutton_b = pygame.transform.scale(self.load_image('button_b.png').convert(), (160, 70))
        self.effects_sounds = {}
        self.suspense = {}
        self.balls = {}
        self.bottle = []
        self.balls_b = {}
        self.falling = []
        self.falling_b = []
        for i in range(5):
            self.bottle.append(pygame.transform.scale(self.load_image(BOTTLE_IMAGES[i]).convert_alpha(), (200,200)))
        for type in BALL:
            self.balls[type] = self.load_image(BALL[type]).convert_alpha()
            self.falling.append(pygame.transform.scale(self.balls[type], (80,80)))
        for type in BALL_B:
            self.balls_b[type] = self.load_image(BALL_B[type]).convert_alpha()
            self.falling_b.append(pygame.transform.scale(self.balls_b[type], (80,80)))
        for type in EFFECTS_SOUNDS:
            self.effects_sounds[type] = pygame.mixer.Sound(path.join(sound_folder, EFFECTS_SOUNDS[type]))
        for type in SUSPENSE_MUSIC:
            self.suspense[type] = path.join(music_folder, SUSPENSE_MUSIC[type])
        pygame.mixer.music.load(self.suspense["1"])
        #picking the 2 red and white pawns to make the falling anim

    def load_image(self, name):
        return pygame.image.load(path.join(self.image_folder, name))

    def getTask(self, id):
        for task in self.tasks:
            if task[0] == id:
                return task

    def run(self):
        """Pour gérer les events on a réalisé une gameLoop (while) dans laquelle on charge la task actuelle grace aux event réalisés dans celle-ci,
         au début le mainMenu est chargé en task par défault. La méthode run sert donc a appeller les méthodes update et draw de la task actuelle en pour chaque event
         de cette task grace a la variable de classe tasks (ligne 58,59)."""
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
                    self.draw(task[2])
                    self.update(task[2])

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
            task.events(event)

m = Main()
m.run()
m.quit()
