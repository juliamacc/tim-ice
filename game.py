import pygame as pg
from map import Map
from player import Player
import os

import config
from tile import Floor, Water, PurpleFloor

class Game:    
    def __init__(self):
        pg.init()
        #pg.mixer.init()

        self.screen_size = (600, 600)
        self.running = False
        self.points = 0
        self.level = 0
        
        self.current_state = None
        self.states = {
            "start": self.start_state,
            "main": self.main_state,
            "game_over": self.game_over_state,
        }

        self.all_sprites = pg.sprite.Group()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(self.screen_size)
        self.font = pg.font.match_font('Flipps-Regular.otf')

        self.map = Map()
        self.player = None

        self.load_files()

        pg.display.set_caption('Tim Ice')
    
    def stop_running(self):
        self.running = False
        
    def change_state(self, name):
        state = self.states.get(name)

        if state:
            self.current_state = state
    
    def start(self):
        self.running = True
        self.change_state("start")

        self.__loop()
    
    def __loop(self):
        while self.current_state and self.running:
            self.current_state()


    def next_level(self):
        self.level += 1

        self.all_sprites.empty()
        self.map.set_level(self.level)

        self.spawn_player()
    
    def spawn_player(self):
        pos = self.map.player_spawn_pos

        self.player = Player(pos)
        self.all_sprites.add(self.player)


    def events(self):
        tx, ty = config.tile_size
        move_delta = {
            pg.K_a: (-tx, 0),
            pg.K_d: (tx, 0),
            pg.K_w: (0, -ty),
            pg.K_s: (0, ty),
        }

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.stop_running()
             
            elif event.type == pg.KEYDOWN:
                move = move_delta.get(event.key)

                if move:
                    self.move(*move)
    
    def move(self, dx, dy):
        x, y = self.player.rect.topleft

        new_pos = (x + dx, y + dy)
        new_tile = self.map.get_tile(*new_pos)

        if isinstance(new_tile, Floor):
            self.player.set_pos(new_pos)

            self.map.add_tile(Water(pos=(x, y)))
        
        if isinstance(new_tile, PurpleFloor):
            self.next_level()


    def load_files(self):
        images_folder = os.path.join(os.getcwd(), 'sprite')
        #self.audios_folder = os.path.join(os.getcwd(), 'audios')
        self.timice_screen = os.path.join(images_folder, 'titlescreen.png')
        self.timice_screen = pg.image.load(self.timice_screen).convert()
        self.timice_dead = os.path.join(images_folder, 'avatar03_red.png')
        self.timice_dead = pg.image.load(self.timice_dead).convert()


    def show_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font, size)
        text = font.render(text, True, color)
        text_rect = text.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text, text_rect)

    def show_start_screen(self, x, y):
        self.screen.fill((50, 51, 83))
        start_screen_rect = self.timice_screen.get_rect()
        start_screen_rect.midtop = (x, y)
        self.screen.blit(self.timice_screen, start_screen_rect)
        pg.display.update()


    def start_state(self):
        #pg.mixer.music.load()
        self.show_start_screen(300, 0)

        self.wait()

        self.change_state("main")


    def main_state(self):
        self.next_level()
        
        self.show_text('asdfgrs', 18, (0, 0, 0), 20, 20)

        while self.running:
            # check if player died
            if False:
                self.change_state("game_over")
                break
                
            # update
            self.clock.tick(30)

            self.events()
            self.all_sprites.update()

            # render
            self.screen.fill((50, 51, 82))
        
            self.map.draw(self.screen)
            self.all_sprites.draw(self.screen)

            pg.display.update()


    def game_over_state(self):
        #pg.mixer.music.load()
        self.show_gameover_screen(300, 300)

        self.wait()
        

    def show_gameover_screen(self, x, y):
        self.screen.fill((50, 51, 83))
        gameover_screen_rect = self.timice_dead.get_rect()
        gameover_screen_rect.midtop = (x, y)
        self.screen.blit(self.timice_dead, gameover_screen_rect)
    



    def wait(self):
        waiting = True
        
        while waiting:
            self.clock.tick(30)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                    
                elif event.type == pg.KEYUP:
                    if event.key == pg.K_s:
                        waiting = False