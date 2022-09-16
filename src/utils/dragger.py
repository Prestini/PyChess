import pygame
from piece import Piece

from settings import *

class Dragger:

    def __init__(self) -> None:
        self.surf = pygame.display.get_surface()
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0

    # Blit Methods
    
    def update_blit(self):
        # texture
        self.piece.set_texture(120)
        # img
        img = pygame.image.load(self.piece.texture).convert_alpha()
        # rect
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center = img_center)
        self.surf.blit(img, self.piece.texture_rect)
    
    # Other Methods
    
    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos
    
    def save_initial(self, pos):
        self.initial_col = pos[0] // SQ_SIZE
        self.initial_row = pos[1] // SQ_SIZE

    def start_dragging(self, pos, piece: Piece):
        self.update_mouse(pos)
        self.save_initial(pos)
        self.piece = piece
        self.dragging = True
    
    def keep_dragging(self, pos):
        self.update_mouse(pos)
    
    def stop_dragging(self):
        self.piece = None
        self.dragging = False