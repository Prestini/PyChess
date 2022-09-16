import pygame, sys
from move import Move

from settings import *
from game import Game
from square import Square

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
            self.game.show_last_move()
            self.game.show_moves()
            self.game.draw_pieces()
            self.game.show_hover()

            for event in pygame.event.get():
                # Mouse Click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_col = event.pos[0] // SQ_SIZE
                    clicked_row = event.pos[1] // SQ_SIZE

                    if board.has_piece(clicked_row, clicked_col):
                        piece = board.get_piece(clicked_row, clicked_col)
                        # valid piece (color) ?
                        if piece.color == self.game.next_player:
                            board.calc_moves(piece, clicked_row, clicked_col, do_weird_stuff=True)
                            dragger.start_dragging(event.pos, piece)
                            # show methods 
                            self.game.draw_bg()
                            self.game.show_last_move()
                            self.game.show_moves()
                            self.game.draw_pieces()
                        

                # Mouse Motion
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // SQ_SIZE
                    motion_col = event.pos[0] // SQ_SIZE

                    self.game.set_hover(motion_row, motion_col)

                    if dragger.dragging:
                        dragger.keep_dragging(event.pos)
                        # show methods 
                        self.game.draw_bg()
                        self.game.show_last_move()
                        self.game.show_moves()
                        self.game.draw_pieces()

                # Mouse Click Release
                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        released_row = dragger.mouseY // SQ_SIZE
                        released_col = dragger.mouseX // SQ_SIZE

                        # create possible move
                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)

                        # valid move ?
                        if board.valid_move(dragger.piece, move):
                            # normal capture
                            captured = board.squares[released_row][released_col].has_piece()
                            board.move(dragger.piece, move)

                            board.set_true_en_passant(dragger.piece)                            

                            # sounds
                            self.game.play_sound(captured)
                            # show methods
                            self.game.draw_bg()
                            self.game.show_last_move()
                            self.game.draw_pieces()
                            # next turn
                            self.game.next_turn()

                    dragger.stop_dragging()

                # key press
                elif event.type == pygame.KEYDOWN:
                    
                    # changing themes
                    if event.key == pygame.K_t:
                        self.game.change_theme()
                        dragger = self.game.dragger
                        board = self.game.board

                    # changing themes
                    if event.key == pygame.K_r:
                        self.game.reset()
                        dragger = self.game.dragger
                        board = self.game.board

                # Quit
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
 
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    main = Main()
    main.run()