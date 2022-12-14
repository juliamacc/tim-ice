import pygame as pg

import config

class Tile(pg.sprite.Sprite):
    image = None

    def __init__(self, pos):
        super().__init__()

        self.pos = pg.Vector2(pos)

        self.image = pg.transform.scale(self.default_image, config.tile_size)
        self.rect = pg.Rect(*pos, *config.tile_size)

class Background(Tile):
    default_image = pg.image.load('sprite/background.png')

class HudBackground(Tile):
    default_image = pg.image.load('sprite/background_hud.png')

class BlueWall(Tile):
    default_image = pg.image.load('sprite/wall_blue.png')

class Water(Tile):
    default_image = pg.image.load('sprite/water.png')


class Floor(Tile):
    default_image = pg.image.load('sprite/floor.png')

class PlayerSpawn(Floor):
    default_image = pg.image.load('sprite/floor.png')
    
class PurpleFloor(Floor):
    default_image = pg.image.load('sprite/floor_purple.png')
