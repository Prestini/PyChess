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

        dragger = self.game.dragger
        board = self.game.board

        while True:

            self.game.show_bg(self.screen)
            self.game.show_pieces(self.screen)

            if dragger.dragging:
                dragger.update_blit(self.screen)

            for event in pygame.event.get():
                # Mouse Click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_col = dragger.mouseX // SQ_SIZE
                    clicked_row = dragger.mouseY // SQ_SIZE

                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)

                # Mouse Motion
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                # Mouse Click Release
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()

                # Quit
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
 
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    main = Main()
    main.run()