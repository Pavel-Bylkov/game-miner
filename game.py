import pygame as pg

from tools.constants import *

pg.init()

window = pg.display.set_mode((WIN_X, WIN_Y))

background = pg.transform.scale(pg.image.load(IMG_FON), (WIN_X, WIN_Y))

clock = pg.time.Clock()
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    window.blit(background, (0, 0))
    pg.display.update()
    clock.tick(FPS)
