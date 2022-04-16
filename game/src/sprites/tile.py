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

        self.colors = [
            (0, 0, 0),
            (10, 100, 0),
            (50, 150, 0),
            (200, 200, 0),
            (150, 130, 0)
        ]
        self.color = self.colors[color]

        colorMask = pygame.Surface(self.image.get_size()).convert_alpha()
        colorMask.fill((self.color))
        self.image.blit(colorMask, (0,0), special_flags = pygame.BLEND_RGBA_MULT)

        self.rect.x = x
        self.rect.y = y
