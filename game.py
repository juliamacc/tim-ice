import pygame as pg
from map import Map

class Game:
    def __init__(self):
        pg.init()

        self.running = False
        self.screen_size = (600, 700)
        self.points = 0

        self.map = Map()

        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(self.screen_size)
        self.font = pg.font.SysFont('arial', 30, True, True)

        pg.display.set_caption('Projeto Final')
    
    def stop_running(self):
        self.running = False
    
    def start(self):
        self.running = True

        self.__loop()
    
    def __loop(self):
        while self.running:
            self.__update()
    
    def __update(self):
        largura_bloco = 50
        altura_bloco = 50

        x = 100
        y = 100

        x_chegada = 450
        y_chegada = 450

        self.clock.tick(30)

        self.screen.fill((158, 239, 241))
        mensagem = f'Pintos: {self.points}'
        texto_formatado = self.font.render(mensagem, True, (255,255,255))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.stop_running()

            # Passos do boneco
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    x = x - 50
                if event.key == pg.K_d:
                    x = x + 50
                if event.key == pg.K_w:
                    y = y - 50
                if event.key == pg.K_s:
                    y = y + 50


        boneco = pg.draw.rect(self.screen, (255,0,0), (x,y,40,40))
        chegada = pg.draw.rect(self.screen, (0,0,255), (x_chegada,y_chegada,40,40))

        # COLISÃO
        if boneco.colliderect(chegada):
            x = 100
            y = 100
    #       x_chegada = randint(40,600)
    #       y_chegada = randint(50,430)
            pontos = pontos + 1

        self.screen.blit(texto_formatado, (30,650))

        pg.display.update()