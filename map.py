import pygame as pg
import sprite

pg.init()

class Map:
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.msprites = []
        self.msprites.append(pg.image.load('sprite/background.png')) #0
        self.msprites.append(pg.image.load('sprite/background (HUD).png')) #1
        self.msprites.append(pg.image.load('sprite/floor.png')) #2
        self.msprites.append(pg.image.load('sprite/floor (water).png')) #3
        self.msprites.append(pg.image.load('sprite/wall (blue).png')) #4
        self.msprites.append(pg.image.load('sprite/wall (purple).png')) #5

        self.hudbackground = self.msprites[1]
        self.hudbackground = pg.transform.scale(self.hudbackground, (40, 40))
        self.icefloor = self.msprites[2]
        self.icefloor = pg.transform.scale(self.icefloor, (40, 40))
        self.waterfloor = self.msprites[3]
        self.waterfloor = pg.transform.scale(self.waterfloor, (40, 40))
        self.bluewall = self.msprites[4]
        self.bluewall = pg.transform.scale(self.bluewall, (40, 40))
        self.purplewall = self.msprites[5]
        self.purplewall = pg.transform.scale(self.purplewall, (40, 40))


        self.map = [""


        ]

        pg.display.update()

        while True:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    exit()