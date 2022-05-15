import os
import pygame
from random import randint, choices
from board import Board
from game_loop import GameLoop
from event_queue import EventQueue
from renderer import Renderer
from clock import Clock
from graph import Graph

dirname = os.path.dirname(__file__)

PLAYERS = 4
MAP_SIZE = 13

# Hard coded boards for testing

#board_map = [[(0,0), (2,0), (2,0), (2,0), (0,0), (0,0), (3,0), (3,0)],
#             [(0,0), (0,0), (2,1), (2,0), (0,0), (0,0), (3,0), (3,0)],
#             [(1,0), (1,0), (2,0), (0,0), (2,0), (3,0), (3,1), (0,0)],
#             [(1,0), (1,0), (1,0), (0,0), (2,0), (3,0), (3,0), (4,0)],
#             [(0,0), (1,0), (0,0), (1,0), (4,0), (4,1), (4,0), (4,0)],
#             [(0,0), (0,0), (1,0), (1,0), (0,0), (0,0), (4,0), (4,0)],
#             [(0,0), (1,0), (1,1), (0,0), (0,0), (4,0), (4,0), (0,0)],
#             [(0,0), (1,0), (1,0), (4,0), (4,0), (4,0), (4,0), (0,0)]]

#board_map = [[[1, 1] for t in range(8)] for r in range(8)]
#half_size = map_size / 2
#board_map = []
#for i in range(map_size):
#    row = []
#    for j in range(map_size):
#        if j <= half_size:
#            jmod = half_size - j
#        else:
#            jmod = 
#        if i <= half_size:
#            imod = i / map_size
#        else:
#            imod = 1 - (i - half_size) / map_size
#        mod = jmod + imod + 0.2
#        w = [mod/players for p in range(players)]
#        w.insert(0, 1-mod)
#        row.append([choices(
#            population=range(players+1),
#            weights=w,
#            k=1)[0],
#            choices(
#            population=[0, 1],
#            weights=[0.9, 0.1],
#            k=1)[0]
#        ])
#    board_map.append(row)

            
w = [85/PLAYERS for p in range(PLAYERS)]
w.insert(0, 15)
board_map = [[[choices(
            population=range(PLAYERS+1), 
            weights=w, 
            k=1)[0], 
            choices(
            population=[0, 1],
            weights=[0.9, 0.1],
            k=1)[0]
            ] for i in range(MAP_SIZE)] for i in range(MAP_SIZE)]

Graph(board_map)

TILE_WIDTH = 40

def main():
    height = len(board_map)
    width = len(board_map[0])
    display_height = height * TILE_WIDTH//4*3 + TILE_WIDTH//4
    display_width = width * TILE_WIDTH + TILE_WIDTH//2

    display = pygame.display.set_mode((display_width, display_height))                                                                        
    pygame.display.set_caption("Slay_copy")
    icon = pygame.image.load(
        os.path.join(dirname, "assets", "Unit1.png")
        )
    pygame.display.set_icon(icon)

    board = Board(board_map, TILE_WIDTH)
    event_queue = EventQueue()
    renderer = Renderer(display, board)
    clock = Clock()
    game_loop = GameLoop(board, renderer, event_queue, clock, TILE_WIDTH, PLAYERS)

    pygame.init()
    game_loop.start()

if __name__ == "__main__":
    main()
