import os
import pygame
from random import randint, choices   #temporary, remove
from board import Board
from game_loop import GameLoop
from event_queue import EventQueue
from renderer import Renderer
from clock import Clock

#Hard coded board for testing
#board_map = [[(0,0), (2,0), (2,0), (2,0), (0,0), (0,0), (3,0), (3,0)],
 #            [(0,0), (0,0), (2,1), (2,0), (0,0), (0,0), (3,0), (3,0)],
  #           [(1,0), (1,0), (2,0), (0,0), (2,0), (3,0), (3,1), (0,0)],
   #          [(1,0), (1,0), (1,0), (0,0), (2,0), (3,0), (3,0), (4,0)],
    #         [(0,0), (1,0), (0,0), (1,0), (4,0), (4,1), (4,0), (4,0)],
     #        [(0,0), (0,0), (1,0), (1,0), (0,0), (0,0), (4,0), (4,0)],
      #       [(0,0), (1,0), (1,1), (0,0), (0,0), (4,0), (4,0), (0,0)],
       #      [(0,0), (1,0), (1,0), (4,0), (4,0), (4,0), (4,0), (0,0)]]

board_map = [[(randint(0,4), choices(
                            population=[0, 1],
                            weights=[0.9, 0.1],
                            k=1
                        )[0]) for i in range(8)] for i in range(8)]

TILE_WIDTH = 40

def main():
    height = len(board_map)
    width = len(board_map[0])
    display_height = height * TILE_WIDTH//4*3 + TILE_WIDTH//4
    display_width = width * TILE_WIDTH + TILE_WIDTH//2

    display = pygame.display.set_mode((display_width, display_height))                                                                        
    pygame.display.set_caption("Slay_copy")
    icon = pygame.image.load(
        os.path.join(os.path.dirname(__file__), "assets", "Unit1.png")
        )
    pygame.display.set_icon(icon)

    board = Board(board_map, TILE_WIDTH)
    event_queue = EventQueue()
    renderer = Renderer(display, board)
    clock = Clock()
    game_loop = GameLoop(board, renderer, event_queue, clock, TILE_WIDTH)

    pygame.init()
    game_loop.start()

if __name__ == "__main__":
    main()
