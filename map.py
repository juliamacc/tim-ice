import pygame as pg

class Map:
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.msprites = []
        self.msprites.append(pg.image.load('sprite/background.png'))
        self.msprites.append(pg.image.load('sprite/background (HUD).png'))
        self.msprites.append(pg.image.load('sprite/floor.png'))
        self.msprites.append(pg.image.load('sprite/floor (water).png'))
        self.msprites.append(pg.image.load('sprite/wall (blue).png'))
        self.msprites.append(pg.image.load('sprite/wall (purple).png'))

        self.map = [ 


        ]

        
