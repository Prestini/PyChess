import pygame

from const import *
from helpers import load_and_scale_svg

class Dragger:

    def __init__(self) -> None:
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0

    # Blit Methods
    
    def update_blit(self, surf):
        # texture
        self.piece.set_texture(120)
        # img
        img = pygame.image.load(self.piece.texture).convert_alpha()
        # rect
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center = img_center)
        surf.blit(img, self.piece.texture_rect)
    
    # Other Methods
    
    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos
    
    def save_initial(self, pos):
        self.initial_col = pos[0] // SQ_SIZE
        self.initial_row = pos[1] // SQ_SIZE
    
    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True
    
    def undrag_piece(self):
        self.piece = None
        self.dragging = False