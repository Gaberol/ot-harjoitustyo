import os
import pygame

dirname = os.path.dirname(__file__)

class Unit(pygame.sprite.Sprite):
    def __init__(self, x, y, unit_type):
        super().__init__()
        
        self.type = unit_type

        self.image = pygame.image.load(os.path.join(dirname, "..", "assets", f"Unit{self.type}.png"))

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        