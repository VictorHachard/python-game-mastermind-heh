import pygame
from settings import *
from pygame import locals as const
from game import Game
from button import Button
from menu import Menu

def main():
    pygame.init()
    screen = pygame.display.set_mode((HEIGHT, WIDTH))
    pygame.display.set_caption(TITLE)

    running = True

    mainMenuLoop = True
    gameLoop = False
    mainMenu = Menu(screen, 3).addText('Mastermind', 60).addButton('Play', 'p').addButton('Quit', 'q').render()

    while running:
        for event in pygame.event.get():
            if event.type == const.QUIT or (event.type == const.KEYDOWN and event.key == const.K_ESCAPE):
                running = False
            if mainMenuLoop:
                res = mainMenu.update(event)
                if res == 'q':
                    running = False
                elif res == 'p':
                    screen.fill(BLACK)
                    game = Game(4, 5, 20, screen).start()
                    mainMenuLoop = False
                    gameLoop = True
            if gameLoop:
                status = game.update(event)
                if status: #win
                    mainMenuLoop = True
                    gameLoop = False
                    print('win')
                    screen.fill(BLACK)
                    mainMenu = Menu(screen, 4).addText('Mastermind', 60).addText('Win').addButton('Play', 'p').addButton('Quit', 'q').render()
                elif status == False: #lose
                    mainMenuLoop = True
                    gameLoop = False
                    print('lose')
                    screen.fill(BLACK)
                    mainMenu = Menu(screen, 4).addText('Mastermind', 60).addText('Lose ' + str(game.array_secret2).strip('[]')).addButton('Play', 'p').addButton('Quit', 'q').render()

        pygame.display.flip( )
    pygame.quit( )

if __name__ == '__main__':
    main()
