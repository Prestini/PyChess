import pygame, sys

from settings import *
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

        dragger = self.game.dragger
        board = self.game.board

        while True:

            self.game.draw_bg()
            self.game.draw_pieces()

            for event in pygame.event.get():
                # Mouse Click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_col = event.pos[0] // SQ_SIZE
                    clicked_row = event.pos[1] // SQ_SIZE

                    if board.has_piece(clicked_row, clicked_col):
                        piece = board.get_piece(clicked_row, clicked_col)
                        dragger.start_dragging(event.pos, piece)

                # Mouse Motion
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.keep_dragging(event.pos)

                # Mouse Click Release
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.stop_dragging()

                # Quit
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
 
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    main = Main()
    main.run()