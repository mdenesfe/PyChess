import pygame

from const import *
from board import Board
from dragger import Dragger

class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.dragger = Dragger()
    def show(self, surface) -> None:
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234,235,200) #chess.com
                else:
                    color = (119,154,88) #chess.com

                rect = (col * SSIZE, row * SSIZE, SSIZE, SSIZE)

                pygame.draw.rect(surface, color, rect)


    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    
                    if piece is not self.dragger.piece:
                        piece.set_texture(size = 80)
                        img = pygame.image.load(piece.texture) 
                        img_center = col * SSIZE + SSIZE // 2, row * SSIZE + SSIZE // 2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)
                    