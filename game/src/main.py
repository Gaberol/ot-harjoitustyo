import os
import pygame
from board import Board

#Hard coded board for testing
board_map = [[(0,0), (1,0), (1,1), (1,0), (0,0), (0,0), (1,0), (1,0)],
             [(0,0), (0,0), (1,0), (1,0), (0,0), (0,0), (1,1), (1,0)],
             [(1,0), (1,0), (1,0), (0,0), (1,0), (1,0), (1,0), (0,0)],
             [(1,0), (1,0), (1,0), (0,0), (1,0), (1,0), (1,0), (1,0)],
             [(0,0), (1,0), (0,0), (1,0), (1,0), (1,0), (1,0), (1,0)],
             [(0,0), (0,0), (1,0), (1,0), (0,0), (0,0), (1,0), (1,0)],
             [(0,0), (1,0), (1,1), (0,0), (0,0), (1,0), (1,0), (0,0)],
             [(0,0), (1,0), (1,0), (1,0), (1,0), (1,1), (1,0), (0,0)]]

TILE_WIDTH = 40

def main():
    height = len(board_map)
    width = len(board_map[0])
    display_height = height * TILE_WIDTH/4*3 + TILE_WIDTH/4
    display_width = width * TILE_WIDTH + TILE_WIDTH/2

    display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Slay_copy")
    dirname = os.path.dirname(__file__)
    icon = pygame.image.load(os.path.join(dirname, "assets", "Unit1.png"))
    pygame.display.set_icon(icon)

    board = Board(board_map, TILE_WIDTH)

    pygame.init()

    board.all_sprites.draw(display)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
