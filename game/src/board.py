import pygame
from sprites.tile import Tile
from sprites.peasant import Peasant

class Board:
    def __init__(self, board_map, tile_width):
        self.tile_width = tile_width
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
                normalized_x = j * self.tile_width
                normalized_y = i * self.tile_width

                if cell == 0:
                    continue
                if cell == 1:
                    self.tiles.add(Tile(normalized_x, normalized_y))
                if cell == 2:
                    self.peasants.add(Peasant(normalized_x, normalized_y))
                    self.tiles.add(Tile(normalized_x, normalized_y))

                self.all_sprites.add(
                    self.tiles,
                    self.peasants
                )

if __name__ == "__main__":
    board = Board([[0, 1],[1, 1]], 50)
