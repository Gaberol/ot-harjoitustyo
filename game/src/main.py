import os
import pygame
from board import Board

#Hard coded board for testing
board_map = [[(0,0), (2,0), (2,0), (2,0), (0,0), (0,0), (3,0), (3,0)],
             [(0,0), (0,0), (2,1), (2,0), (0,0), (0,0), (3,0), (3,0)],
             [(1,0), (1,0), (2,0), (0,0), (2,0), (3,0), (3,1), (0,0)],
             [(1,0), (1,0), (1,0), (0,0), (2,0), (3,0), (3,0), (4,0)],
             [(0,0), (1,0), (0,0), (1,0), (4,0), (4,1), (4,0), (4,0)],
             [(0,0), (0,0), (1,0), (1,0), (0,0), (0,0), (4,0), (4,0)],
             [(0,0), (1,0), (1,1), (0,0), (0,0), (4,0), (4,0), (0,0)],
             [(0,0), (1,0), (1,0), (4,0), (4,0), (4,0), (4,0), (0,0)]]

TILE_WIDTH = 40

def main():
    height = len(board_map)
    width = len(board_map[0])
    display_height = height * TILE_WIDTH//4*3 + TILE_WIDTH//4
    display_width = width * TILE_WIDTH + TILE_WIDTH//2

    display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Slay_copy")
    icon = pygame.image.load(
        os.path.join(
            os.path.dirname(__file__), "assets", "Unit1.png")
        )
    pygame.display.set_icon(icon)

    board = Board(board_map, TILE_WIDTH)

    pygame.init()

    board.all_sprites.draw(display)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                
                m_coords = board.mouse_event(pos)
                if 0 <= m_coords[0] < width and 0 <= m_coords[1] < height:
                    print(f"clicked at hex {m_coords}")
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
