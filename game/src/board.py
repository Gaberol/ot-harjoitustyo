import pygame
from sprites.tile import Tile
from sprites.peasant import Peasant

class Board:
    def __init__(self, board_map, tile_width):
        self.tile_width = tile_width
        self.x_offset = tile_width/2
        self.y_offset = tile_width/4
        self.tiles = pygame.sprite.Group()
        self.peasants = pygame.sprite.Group()
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

                if cell == 0:
                    continue
                if cell == 1:
                    self.tiles.add(Tile(normalized_x, normalized_y))
                if cell == 2:
                    self.peasants.add(Peasant(normalized_x, normalized_y))
                    self.tiles.add(Tile(normalized_x, normalized_y))
                
                #for k in range(width):
                #    self.tiles.add(Tile(0*self.tile_width + k*10, 0))

                self.all_sprites.add(
                    self.tiles,
                    self.peasants
                    
                )
