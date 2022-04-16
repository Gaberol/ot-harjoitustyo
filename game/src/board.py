import pygame
from sprites.tile import Tile
from sprites.unit import Unit

class Board:
    def __init__(self, board_map, tile_width):
        self.tile_width = tile_width
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

                if i%2 == 0:
                    normalized_x = j * self.tile_width
                else:
                    normalized_x = j * self.tile_width + self.x_offset
                if i == 0:
                    normalized_y = 0
                else:
                    normalized_y = i * (self.tile_width - self.y_offset)

                cell_tile = cell[0]
                cell_unit = cell[1]

                if cell_tile == 0:
                    continue
                self.tiles.add(Tile(normalized_x, normalized_y))
                
                if cell_unit == 0:
                    continue
                self.units.add(Unit(normalized_x, normalized_y, cell_unit))

                self.all_sprites.add(
                    self.tiles,
                    self.units
                )
