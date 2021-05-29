import pygame as pg

from tools.constants import *
from tools.game_classes import Wall, Hero, Enemy

pg.init()

window = pg.display.set_mode((WIN_X, WIN_Y))

background = pg.transform.scale(pg.image.load(IMG_FON), (WIN_X, WIN_Y))

walls = pg.sprite.Group()
walls.add(
    Wall(img=IMG_WALL, x=0, y=WIN_Y-50, size_x=WIN_X+30, size_y=50),
    Wall(img=IMG_WALL, x=WIN_X//2, y=WIN_Y//2, size_x=WIN_X//2, size_y=50)
)

hero = Hero(imgs=IMGS_HERO, x=50, y=WIN_Y-150, size_x=60, size_y=95, speed=10)
enemy = Enemy(imgs=IMGS_ENEMY, x=850, y=WIN_Y-100, size_x=80, size_y=60, speed=5, shift=200)

clock = pg.time.Clock()
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    window.blit(background, (0, 0))
    walls.draw(window)
    hero.update()
    hero.reset(window)
    enemy.update()
    enemy.reset(window)
    if hero.check_air(walls):
        hero.gravity = GRAVITY
    else:
        hero.gravity = 0
    pg.display.update()
    clock.tick(FPS)
