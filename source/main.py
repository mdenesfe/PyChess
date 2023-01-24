import pygame
import sys

from const import *

class Main:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(WIDTH, HEIGHT)
        pygame.display.set_caption('PyChess')

    def mainloop(self):
        
        while True:
            for event in pygame.events.get()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

main = Main()
main.mainloop()