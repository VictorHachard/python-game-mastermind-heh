import pygame, sys, math, random
from settings import *
from pygame import locals as const
from Items.button import Button
from Items.text import Text
from Items.circle import Circle

class Game(object):
    """docstring for Game. cette classe est responsable du rendu du jeu, elle est appellée suit au choix d'une difficultée dans le difficultyMenu"""

    def __init__(self, main, screen, difficultyMenu, difficultyLvl, column = 4, row = 6, radius = 24, colors = 5, offeset = 0):
        """dans ce constructeur on y défini les paramètres du niveau comme le nombre de lignes, colonnes et le nombre de couleur. On a mis des valeurs par défault pour
        les games de base. Les attributs de la lignes 21 a 25 sont des tableaux comprenant respectivement les éléments du game. currentRow est la l'essai auquel on est
        actuellement donc 1 par default."""
        self.main = main
        self.screen = screen
        self.column, self.row = column, row
        self.difficultyMenu = difficultyMenu
        self.difficultyLvl = difficultyLvl
        self.color = colors
        self.colors = COLORS[:colors]
        self.radius = radius
        self.offeset = offeset
        self.win = False
        self.sandbox = False

        self.font = pygame.font.SysFont('comicsans', 20)
        self.secret = []
        self.circles = []
        self.circles_empty_secret = []
        self.circles_empty_secret_2 = []
        self.buttons = []
        self.texts = []
        self.rec = []
        self.currentRow = 1
        self.new()

    def new(self):
        """new est appellé dans le constructeur, dans cette méthode on génére la combinaison secrete en fonction de si le mode multiColors est activé. Ensuite les
        lignes 40 a 43 créent les cercles et les placent dans la variable de classe circles. Les 2 derniere lignes ajoutent les 2 bouttons au game"""
        self.sandbox = self.main.getTask('gameModeMenu')[2].sandbox
        if not self.sandbox:
            self.colorMode = self.main.getTask('gameModeMenu')[2].colorMode #To Move
            secrets = [random.randint(0, len(self.colors) - 1) for i in range(self.column)] if self.colorMode else random.sample(range(0, len(self.colors)), self.column)
            for secret in secrets:
                self.secret.append([self.colors[secret][0], ''])

        for j in range(self.row + 1):
            self.circles.append([])
            for i in range(self.column):
                self.createCircle(i, j)
        marginX = int((HEIGHT - 30 - (self.radius * (self.column))) / (self.column + 2))
        marginY = int((WIDTH - 40 - (self.radius * (self.row + 1))) / (self.row + 2))
        for n in range(1, self.row + 1):
            x = marginX + self.column * (marginX + self.radius)
            self.circles_empty_secret.append(Circle(self.main, self.screen, self.colors).horizontal(x).vertical(marginY + n * (marginY + self.radius) - 10).size(12))
            self.circles_empty_secret.append(Circle(self.main, self.screen, self.colors).horizontal(x + 25).vertical(marginY + n * (marginY + self.radius) - 10).size(12))
            if self.column >= 5:
                self.circles_empty_secret.append(Circle(self.main, self.screen, self.colors).horizontal(x + 50).vertical(marginY + n * (marginY + self.radius) - 10).size(12))
            if self.column >= 7:
                self.circles_empty_secret.append(Circle(self.main, self.screen, self.colors).horizontal(x + 75).vertical(marginY + n * (marginY + self.radius) - 10).size(12))
            self.circles_empty_secret.append(Circle(self.main, self.screen, self.colors).horizontal(x).vertical(marginY + n * (marginY + self.radius) + 15).size(12))
            self.circles_empty_secret.append(Circle(self.main, self.screen, self.colors).horizontal(x + 25).vertical(marginY + n * (marginY + self.radius) + 15).size(12))
            if self.column >= 6:
                self.circles_empty_secret.append(Circle(self.main, self.screen, self.colors).horizontal(x + 50).vertical(marginY + n * (marginY + self.radius) + 15).size(12))
        if self.sandbox:
            marginX = int((WIDTH - (self.radius * (self.column + 1))) / (self.column + 3))
            for n in range(1, self.row + 1):
                x = marginX + self.column * (marginX + self.radius)
        self.buttons.append(['Enter', Button(self.screen, self.main).createButton([WIDTH / 4, HEIGHT - 60], 'Enter', 60, menu = False, petit = True, test = 4)])
        self.buttons.append(['Menu', Button(self.screen, self.main).createButton([WIDTH / 2, HEIGHT - 60], 'Menu', 60, menu = False, petit = True, test = 2)])
        pygame.mixer.music.load(self.main.suspense["1"])
        pygame.mixer.music.play(loops=-1)

    def addImage(self, image, size):
        """Add an image"""
        self.items.append(['image', ForeGroundImage(self.screen, self.main).createImage([-1, self.itemsPos[self.item]], image, size)])
        self.item = self.item + 1
        return self

    def play(self):
        if self.currentRow <= 5:
            pygame.mixer.music.load(self.main.suspense[str(self.currentRow)])
            pygame.mixer.music.play(loops=-1)

    def update(self):
        """cette méthode update l'image, elle permet a la barre de pv de ce render correctement et faire disparaitre le boutton enter en cas de victoire"""

    def showSecret(self):
        if len(self.secret) != 0:
            i = 0
            for circle in self.circles[0]:
                for color in self.colors:
                    if color[0] == self.secret[i][0]:
                        circle.fill(color[0])
                        break
                i += 1

    def createCircle(self, i, j):
        """cette méthode est appellée dans la méthode new et sert a créer un cerle en gris et le placer dans le game"""
        if self.sandbox:
            marginX = int((WIDTH - (self.radius * self.column + 1)) / (self.column + 3))
        else:
            marginX = int((WIDTH - (self.radius * self.column)) / (self.column + 2))
        marginY = int((HEIGHT - 40 - (self.radius * (self.row + 1))) / (self.row + 2))
        circle = Circle(self.main, self.screen, self.colors).horizontal(marginX + i * (marginX + self.radius)).vertical(marginY + j * (marginY + self.radius)).size(self.radius)
        if j == 0 and not self.sandbox:
            circle.fill(DARKGREY)
        elif j != 0 and self.sandbox:
            circle.fill(DARKGREY)
        self.circles[j].append(circle)

    def createHints(self, place, present):
        """Apres chaque essai les indices Placment et Présent sont placés a coté de chaque row apres avoir tenté un essai"""
        for n in range(0, place):
            self.circles_empty_secret[n + self.column * (self.currentRow - 1)].fill('dark')
        for n in range(place, place + present):
            self.circles_empty_secret[n + self.column * (self.currentRow - 1)].fill('white')

    def draw(self):
        """cette méthode est la meme que les méthodes draw() des menus est elle lancée dans la méthode run du main"""
        bg = self.main.background_image_b if self.main.getTask('settingsMenu')[2].biere else self.main.background_image
        self.screen.blit(bg, (0, 0))
        for j in range(self.row + 1):
            for circle in self.circles[j]:
                circle.render()
        for button in self.buttons:
            button[1].render()
        for circle in self.circles_empty_secret:
            circle.render()

    def clickCircle(self, pos, event):
        """cette méthode sert a détecter si la souris a cliqué dans un cercle, cela est fait grace a la boucle for qui check chaque circle grace a la formule
        de la racine carrée. Le 1er if sert a checker si le mode 2 joueurs est activé. """
        if self.sandbox:
            right = event.button == 3 if True else False
            for circle in self.circles[0]:
                sqx = (pos[0] - circle.horizontal())**2
                sqy = (pos[1] - circle.vertical())**2
                if math.sqrt(sqx + sqy) < self.radius + 10:
                    circle.switch("desc" if right else "asc")
        else:
            if self.currentRow <= self.row:
                right = event.button == 3 if True else False
                for circle in self.circles[self.currentRow]:
                    sqx = (pos[0] - circle.horizontal())**2
                    sqy = (pos[1] - circle.vertical())**2
                    if math.sqrt(sqx + sqy) < self.radius + 10:
                        circle.switch("desc" if right else "asc")

    def clickButton(self, pos, event):
        """cette méthode passe en revue tout les bouttons grace a la boucle for numero 1, si c'est le boutton menu on retourne au menu, si c'est le boutton enter alors
        on vérifie si on joue avec un autre joueur, si non, alors il attends que le joueur 1 le génère. A la fin de cette méthode la méthode la méthode verification
         est appellée si le player 1 n'était pas en train de générer le secret"""
        for button in self.buttons:
            if button[0] == 'Menu' and button[1].isMouseIn(pos):
                pygame.mixer.music.load(self.main.suspense["1"])
                pygame.mixer.music.play(loops=-1)
                if self.win:
                    if(self.difficultyMenu.difficultyLvl == self.difficultyLvl):
                        self.main.getTask('difficultyMenu')[2].difficultyLvl += 1
                        self.main.getTask('scoreMenu')[2].addBottle()
                    else:
                        self.main.getTask('difficultyMenu')[2]
                    self.main.getTask('difficultyMenu')[2].new()
                    self.main.getTask('scoreMenu')[2].addScore()
                    self.main.getTask('winMenu')[2].new()
                    self.main.change = 'winMenu'
                elif (self.currentRow >= self.row + 1):
                    self.main.getTask('loseMenu')[2].new()
                    self.main.change = 'loseMenu'
                else:
                    self.main.change = 'mainMenu'
            if button[0] == 'Enter' and button[1].isMouseIn(pos) and self.currentRow <= self.row:
                if self.sandbox:
                    if not self.canEnter(0):
                        return
                    self.sandbox = not self.sandbox
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
                    self.verification()

    def verification(self):
        """cette méthode est appellée après chaque essai de combinaison, elle vérifie si la combinanaison est bonne ou pas et ajoute le score au player"""
        for secret in self.secret:
            secret[1] = ''
        if not self.canEnter(self.currentRow):
            return
        place, present, i = 0, 0, 0
        for circle in self.circles[self.currentRow]:
            if circle.fill() == self.secret[i][0]:
                place += 1
                self.secret[i][1] = 'bien'
                circle.done(True)
            i += 1
        for circle in self.circles[self.currentRow]:
            for secret in self.secret:
                if secret[1] == '' and not circle.done() and secret[0] == circle.fill():
                    secret[1] = 'place'
                    circle.done(True)
                    present += 1
        self.createHints(place, present)
        self.currentRow += 1
        self.play()
        if (place == self.column): #win
            self.win = True
            self.buttons.pop(0)
            self.showSecret()
        elif (self.currentRow >= self.row + 1): #lose
            self.buttons.pop(0)
            self.showSecret()


    def canEnter(self, j):
        """cette méthode vérifie si toute les cases de la ligne ont étés remplies, si oui return true sinon return false"""
        for circle in self.circles[j]:
            if circle.fill() == 'grey':
                return False
        return True

    def events(self, event):
        """meme méthode que event des menus, est appellée dans le main pour afficher les events"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                self.showSecret()
        if event.type == pygame.MOUSEBUTTONUP:
            self.clickCircle(pygame.mouse.get_pos(), event)
            self.clickButton(pygame.mouse.get_pos(), event)
