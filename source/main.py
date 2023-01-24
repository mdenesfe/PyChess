import pygame
import sys

from const import *
from game import *

class Main:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('PyChess')
        self.game = Game()

    def mainloop(self) -> None:
        
        screen = self.screen
        game = self.game

        while True:
            game.show(self.screen)
            game.show_pieces(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()


main = Main()
main.mainloop()