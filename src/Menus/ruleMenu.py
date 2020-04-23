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
            .addText("Masterbeer is a game whose goal is to knock out the computer or the opponent (who will be representedby a bar pillar", 20)\
            .addText("in history) by making him swallow as much beer as possible. To do so, the player (s) must try to find the secret", 20)\
            .addText("combination of the opponent's different beer caps. The closer you get to the correct answer and the higher the dose of beer,", 20)\
            .addText("the further you go and the smaller it will be. The game has two game modes, a single player mode where the player’s", 20)\
            .addText("objective will be to challenge the biggest drinkers to get one of the different exotic beers over the levels which", 20)\
            .addText("will increase in difficulty to collect them. As well as a two players mode which will consist in finding the secret", 20)\
            .addText("combination before the other player, the number of beer busses is then counted for the two players for the winner.", 20)\
            .addText("Finding the combination directly wins the game and suddenly make the loser drink", 20)\
            .addText("", 20)\
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
