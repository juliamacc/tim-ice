import pygame as pg

import config

class Player(pg.sprite.Sprite):
    def __init__(self, pos = None):
        pg.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pg.image.load('sprite/avatar01_red.png'))
        self.sprites.append(pg.image.load('sprite/avatar03_red.png'))

        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pg.transform.scale(self.image, (16*2.5, 40))

        if pos is None:
            pos = (100, 100)

        self.rect = self.image.get_rect()
        self.rect.topleft = pos
    
    def set_pos(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]