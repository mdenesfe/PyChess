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
        board = self.game.board
        dragger = self.game.dragger

        while True:
            game.show(self.screen)
            game.show_pieces(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    clicked_row = dragger.mouseY // SSIZE
                    clicked_col = dragger.mouseX // SSIZE

                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_blit(screen)
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()


main = Main()
main.mainloop()