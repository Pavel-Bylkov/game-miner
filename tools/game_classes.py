import pygame as pg

from .constants import *


class Wall(pg.sprite.Sprite):
    def __init__(self, img, x, y, size_x, size_y):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(img), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Person(pg.sprite.Sprite):
    def __init__(self, imgs: list, x: int, y: int, size_x: int, size_y: int, speed: int):
        super().__init__()
        self.imgs = [pg.transform.scale(pg.image.load(imgs[0]), (size_x, size_y)),
                     pg.transform.scale(pg.image.load(imgs[1]), (size_x, size_y)),
                     pg.transform.scale(pg.image.load(imgs[2]), (size_x, size_y))]
        self.direction = "left"
        self.speed = speed
        self.image = self.imgs[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.gravity = 0

    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def change_skin(self, direction):
        self.direction = direction
        x, y = self.rect.x, self.rect.y
        if self.direction == "left":
            self.image = self.imgs[0]
        elif self.direction == "right":
            self.image = self.imgs[2]
        else:
            self.image = self.imgs[1]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def check_air(self, things):
        return not pg.sprite.spritecollideany(self, things)


class Hero(Person):
    def update(self):
        keys = pg.key.get_pressed()
        self.rect.y += self.gravity
        if keys[pg.K_w]:
            if self.direction != "up":
                self.change_skin(direction="up")
            self.rect.y -= self.speed
        if keys[pg.K_s]:
            if self.direction != "down":
                self.change_skin(direction="down")
            self.rect.y += self.speed
        if keys[pg.K_a]:
            if self.direction != "left":
                self.change_skin(direction="left")
            self.rect.x -= self.speed
        if keys[pg.K_d]:
            if self.direction != "right":
                self.change_skin(direction="right")
            self.rect.x += self.speed
