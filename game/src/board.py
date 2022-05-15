import pygame
from sprites.tile import Tile
from sprites.unit import Unit

#This class uses a lot of hexagon math from https://tinyurl.com/3ad9y383
class Board:
    def __init__(self, board_map, tile_width):
        self.tile_width = tile_width
        self.map_height = len(board_map)
        self.map_width = len(board_map[0])
        self.tiles = pygame.sprite.Group()
        self.units = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        #variables for hexagon math
        self.hex_r = tile_width//2
        self.hex_h = tile_width//4

        self.initialize_sprites(board_map)

    def initialize_sprites(self, board_map):
        for i in range(self.map_height):
            for j in range(self.map_width):
                cell = board_map[i][j]

                # Tile grid with hexagons
                if i%2 == 0:
                    normalized_x = j * self.tile_width
                else:
                    normalized_x = j * self.tile_width + self.hex_r
                if i == 0:
                    normalized_y = 0
                else:
                    normalized_y = i * (self.tile_width - self.hex_h)

                # cell[0] == tile colour // cell[1] == unit type
                if cell[0] == 0: continue
                self.tiles.add(Tile(normalized_x, normalized_y, (j, i), cell[0]))
                if not cell[1] == 0:
                    self.units.add(Unit(normalized_x, normalized_y, cell[1]))

                self.all_sprites.add(
                    self.tiles,
                    self.units
                )

    def mouse_event(self, pos):
        x_section = pos[0] // self.tile_width
        y_section = pos[1] // (self.hex_h*3)
        sect_pxl_x = pos[0] % self.tile_width
        sect_pxl_y = pos[1] % (self.hex_h*3)
        m = self.hex_h / self.hex_r
        if y_section % 2 == 0:   # Section type A
            if sect_pxl_y < (self.hex_h - sect_pxl_x * m):
                x_section -= 1
                y_section -= 1
            elif sect_pxl_y < (-self.hex_h + sect_pxl_x * m):
                y_section -= 1
        else:                    # Section type B
            if sect_pxl_x >= self.hex_r:
                if sect_pxl_y < (2 * self.hex_h - sect_pxl_x * m):
                    y_section -= 1
            else:
                if sect_pxl_y < (sect_pxl_x * m):
                    y_section -= 1
                else:
                    x_section -= 1
        if x_section == self.map_width or y_section == self.map_height:
            return (-1, -1)
        return (x_section, y_section)
