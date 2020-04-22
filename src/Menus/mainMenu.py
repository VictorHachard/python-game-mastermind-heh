import pygame, random
from settings import *
from pygame import locals as const
from Items.button import Button
from Items.text import Text
from Menus.menu import Menu
from Menus.game import Game


class MainMenu(object):
    """docstring for MainMenu. Cette classe est la classe responsable de la creation et personnalisatioon du mainMenu"""

    def __init__(self, main, screen):
        """"Dans ce constructeur on initialise les variables de classe et on appelle la méthode new(self)"""
        self.main = main
        self.screen = screen
        self.new()
        #handles the falling pawn anim
        self.isPawnFalling = False
        self.fallingPawnX = 0
        self.fallingPawnY = -80
        self.listOfFallingPawns = [self.main.fallingRedPawn, self.main.fallingWhitePawn]
        self.currentFallingPawn = self.main.fallingRedPawn

    def new(self):
        """cette méthode sert a ajouter les bouttons et textes au menu en fonction des variables de classe dans le constructeur"""
        self.menu = Menu(self.screen, self.main, 6).addText('Mastermind', 60).addButton('Play', 'p').addButton('Game Mode', 'o')
        self.menu.addButton('Rules', 'r').addButton('High score', 'h').addButton('Quit', 'q')

    """les 3 méthodes suivantes sont les méthodes dans lesquelles les tacks sont gérés, ces méthodes sont appellée depuis la méthode run du main"""

    def update(self):
        pass

    def draw(self):
        """cette méthode permet de placer les element a render"""
        self.screen.blit(self.main.background_image, (0, 0))
        self.drawFallingPawn()
        self.menu.render()

    def events(self, event):
        """cette méthode gere les input du clavier et les traite en conséquence"""
        res = self.menu.update(event)
        if res == 'q':
            self.main.running = False
        elif res == 'p':
            self.main.change = 'difficultyMenu'
        elif res == 'o':
            self.main.change = 'gameModeMenu'
        elif res == 'h':
            self.main.change = 'scoreMenu'
        elif res == 'r':
            self.main.change = 'ruleMenu'

    """les 3 prochaines méthodes gèrent la création et animation de la bille qui tombe dans le menu"""

    def handleFallingPawnSpawn(self):
        """cette méthode crée une bille a positionner si il y en a pas encore (il alterne entre rouge et blanc) et la positionne, si il y a déja une bille
        il appelle la méthode fallingPawnUpdatePos()"""
        if not self.isPawnFalling:
            if self.currentFallingPawn == self.listOfFallingPawns[0]:
                self.currentFallingPawn = self.listOfFallingPawns[1]
            else :
                self.currentFallingPawn = self.listOfFallingPawns[0]
            self.fallingPawnX= random.randint(1, WIDTH-81)
            self.fallingPawnY= -80
            self.isPawnFalling= True

        else:
            self.fallingPawnUpdatePos()

    def fallingPawnUpdatePos(self):
        """cette méthode rajoute 2 de coord y a la pos de la bille (ca donne un illusion d'animation) . Si la bille n'est plus du tout sur l'écran alors on set
        isPawnFalling a false"""
        if self.fallingPawnY < HEIGHT+80:
            self.fallingPawnY = self.fallingPawnY+4
        else:
            self.isPawnFalling = False

    def drawFallingPawn(self):
        """c'est cette méthode qui update sur l'écran la position de bille avec les paramètres fallingPawnX et Y"""
        self.handleFallingPawnSpawn()
        self.screen.blit(self.currentFallingPawn, (self.fallingPawnX, self.fallingPawnY))

