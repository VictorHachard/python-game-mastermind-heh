import pygame
from settings import *
from pygame import locals as const
from game import Game
from button import Button
from menu import Menu

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)

    running = True

    difficultyLvl = 0
    mainMenuLoop = True
    gameLoop = False
    difficultyMenuLoop = False
    multipleColor = False
    mainMenu = Menu(screen, 4).addText('Mastermind', 60).addButton('Play', 'p').addButton('multiple colors: Off', 'm').addButton('Quit', 'q').render()

    while running:
        for event in pygame.event.get():
            if event.type == const.QUIT or (event.type == const.KEYDOWN and event.key == const.K_ESCAPE):
                running = False
            if mainMenuLoop:
                res = mainMenu.update(event)
                if res == 'q':
                    running = False
                elif res == 'm':
                    if multipleColor:
                        multipleColor = False
                        screen.fill(BLACK)
                        mainMenu = Menu(screen, 4).addText('Mastermind', 60).addButton('Play', 'p').addButton('multiple colors: Off', 'm').addButton('Quit', 'q').render()
                    else:
                        multipleColor = True
                        screen.fill(BLACK)
                        mainMenu = Menu(screen, 4).addText('Mastermind', 60).addButton('Play', 'p').addButton('multiple colors: On', 'm').addButton('Quit', 'q').render()
                elif res == 'p':
                    screen.fill(BLACK)
                    difficultyMenu = Menu(screen, 6).addText('Difficulty', 60).addButton('Easy', 'e', GREEN if difficultyLvl >= 0 else GREY).addButton('Medium', 'm', GREEN if difficultyLvl >= 1 else GREY).addButton('Hard', 'h', GREEN if difficultyLvl >= 2 else GREY).addButton('Extreme', 'ex', GREEN if difficultyLvl >= 3 else GREY).addButton('Armand', 'a', GREEN if difficultyLvl >= 4 else GREY)
                    difficultyMenu.render()
                    mainMenuLoop = False
                    difficultyMenuLoop = True
            elif difficultyMenuLoop:
                res = difficultyMenu.update(event)
                game = False
                if res == 'e' and difficultyLvl >= 0:
                    screen.fill(BLACK)
                    game = Game(screen, 4, 2, 20).start(multipleColor)
                elif res == 'm' and difficultyLvl >= 1:
                    screen.fill(BLACK)
                    game = Game(screen, 4, 5, 20).start(multipleColor)
                elif res == 'h' and difficultyLvl >= 2:
                    screen.fill(BLACK)
                    game = Game(screen, 5, 5, 20).start(multipleColor)
                elif res == 'ex' and difficultyLvl >= 3:
                    screen.fill(BLACK)
                    game = Game(screen, 5, 4, 20).start(multipleColor)
                elif res == 'a' and difficultyLvl >= 4:
                    screen.fill(BLACK)
                    game = Game(screen, 7, 6, 20, 7).start(multipleColor)
                if res == 'e' or res == 'm' or res == 'h' or res == 'ex' or res == 'a':
                    if game:
                        difficultyMenuLoop = False
                        gameLoop = True
            elif gameLoop:
                status = game.update(event)
                if status: #win
                    difficultyLvl += 1
                    mainMenuLoop = True
                    gameLoop = False
                    print('win')
                    screen.fill(BLACK)
                    mainMenu = Menu(screen, 5).addText('Mastermind', 60).addText('Win').addButton('Play', 'p').addButton('multiple colors: On' if multipleColor else 'multiple colors: Off', 'm').addButton('Quit', 'q').render()
                elif status == False: #lose
                    mainMenuLoop = True
                    gameLoop = False
                    print('lose')
                    screen.fill(BLACK)
                    mainMenu = Menu(screen, 5).addText('Mastermind', 60).addText('Lose ' + str(game.array_secret2).strip('[]')).addButton('Play', 'p').addButton('multiple colors: On' if multipleColor else 'multiple colors: Off', 'm').addButton('Quit', 'q').render()

        pygame.display.flip( )
    pygame.quit( )

if __name__ == '__main__':
    main()
