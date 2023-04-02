import pygame
from pygame.locals import *
from sys import exit
from random import randint
import os

#tela
largura = 1000
altura = 650

#formiga:
formiga_xtamanho = 110
formiga_ytamanho = 110
x_formiga = (largura // 2) - (formiga_xtamanho // 2)
y_formiga = 487
formiga_c = 0

#alien:
alien_xtamanho = 130
alien_ytamanho = 130
x_alien = 0
y_alien = 10

#fogo
fogo_xtamanho = 35
fogo_ytamanho = 65
x_fogo = 50
y_fogo = 30

#arquivos e textos
fundo1 = pygame.image.load('inicio.png')
fundo1 = pygame.transform.scale(fundo1, (largura, altura))


fundo = pygame.image.load('estrada.png')
fundo = pygame.transform.scale(fundo, (largura, altura))

formiga_d = pygame.image.load('bixod.png')
formiga_e = pygame.image.load('bixoe.png')
formiga_d = pygame.transform.scale(formiga_d, (formiga_xtamanho, formiga_ytamanho))
formiga_e = pygame.transform.scale(formiga_e, (formiga_xtamanho, formiga_ytamanho))
formiga = formiga_d

alien_d = pygame.image.load('alien_d.png')
alien_e = pygame.image.load('alien_e.png')
alien_d = pygame.transform.scale(alien_d, (alien_xtamanho, alien_ytamanho))
alien_e = pygame.transform.scale(alien_e, (alien_xtamanho, alien_ytamanho))
alien = alien_d

fogo = pygame.image.load('meteoro.png')
fogo = pygame.transform.scale(fogo, (fogo_xtamanho, fogo_ytamanho))

#booleanos
jogo = False
morreu = False
tiro = False

#programa
pygame.init()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('formiguinha')
clock = pygame.time.Clock()
fonte1 = pygame.font.SysFont('kristenitc', 78, True, True)
fonte2 = pygame.font.SysFont('kristenitc', 36, True, True)
fonte = pygame.font.SysFont('arial', 40, True, True)
fontet = pygame.font.SysFont('arial', 60, True, True)

#definicioes
def respown():
    tiro = False
    x_fogo = x_alien + 50
    y_fogo = 30
    return[tiro, x_fogo, y_fogo]

def recomeco():
    global x_alien, x_formiga, x_fogo, y_fogo, tiro
    x_alien = 0
    x_formiga = (largura // 2) - (formiga_xtamanho // 2)
    x_fogo = 50
    y_fogo = 30
    tiro = False

while True:
    texto = fonte1.render('formiguinha', True, (126, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #botoes
    if event.type == pygame.MOUSEBUTTONDOWN:
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        #para deizer onde fica as posicoes do rect, colocamos
        #o x e o y de ambas as pontas com (x, y, xt, yt) o calculo:
        #xpos > x and ypos > y and x < x + xt and ypos < yt:
        if x > 395 and y > 200 and x < 595 and y < 264:
            jogo = True
            while jogo:
                clock.tick(300)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()

                # robo:
                if pygame.key.get_pressed()[K_RIGHT] and x_formiga < 900:
                    x_formiga += 3
                    formiga = formiga_d
                if pygame.key.get_pressed()[K_LEFT] and x_formiga > -10:
                    x_formiga -= 3
                    formiga = formiga_e

                # tiro do alien (fogo):
                if pygame.key.get_pressed()[K_s]:
                    tiro = True
                if tiro:
                    y_fogo += 3
                if y_fogo > 597:
                    tiro = respown()[0]
                    x_fogo = respown()[1]
                    y_fogo = respown()[2]

                # alien:
                if pygame.key.get_pressed()[K_d] and x_alien < 890:
                    x_alien += 2
                    if tiro == False:
                        x_fogo += 2
                    alien = alien_d
                    # x_lazer += 2
                if pygame.key.get_pressed()[K_a] and x_alien > -20:
                    x_alien -= 2
                    if tiro == False:
                        x_fogo -= 2
                    alien = alien_e
                # colizao:
                formiga_c = pygame.draw.rect(tela, (255, 0, 0), ((x_formiga + 35), (y_formiga + 43), 40, 40))
                fogo_c = pygame.draw.rect(tela, (255, 0, 0), ((x_fogo + 2), (y_fogo), 35, 65))
                if fogo_c.colliderect(formiga_c):
                    morreu = True
                    while morreu:
                        tela.fill((255, 0, 0))
                        for event in pygame.event.get():
                            # entao ele podera sair
                            if event.type == QUIT:
                                pygame.quit()
                                exit()
                            # ou se clicar r ele reinicia
                            if event.type == KEYDOWN:
                                if event.key == K_r:
                                    recomeco()
                                    morreu = False
                                if event.key == K_s:
                                    pygame.quit()
                                    exit()

                        tela.blit(fontet.render('A formiguinha foi extinta', True, (0, 0, 0)), (220, 90))
                        tela.blit(fonte.render('Precione r para tentar denovo', True, (0, 0, 0)), (265, 295))
                        tela.blit(fonte.render('ou s para arregar', True, (0, 0, 0)), (361, 332))

                        pygame.display.flip()

                # prints
                tela.blit(tela, (0, 0))
                tela.blit(fundo, (0, 0))
                tela.blit(formiga, (x_formiga, y_formiga))
                tela.blit(fogo, (x_fogo, y_fogo))
                tela.blit(alien, (x_alien, y_alien))

                pygame.display.flip()

        if x > 395 and y > 400 and x < 595 and y < 494:
            pygame.quit()
            exit()
    tela.blit(fundo1, (0, 0))
    tela.blit(texto, (224, 40))
    texto_play = fonte2.render('começar', True, (111, 115, 114))
    texto_exit = fonte2.render('sair', True, (111, 115, 114))
    play = pygame.draw.rect(tela, (49, 0, 0), (395, 200, 200, 64))
    sair = pygame.draw.rect(tela, (49, 0, 0), (395, 400, 200, 64))
    tela.blit(texto_play, (408, 209))
    tela.blit(texto_exit, (454, 409))



    pygame.display.flip()