import pygame as pg

from tile import Background, BlueWall, PurpleWall, IceFloor, PlayerSpawn, HudBackground
import config

#boneco começa no S

class Map:
    levels = {
        1: [
                "bbbbbbbbbbbbbbb",
                "               ",
                "               ",
                "               ",
                "               ",
                " wwwww         ",
                " wOggw         ",
                " wwwgwwwwwwwww ",
                "   wggggggggXw ",
                "   wwwwwwwwwww ",
                "               ",
                "               ",
                "               ",
                "               ",
                "bbbbbbbbbbbbbbb",
        ],
        2: [
                "bbbbbbbbbbbbbbb",
                "               ",
                "               ",
                "   wwwwww      ",
                "   wOgggw      ",
                "   wwwwgw      ",
                "      wgw      ",
                "      wgw      ",
                "     wwgw      ",
                "     wggwwww   ",
                "     wggggXw   ",
                "     wwwwwww   ",
                "               ",
                "               ",
                "bbbbbbbbbbbbbbb",
        ],
        3: [
                "bbbbbbbbbbbbbbb",
                "               ",
                "               ",
                "               ",
                "               ",
                "  wwwwwwwwwww  ",
                "  wOgggggggXw  ",
                "  wwwgggggwww  ",
                "    wgggggw    ",
                "    wwwwwww    ",
                "               ",
                "               ",
                "               ",
                "               ",
                "bbbbbbbbbbbbbbb",
        ],
        4: [
                "bbbbbbbbbbbbbbb",
                "               ",
                "               ",
                "          www  ",
                "  wwwww   wXw  ",
                "  wgggw   wgw  ",
                "  wgwgwwwwwgw  ",
                "  wgggggggggw  ",
                "  wwgwwwwggww  ",
                "   wgw wggggw  ",
                "   wOw wggggw  ",
                "   www wwwwww  ",
                "               ",
                "               ",
                "bbbbbbbbbbbbbbb",
        ],
        5: [
                "bbbbbbbbbbbbbbb",
                "               ",
                "               ",
                "        www    ",
                "        wOw    ",
                "        wgw    ",
                "   wwwwwwgwww  ",
                "   wggggggggw  ",
                "  wwggggggggw  ",
                "  wXggggggggw  ",
                "  wwwwwwwwwww  ",
                "               ",
                "               ",
                "               ",
                "bbbbbbbbbbbbbbb",
        ],
        6: [
                "bbbbbbbbbbbbbbb",
                "               ",
                "               ",
                "           www ",
                "           wXw ",
                "           wgw ",
                "  wwwwwww  wgw ",
                " wwgggggwwwwgw ",
                " wOggggggggggw ",
                " wwwgggwgggggw ",
                "   wwwwwwwwwww ",
                "               ",
                "               ",
                "               ",
                "bbbbbbbbbbbbbbb",
        ],
    }

    tile_mapping = {
        "b": HudBackground,
        "w": BlueWall,
        "g": IceFloor,
        #"a": WaterFloor,
        "X": PurpleWall,
        "O": PlayerSpawn,
    }

    def __init__(self, ):
        self.tiles = {}
        self.tile_group = pg.sprite.Group()

        self.__player_spawn_pos = None
    
    def add_tile(self, tile):
        x, y = tile.pos

        row = self.tiles.setdefault(x, {})
        row[y] = tile

        self.tile_group.add(tile)
    
    def clear_level(self):        
        self.tile_group.empty()
        self.tiles.clear()
    
    def set_level(self, name):
        map = self.levels.get(name)

        if not map:
            return

        tile_x, tile_y = config.tile_size

        for i, line in enumerate(map):
            y = i * tile_x

            for j, char in enumerate(line):
                x = j * tile_y

                tile_type = self.tile_mapping.get(char)

                if tile_type is None:
                    continue

                if tile_type is PlayerSpawn:
                    self.set_player_spawn_pos(x, y)

                tile = tile_type(pos=(x, y))
                self.add_tile(tile)
    
    def draw(self, surface):
        self.tile_group.draw(surface)

    def set_player_spawn_pos(self, x, y):
        self.__player_spawn_pos = (x, y)
    
    @property
    def player_spawn_pos(self):
        return self.__player_spawn_pos





