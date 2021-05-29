import pygame as pg
from time import time

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


class Enemy(pg.sprite.Sprite):
    def __init__(self, imgs: list, x: int, y: int, size_x: int, size_y: int, speed: int, shift: int):
        super().__init__()
        self.imgs_right = [pg.transform.scale(pg.image.load(imgs[i]), (size_x, size_y)) for i in range(len(imgs))]
        self.imgs_left = [pg.transform.flip(self.imgs_right[i], True, False) for i in range(len(imgs))]
        self.direction = "left"
        self.speed = speed
        self.current_skin = 0
        self.image = self.imgs_left[0]
        self.rect = self.image.get_rect()
        self.start_pos = (x, y)
        self.shift = shift
        self.rect.x = x
        self.rect.y = y
        self.gravity = 0
        self.last_time = time()  # сохраняем текущее время в секундах с 1970 года

    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def change_direction(self, direction):
        self.direction = direction
        x, y = self.rect.x, self.rect.y
        if self.direction == "left":
            self.image = self.imgs_left[self.current_skin]
        else:
            self.image = self.imgs_right[self.current_skin]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def next_skin(self):
        x, y = self.rect.centerx, self.rect.centery
        if self.current_skin < len(self.imgs_left):
            self.current_skin += 1
        else:
            self.current_skin = 0
        if self.direction == "left":
            self.image = self.imgs_left[self.current_skin]
        else:
            self.image = self.imgs_right[self.current_skin]
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = x, y

    def check_air(self, things):
        return not pg.sprite.spritecollideany(self, things)

    def update(self):
        if self.direction == "left" and self.rect.x < self.start_pos[0] - self.shift:
            self.change_direction("right")
        if self.direction == "right" and self.rect.x > self.start_pos[0] + self.shift:
            self.change_direction("left")
        if self.direction == "left":
            self.rect.x -= self.speed
        if self.direction == "right":
            self.rect.x += self.speed
        if time() - self.last_time > 0.5:
            self.next_skin()
