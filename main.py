import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

#pygame.mixer.music.set_volume(0.03)
#musica_fundo = pygame.mixer.music.load('')
#pygame.mixer.music.play(-1)a

largura = 600
altura = 700

largura_bloco = 50
altura_bloco = 50

x = 100
y = 100

x_chegada = 450
y_chegada = 450

pontos = 0
fonte = pygame.font.SysFont('arial', 30, True, True)


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Projeto Final')
relogio = pygame.time.Clock()



while True:
    relogio.tick(30)
    tela.fill((158, 239, 241))
    mensagem = f'Pintos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        # Passos do boneco
        elif event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 50
            if event.key == K_d:
                x = x + 50
            if event.key == K_w:
                y = y - 50
            if event.key == K_s:
                y = y + 50
                
        '''
    if pygame.key.get_pressed()[K_a]:
        x = x - 10
    if pygame.key.get_pressed()[K_d]:
        x = x + 10
    if pygame.key.get_pressed()[K_w]:
        y = y - 10
    if pygame.key.get_pressed()[K_s]:
        y = y + 10
'''

    boneco = pygame.draw.rect(tela, (255,0,0), (x,y,40,40))
    chegada = pygame.draw.rect(tela, (0,0,255), (x_chegada,y_chegada,40,40))

    # COLISÃO
    if boneco.colliderect(chegada):
        x = 100
        y = 100
 #       x_chegada = randint(40,600)
 #       y_chegada = randint(50,430)
        pontos = pontos + 1

    tela.blit(texto_formatado, (30,650))

    pygame.display.update()