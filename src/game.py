import pygame
from board import Board
from settings import *
from utils.dragger import Dragger

class Game:
    def __init__(self) -> None:
        self.surf = pygame.display.get_surface()
        self.board = Board()
        self.dragger = Dragger()

    def draw_bg(self) -> None:
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200)
                else:
                    color = (119, 154, 88)
                
                rect = (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE)

                pygame.draw.rect(self.surf, color, rect)
    
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