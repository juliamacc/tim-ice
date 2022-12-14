import pygame as pg
#from map import Map
from player import Player
import sprite
import os

class Game:
    def __init__(self):
        pg.init()
        #pg.mixer.init()
        f = 32
        self.running = False
        self.screen_size = (600, 600)
        #self.map = Map()
        #self.player = Player()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(self.screen_size)
        self.font = pg.font.match_font('arial')
        self.load_files()

        self.points = 0
        self.level = 0

        pg.display.set_caption('Tim Ice')
    
    def stop_running(self):
        self.running = False
    
    def start(self):
        self.all_sprites = pg.sprite.Group()
        self.running = True
        self.__loop()
    
    def __loop(self):
        while self.running:
            self.__update()
    
    def __update(self):

        largura_bloco = 50
        altura_bloco = 50

        #x = 100
        #y = 100

        x_chegada = 350
        y_chegada = 350

        self.clock.tick(30)

        self.screen.fill((50, 51, 82))
        #mensagem = f'Level: {self.level}'
        #texto_formatado = self.font.render(mensagem, True, (255,255,255))

        self.update_sprites()
        self.draw_sprites()

        boneco = pg.draw.rect(self.screen, (255,0,0), (x,y,40,40))
        chegada = pg.draw.rect(self.screen, (0,0,255), (x_chegada,y_chegada,40,40))

        # COLISÃO
        if boneco.colliderect(chegada):
            x = 100
            y = 100
    #       x_chegada = randint(40,600)
    #       y_chegada = randint(50,430)
            pontos = pontos + 1
       # self.screen.blit(texto_formatado, (30,650))

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
    
    def update_sprites(self):
        self.all_sprites.update()
    
    def draw_sprites(self):
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def load_files(self):
        images_folder = os.path.join(os.getcwd(), 'sprite')
        #self.audios_folder = os.path.join(os.getcwd(), 'audios')
        #self.spritesheet = os.path.join(images_folder, 'spritesheet')
        #self.timice_logo = os.path.join(images_folder, 'title.png')
        #self.timice_logo = pg.image.load(self.timice_logo).convert()
        #self.timice_logo = pg.transform.scale(self.timice_logo, (306, 84))
        self.timice_screen = os.path.join(images_folder, 'titlescreen (500x600).png')
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