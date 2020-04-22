import pygame
from settings import *
from pygame import locals as const
from Items.button import Button
from Items.text import Text
from Menus.menu import Menu
from Menus.game import Game


class RuleMenu(object):
    """docstring for RuleMenu."""

    def __init__(self, main, screen):
        """"Dans ce constructeur on initialise les variables de classe et on appelle la méthode new(self)"""
        self.main = main
        self.screen = screen
        self.new()

    def new(self):
        """cette méthode sert a ajouter les bouttons et textes au menu en fonction des variables de classe dans le constructeur"""
        self.ruleMenu = Menu(self.screen, self.main, 16)\
            .addText('Rules', 60)\
            .addText("")\
            .addText("")\
            .addText("Masterbeer est un jeu dont le but est de mettre K.O. l’ordinateur ou l’adversaire (qui sera représenter par un pilier", 20)\
            .addText("de bar dans l’histoire) en lui faisant avaler le plus de bière possible. Pour se faire, le/les joueur(s) devra/devront", 20)\
            .addText("essayer de trouver la combinaison secrète de différente capsule de bière de l’adversaire. Plus vous vous approcher de la", 20)\
            .addText("bonne réponse et plus la dose de bière est élevée, plus vous vous éloigner et plus elle sera minime. Le jeu possède deux", 20)\
            .addText("modes de jeu, un mode solo où l’objectif du joueur sera de défier les plus grands buveurs pour obtenir l’une des", 20)\
            .addText("différentes bières exotiques au fil des niveaux qui augmenteront en difficulté pour ainsi les collectionner.", 20)\
            .addText("Ainsi qu’un mode deux joueur qui consistera à trouver le combinaison secrète avant l’autre joueur, le nombre de bière", 20)\
            .addText("bus est alors comptabilisé pour les deux joueurs pour les départagé. Trouver la combinaison fait remporter directement", 20)\
            .addText("la partie et du coup fais boire le perdant.", 20)\
            .addText("")\
            .addText("")\
            .addButton('Menu', 'm')

    """les 3 méthodes suivantes sont les méthodes dans lesquelles les tacks sont gérés, ces méthodes sont appellée depuis la méthode run du main"""

    def update(self):
        pass

    def draw(self):
        """cette méthode permet de placer les element a render"""
        bg = self.main.background_image_b if self.main.getTask('settingsMenu')[2].biere else self.main.background_image
        self.screen.blit(bg, (0, 0))
        self.ruleMenu.render()

    def events(self, event):
        """cette méthode gere les input du clavier et les traite en conséquence"""
        res = self.ruleMenu.update(event)
        if res == 'm':
            self.main.change = 'mainMenu'
