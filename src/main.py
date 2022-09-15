import pygame, sys

from const import *
from game import Game

class Main:

    def __init__(self) -> None:
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('PyChess')
        self.clock = pygame.time.Clock()
        self.game = Game()

    def run(self) -> None:
        while True:

            self.game.show_bg(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
 
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    main = Main()
    main.run()