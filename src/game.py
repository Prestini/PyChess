import pygame
from board import Board
from const import *

class Game:

    def __init__(self) -> None:
        self.board = Board()

    def show_bg(self, surf) -> None:
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200)
                else:
                    color = (119, 154, 88)
                
                rect = (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE)

                pygame.draw.rect(surf, color, rect)
    
    def show_pieces(self, surf):
        for row in range(ROWS):
            for col in range(COLS):
                # Check if there's a piece
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    img = pygame.image.load(piece.texture)
                    img_center = col * SQ_SIZE + SQ_SIZE // 2, row * SQ_SIZE + SQ_SIZE // 2
                    piece.texture_rect = img.get_rect(center = img_center)
                    surf.blit(img, piece.texture_rect)