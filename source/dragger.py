import pygame

from const import *

class Dragger:
    def __init__(self) -> None:
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0

    def update_blit(self, surface):
        self.piece.set_texture(size = 128)
        texture = self.piece.texture
        img = pygame.image.load(texture)
        img_center = (self.mouseX, self.mouseY)
    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos

    def save_initial(self, pos):
        self.initial_row = pos[1] // SSIZE
        self.initial_col = pos[0] // SSIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True
    def undragging_piece(self, pos):
        self.piece = None
        self.dragging = False