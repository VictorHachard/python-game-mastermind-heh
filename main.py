import pygame
from pygame import locals as const
from game import Game
from button import Button
from menu import Menu

def main():

    print("Appuyez sur n'importe quelle touche pour lancer la partie !")

    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("mastermind")

    running = True

    mainMenuLoop = True
    gameLoop = False
    mainMenu = Menu(screen, 3).addText('Mastermind').addButton('Play', 'p').addButton('Quit', 'q').render()

    while running :
        for event in pygame.event.get():
            if event.type == const.QUIT or (event.type == const.KEYDOWN and event.key == const.K_ESCAPE):
                running = False
            if mainMenuLoop:
                res = mainMenu.update(event)
                if res == 'q':
                    running = False
                elif res == 'p':
                    screen.fill((0, 0 ,0))
                    game = Game(4, 5, 20, screen).start()
                    mainMenuLoop = False
                    gameLoop = True
            if gameLoop:
                status = game.update(event)
                if status: #win
                    mainMenuLoop = True
                    gameLoop = False
                    print('win')
                    screen.fill((0, 0 ,0))
                    mainMenu = Menu(screen, 4).addText('Mastermind').addText('Win').addButton('Play', 'p').addButton('Quit', 'q').render()
                elif status == False : #lose
                    mainMenuLoop = True
                    gameLoop = False
                    print('lose')
                    screen.fill((0, 0 ,0))
                    mainMenu = Menu(screen, 4).addText('Mastermind').addText('Lose ' + str(game.array_secret2).strip('[]')).addButton('Play', 'p').addButton('Quit', 'q').render()

        pygame.display.flip( )
    pygame.quit( )


if __name__ == '__main__':
    main()
