import pygame
from const import *

class Game:

    def __init__(self) -> None:
        pass

    def show(self, surface) -> None:
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234,235,200) #chess.com
                else:
                    color = (119,154,88) #chess.com

                rect = (col * SSIZE, row * SSIZE, SSIZE, SSIZE)

                pygame.draw.rect(surface, color, rect)