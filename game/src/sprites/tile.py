import os
import pygame

dirname = os.path.dirname(__file__)

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "Tile.png")
            )
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.colors = [
            (0, 0, 0),
            (140, 110, 0),
            (80, 210, 0),
            (10, 85, 0),
            (225, 200, 0)
        ]
        self.color = self.colors[color]

        color_mask = pygame.Surface(self.image.get_size()).convert_alpha()
        color_mask.fill((self.color))
        self.image.blit(color_mask, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
