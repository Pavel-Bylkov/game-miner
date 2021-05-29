import os

WIN_X, WIN_Y = 1600, 900

FPS = 40  # задает обновление экрана со скоростью 40 кадров в секунду

GRAVITY = 5

# картинки
IMG_FON = f"img{os.sep}brick-wall.jpg"
IMG_WALL = f"img{os.sep}plat.png"
IMG_WALL_L = f"img{os.sep}plat_l.png"
IMG_WALL_R = f"img{os.sep}plat_r.png"

IMG_GAMEOVER = f"img{os.sep}gameover.jpeg"

# списки картинок персонажей [левая, спина, правая]
IMGS_HERO = [f"img{os.sep}Asset 59@4x.png", f"img{os.sep}Asset 73@4x.png", f"img{os.sep}Asset 60@4x.png"]

IMGS_ENEMY = [f"img{os.sep}spider{os.sep}shutterstock_783589831-[Converted]-{i}.png" for i in range(2, 23)]

