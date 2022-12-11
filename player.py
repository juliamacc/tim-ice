import pygame as pg
from pygame.locals import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos = None):
        pg.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pg.image.load('sprite/avatar01 (red).png'))
        self.sprites.append(pg.image.load('sprite/avatar03 (red).png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pg.transform.scale(self.image, (16*2.5, 40))

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100

        #if pos is None:
        #    pos = (0, 0)
        #if size is None:
        #    size = (40, 40)
        #self.pos = pg.Vector2(pos)
        #self.size = pg.Vector2(size)