import pygame as pg

class Player:
    def __init__(self, pos = None, size = None):
        if pos is None:
            pos = (0, 0)

        if size is None:
            size = (40, 40)
        
        self.pos = pg.Vector2(pos)
        self.size = pg.Vector2(size)