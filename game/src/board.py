import pygame
from sprites.tile import Tile
from sprites.unit import Unit

class Board:
    def __init__(self, board_map, tile_width):
        self.tile_width = tile_width
        #offsets for hexagon math
        self.x_offset = tile_width/2
        self.y_offset = tile_width/4
        self.tiles = pygame.sprite.Group()
        self.units = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self.initialize_sprites(board_map)

    def initialize_sprites(self, board_map):
        height = len(board_map)
        width = len(board_map[0])

        for i in range(height):
            for j in range(width):
                cell = board_map[i][j]

                #tile grid with hexagons
                if i%2 == 0:
                    normalized_x = j * self.tile_width
                else:
                    normalized_x = j * self.tile_width + self.x_offset
                if i == 0:
                    normalized_y = 0
                else:
                    normalized_y = i * (self.tile_width - self.y_offset)

                # cell[0] == tile colour // cell[1] == unit type
                if cell[0] == 0:
                    continue
                self.tiles.add(Tile(normalized_x, normalized_y, cell[0]))
                if not cell[1] == 0:
                    self.units.add(Unit(normalized_x, normalized_y, cell[1]))

                self.all_sprites.add(
                    self.tiles,
                    self.units
                )
