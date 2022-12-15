import pygame as pg
from map import Map
from player import Player
import os

import config
from tile import Floor, Water, PurpleFloor


def play_sound(path, volume=1):
    sound = pg.mixer.Sound(path)
    sound.set_volume(volume)

    sound.play()


class Game:    
    def __init__(self):
        pg.init()
        pg.mixer.init()

        self.screen_size = (600, 600)
        self.running = False
        self.points = 0
        self.level = 0
        
        self.current_state = None
        self.states = {
            "start": self.start_state,
            "main": self.main_state,
            "game_over": self.game_over_state,
            "victory": self.victory_state,
        }

        self.all_sprites = pg.sprite.Group()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(self.screen_size)

        self.font2 = pg.font.match_font('Flipps-Regular.otf')


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
            self.points += 1

            self.map.add_tile(Water(pos=(x, y)))

            play_sound(os.path.join(self.audios_folder, 'steps.wav'), 0.1)
        
        if isinstance(new_tile, PurpleFloor):
            if self.level + 1 in self.map.levels:
                self.next_level()
                play_sound(os.path.join(self.audios_folder, 'levelup.wav'))
    
    def is_player_dead(self):
        x, y = self.player.rect.topleft

        adjacent_tiles = self.map.get_adjacent_tiles(x, y)

        for tile in adjacent_tiles:
            if isinstance(tile, Floor):
                return False
        
        return True

    def load_files(self):
        images_folder = os.path.join(os.getcwd(), 'sprite')
        self.audios_folder = os.path.join(os.getcwd(), 'audio')
        #self.level_sound = os.path.join(audios_folder, 'levelup.wav')
        self.timice_screen = os.path.join(images_folder, 'titlescreen.png')
        self.timice_screen = pg.image.load(self.timice_screen).convert()
        self.timice_dead = os.path.join(images_folder, 'avatar03_red.png')
        self.timice_dead = pg.image.load(self.timice_dead).convert()

    def get_font(self, size):
        return pg.font.Font("DigitalDisco.ttf", size)


    def show_text(self, text, size, color, x, y, centered=True):
        font = self.get_font(size)
        
        text = font.render(text, True, color)
        text_rect = text.get_rect()

        if centered:
            text_rect.midtop = (x, y)
        else:
            text_rect.topleft = (x, y)

        self.screen.blit(text, text_rect)

    def show_start_screen(self, x, y):
        self.screen.fill((50, 51, 83))

        start_screen_rect = self.timice_screen.get_rect()
        start_screen_rect.midtop = (x, y)

        self.screen.blit(self.timice_screen, start_screen_rect)
        
        pg.display.update()


    def start_state(self):
        self.show_start_screen(300, 0)

        self.wait(pg.K_s)

        self.change_state("main")


    def main_state(self):
        self.level = 0
        self.points = 0
        self.next_level()

        while self.running:
            # check if player died
            if self.is_player_dead():
                if not self.level + 1 in self.map.levels:
                    self.change_state("victory")
                    break

                self.player.set_dead()
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

            self.show_text(f"Level: {self.level}", 30, "#ffffff", 30, 50, centered=False)
            self.show_text(f"Points: {self.points}", 30, "#ffffff", 450, 50, centered=False)

            pg.display.update()


    def game_over_state(self):
        play_sound(os.path.join(self.audios_folder, 'defeat.wav'))
        
        self.show_gameover_screen(300, 300)

        self.wait()

        self.change_state("main")
        

    def show_gameover_screen(self, x, y):
        self.screen.fill((50, 51, 82))

        self.map.draw(self.screen)
        self.all_sprites.draw(self.screen)

        self.show_text('GAME OVER', 60, (255,127,127), 300, 75)
        self.show_text('Perdeste, otario', 20, (255,127,127), 300, 135)

        self.show_text('Press any key to restart', 30, (255,255,255), 300, 500)

        pg.display.update()

    def victory_state(self):
        play_sound(os.path.join(self.audios_folder, 'win.wav'))
        
        self.show_victory_screen(300, 300)

        self.wait()

        self.change_state("start")
        

    def show_victory_screen(self, x, y):
        self.screen.fill((50, 51, 82))

        self.map.draw(self.screen)
        self.all_sprites.draw(self.screen)

        self.show_text('VICTORY', 60, (255, 255, 153), 300, 75)
        self.show_text('Ganhaste, otario', 20, (255, 255, 153), 300, 135)

        self.show_text('Press any key to return', 30, (255,255,255), 300, 500)

        pg.display.update()


    def wait(self, *keys):
        waiting = True
        
        while waiting:
            self.clock.tick(30)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                    
                elif event.type == pg.KEYDOWN:
                    if not keys:
                        return
                    
                    if event.key in keys:
                        waiting = False