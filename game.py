import pygame as pg
from map import Map
from player import Player
import os

class Game:    
    def __init__(self):
        pg.init()
        #pg.mixer.init()

        self.screen_size = (600, 600)
        self.running = False
        self.points = 0
        self.level = 0

        self.all_sprites = pg.sprite.Group()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(self.screen_size)
        self.font = pg.font.match_font('arial')

        self.map = Map()
        self.player = None

        self.load_files()

        pg.display.set_caption('Tim Ice')
    
    def stop_running(self):
        self.running = False
    
    def start(self):
        self.running = True
        self.map.set_level(2)

        self.spawn_player()

        self.__loop()
    
    def spawn_player(self):
        pos = self.map.player_spawn_pos

        self.player = Player(pos)

        self.all_sprites.add(self.player)
    
    def __loop(self):
        while self.running:
            self.__update()
            self.__draw()
    
    def __update(self):
        self.clock.tick(30)

        self.events()

        self.all_sprites.update()

    def __draw(self):
        self.screen.fill((50, 51, 82))

        self.map.draw(self.screen)

        self.all_sprites.draw(self.screen)

        pg.display.update()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
             self.stop_running()

             #Passos do boneco
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    x = x - 50
                if event.key == pg.K_d:
                    x = x + 50
                if event.key == pg.K_w:
                    y = y - 50
                if event.key == pg.K_s:
                    y = y + 50

    def load_files(self):
        images_folder = os.path.join(os.getcwd(), 'sprite')
        #self.audios_folder = os.path.join(os.getcwd(), 'audios')
        #self.spritesheet = os.path.join(images_folder, 'spritesheet')
        #self.timice_logo = os.path.join(images_folder, 'title.png')
        #self.timice_logo = pg.image.load(self.timice_logo).convert()
        #self.timice_logo = pg.transform.scale(self.timice_logo, (306, 84))
        self.timice_screen = os.path.join(images_folder, 'titlescreen.png')
        self.timice_screen = pg.image.load(self.timice_screen).convert()

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

    def start_screen(self):
        #pg.mixer.music.load()
        self.show_start_screen(300, 0)

        pg.display.flip()
        self.wait()
    
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


    def game_over(self):
        pass