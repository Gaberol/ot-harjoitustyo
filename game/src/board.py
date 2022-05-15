import pygame
from sprites.tile import Tile
from sprites.unit import Unit

#This class uses a lot of hexagon math from https://tinyurl.com/3ad9y383
class Board:
    def __init__(self, board_map, tile_width):
        self.board_map = board_map
        self.tile_width = tile_width
        self.map_height = len(board_map)
        self.map_width = len(board_map[0])
        self.tiles = pygame.sprite.Group()
        self.units = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        #variables for hexagon math
        self.hex_r = tile_width//2
        self.hex_h = tile_width//4

        self._initialize_sprites(board_map)

    def _initialize_sprites(self, board_map):
        for i in range(self.map_height):
            for j in range(self.map_width):
                cell = board_map[i][j]

                xy = self._normalize_xy(j,i)

                # cell[0] == tile colour // cell[1] == unit type
                if cell[0] == 0: continue
                self.tiles.add(Tile(xy[0], xy[1], cell[0]))
                if not cell[1] == 0:
                    self.units.add(Unit(xy[0], xy[1], (j,i), cell[1]))

                self.all_sprites.add(
                    self.tiles,
                    self.units
                )

    def _normalize_xy(self, x, y):
        if y % 2 == 0:
            normalized_x = x * self.tile_width
        else:
            normalized_x = x * self.tile_width + self.hex_r
        if y == 0:
            normalized_y = 0
        else:
            normalized_y = y * (self.tile_width - self.hex_h)
        return (normalized_x, normalized_y)

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
        return [x_section,
                y_section,
                self.board_map[y_section][x_section][0],
                self.board_map[y_section][x_section][1]]

    def move_unit(self, pos, start, target):
        unit_type = start[3]
                                                                                
        unit = [u for u in self.units if
            u.get_coordinates() == (start[0], start[1])][0]
        self.board_map[start[1]][start[0]][1] = 0
        unit.kill()
        target_x = target[0]
        target_y = target[1]
        self.board_map[target_y][target_x][1] = unit_type
        xy = self._normalize_xy(target_x, target_y)
        self.units.add(Unit(xy[0], xy[1], (target_x, target_y), unit_type))
        self.all_sprites.add(self.units)
