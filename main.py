import pygame
from pygame import locals as const
from game import Game

def main():

    print("Appuyez sur n'importe quelle touche pour lancer la partie !")

    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("mastermind")

    running = True
    start = False
    game = Game(4, 5, 20, screen) # Game class

    while running:
        for event in pygame.event.get():
            if event.type == const.QUIT or (event.type == const.KEYDOWN and event.key == const.K_ESCAPE):
                running = False
            if start:
                status = game.update(event)
                if status: #win
                    start = False
                    print('win')
                    screen.fill((0, 0 ,0))
                    font = pygame.font.SysFont('comicsans', 30)
                    text = font.render('Win', 1, (255, 255, 255))
                    screen.blit(text, (320 + (20/2 - text.get_width()/2), 240 + (20/2 - text.get_height()/2)))
                    game = Game(4, 5, 20, screen) # Game class
                elif status == False : #lose
                    start = False
                    print('lose')
                    screen.fill((0, 0 ,0))
                    font = pygame.font.SysFont('comicsans', 30)
                    text = font.render('Lose ' + str(game.array_secret2).strip('[]'), 1, (255, 255, 255))
                    screen.blit(text, (320 + (20/2 - text.get_width()/2), 240 + (20/2 - text.get_height()/2)))
                    game = Game(4, 5, 20, screen) # Game class

            if event.type == const.KEYDOWN:
                start = True
                screen.fill((0, 0 ,0))
                game.start()

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
