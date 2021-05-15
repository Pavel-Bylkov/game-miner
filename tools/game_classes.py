import pygame as pg

from .constants import *


class Wall(pg.sprite.Sprite):
    def __init__(self, img, x, y, size_x, size_y):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(img), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

