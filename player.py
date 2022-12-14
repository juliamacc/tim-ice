import pygame as pg
from pygame.locals import *
import sprite


class Player(pg.sprite.Sprite):
    def __init__(self, pos = None):
        pg.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pg.image.load('sprite/avatar01 (red).png'))
        self.sprites.append(pg.image.load('sprite/avatar03 (red).png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pg.transform.scale(self.image, (16*2.5, 40))

        if pos is None:
            pos = (100, 100)
        self.pos = pg.Vector2(pos)

        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    
    # def events(self):
    #     for event in pg.event.get():
    #         if event.type == pg.QUIT:
    #          self.stop_running()
    #         # Passos do boneco
    #         elif event.type == pg.KEYDOWN:
    #             if event.key == pg.K_a:
    #                 xp = xp - 50
    #             if event.key == pg.K_d:
    #                 xp = xp + 50
    #             if event.key == pg.K_w:
    #                 yp = yp - 50
    #             if event.key == pg.K_s:
    #                 yp = yp + 50
