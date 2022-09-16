import pygame
from board import Board
from config import Config
from settings import *
from square import Square
from utils.dragger import Dragger

class Game:
    def __init__(self) -> None:
        self.surf = pygame.display.get_surface()
        self.next_player = 'w'
        self.hovered_sqr = None
        self.board = Board()
        self.dragger = Dragger()
        self.config = Config()
        self.theme = self.config.theme

    def draw_bg(self) -> None:
        for row in range(ROWS):
            for col in range(COLS):
                # color
                color = self.config.theme.bg.light if (row + col) % 2 == 0 else self.config.theme.bg.dark
                # rect
                rect = (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
                # blit
                pygame.draw.rect(self.surf, color, rect)

                # row coordinates
                if col == 0:
                    # color
                    color = self.config.theme.bg.dark if row % 2 == 0 else self.config.theme.bg.light
                    # label
                    lbl = self.config.font.render(str(ROWS-row), 1, color)
                    lbl_pos = (5, 5 + row * SQ_SIZE)
                    # blit
                    self.surf.blit(lbl, lbl_pos)
                
                # col coordinates
                if row == 7:
                    # color
                    color = self.config.theme.bg.dark if (row + col) % 2 == 0 else self.config.theme.bg.light
                    # label
                    lbl = self.config.font.render(Square.get_alphacol(col), 1, color)
                    lbl_pos = (col * SQ_SIZE + SQ_SIZE - 20, HEIGHT - 20)
                    # blit
                    self.surf.blit(lbl, lbl_pos)

    
    def draw_pieces(self):
        for row in range(ROWS):
            for col in range(COLS):
                # Check if there's a piece
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    if piece is not self.dragger.piece:
                        piece.set_texture()
                        img = pygame.image.load(piece.texture).convert_alpha()
                        img_center = col * SQ_SIZE + SQ_SIZE // 2, row * SQ_SIZE + SQ_SIZE // 2
                        piece.texture_rect = img.get_rect(center = img_center)
                        self.surf.blit(img, piece.texture_rect)
    
        if self.dragger.dragging:
            self.dragger.update_blit()
    
    def show_moves(self):
        if self.dragger.dragging:
            piece = self.dragger.piece

            # loop all valid moves
            for move in piece.moves:
                # color
                color = self.theme.moves.light if (move.final.row + move.final.col) % 2 == 0 else self.theme.moves.dark
                # rect
                rect = (move.final.col * SQ_SIZE, move.final.row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
                # blit
                pygame.draw.rect(self.surf, color, rect)
    
    def show_last_move(self):
        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final

            for pos in [initial, final]:
                # color
                color = self.theme.trace.light if (pos.row + pos.col) % 2 == 0 else self.theme.trace.dark
                # rect
                rect = (pos.col * SQ_SIZE, pos.row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
                # blit
                pygame.draw.rect(self.surf, color, rect)
    
    def show_hover(self):
        if self.hovered_sqr:
            # color
            color = (180, 180, 180)
            # rect
            rect = (self.hovered_sqr.col * SQ_SIZE, self.hovered_sqr.row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
            # blit
            pygame.draw.rect(self.surf, color, rect, width=3)
    
    # other methods

    def next_turn(self):
        self.next_player = 'w' if self.next_player == 'b' else 'b'

    def set_hover(self, row, col):
        self.hovered_sqr = self.board.squares[row][col]

    def change_theme(self):
        self.config.change_theme()

    def play_sound(self, captured=False):
        if captured:
            self.config.capture_sound.play()
        else:
            self.config.move_sound.play()

    def reset(self):
        self.__init__()