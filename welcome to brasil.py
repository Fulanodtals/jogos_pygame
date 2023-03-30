# jogos_pygame
#Jogos feitos por fulanodtals, para fins de experiência,  aprendizagem e entretenimento. 
import pygame
from pygame.locals import *
from sys import exit


#tela:
largura = 800
altura = 600

#p1:
x_p1 = 10
y_p1 = 330
p1_xtamanho = 200
p1_ytamanho = 270

#p2:
x_p2 = 590
y_p2 = 330
p2_xtamanho = 200
p2_ytamanho = 270

#bala_1:
qtiros_1 = 1
x_bala1 = 130
y_bala1 = 455
bala1_xtamanho = 40
bala1_ytamanho = 40

#bala_2:
qtiros_2 = 1
x_bala2 = 690
y_bala2 = 453
bala2_xtamanho = 40
bala2_ytamanho = 40


#arquivos:
parede = pygame.image.load('parede.png')
parede = pygame.transform.scale(parede, (largura, altura))

bala_1 = pygame.image.load('bala.png')
bala_1 = pygame.transform.scale(bala_1, (bala1_xtamanho, bala1_ytamanho))

bala_2 = pygame.image.load('bala.png')
bala_2 = pygame.transform.scale(bala_2, (bala2_xtamanho, bala2_ytamanho))


tiro_1 = pygame.image.load('tiro_1.png')
tiro_1 = pygame.transform.scale(tiro_1, (p1_xtamanho + 40, p1_ytamanho))

tiro_2 = pygame.image.load('tiro_2.png')
tiro_2 = pygame.transform.scale(tiro_2, (p2_xtamanho + 20, p2_ytamanho ))

carrega_1 = pygame.image.load('carrega_1.png')
carrega_1 = pygame.transform.scale(carrega_1, (p1_xtamanho, p1_ytamanho))

carrega_2 = pygame.image.load('carrega_2.png')
carrega_2 = pygame.transform.scale(carrega_2, (p2_xtamanho, p2_ytamanho))

defende_1 = pygame.image.load('defende_1.png')
defende_1 = pygame.transform.scale(defende_1, (p1_xtamanho, p1_ytamanho))

defende_2 = pygame.image.load('defende_2.png')
defende_2 = pygame.transform.scale(defende_2, (p2_xtamanho, p2_ytamanho))

p1 = defende_1
p2 = defende_2

#colisao:
p1c = p1.get_rect()
p2c = p2.get_rect()
balac_1 = bala_1.get_rect()
balac_2 = bala_2.get_rect()
p1c.x = x_p1
p1c.y = y_p1
p2c.x = x_p2
p2c.y = y_p2


#booleanos:
tiro1 = False
tiro2 = False
morreu1 = False
morreu2 = False

#programa:
pygame.init()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('atrade!')
clock = pygame.time.Clock()

#definicioes:
def respown_1():
    x_bala1 = 130
    y_bala1 = 455
    return [x_bala1, y_bala1]
def respown_2():
    x_bala2 = 690
    y_bala2 = 453
    return [x_bala2, y_bala2]
def recomeco():
    global p1, p2
    p1 = defende_1
    p2 = defende_2

fonte = pygame.font.SysFont('arial', 40, True, True)
fontet = pygame.font.SysFont('arial', 60, True, True)

while True:
    clock.tick(230)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:

            #p1 teclas
            if event.key == K_a:
                p1 = tiro_1
                if qtiros_1 >= 1:
                    tiro1 = True
                    qtiros_1 -= 1
            if event.key == K_s:
                p1 = defende_1
            if event.key == K_d and qtiros_1 < 1:
                p1 = carrega_1
                qtiros_1 += 1

            #p2 teclas
            if event.key == K_RIGHT and qtiros_2 < 1:
                p2 = carrega_2
                qtiros_2 += 1
            if event.key == K_DOWN:
                p2 = defende_2
            if event.key == K_LEFT:
                p2 = tiro_2
                if qtiros_2 >= 1:
                    tiro2 = True
                    qtiros_2 -= 1

    #colosoes da bala
    if tiro1 == True:
        x_bala1 += 3
    if tiro2 == True:
        x_bala2 -= 3
    balac_1.x = x_bala1
    balac_1.y = y_bala1
    balac_2.x = x_bala2
    balac_2.y = y_bala2
    if balac_1.colliderect(balac_2):
        x_bala1 = respown_1()[0]
        y_bala1 = respown_1()[1]
        x_bala2 = respown_2()[0]
        y_bala2 = respown_2()[1]
        tiro2 = False
        tiro1 = False
    if balac_1.colliderect(p2c):
        x_bala1 = respown_1()[0]
        y_bala1 = respown_1()[1]
        tiro1 = False
    if balac_2.colliderect(p1c) :
        x_bala2 = respown_2()[0]
        y_bala2 = respown_2()[1]
        tiro2 = False

    #mensagens
    pontos1 = fonte.render(f'munição: {qtiros_1}', True, (255, 255, 255))
    pontos2 = fonte.render(f'munição: {qtiros_2}', True, (255, 255, 255))

    #colisao do personagem:
    if balac_1.colliderect(p2c) and p2 == carrega_2 or balac_1.colliderect(p2c) and p2 == tiro_2:
        morreu1 = True
        while morreu1:
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
                        morreu1 = False
                    if event.key == K_s:
                        pygame.quit()
                        exit()

            tela.blit(fontet.render('Frank venceu!', True, (0, 0, 0)), (230, 90))
            tela.blit(fonte.render('precione r para tentar denovo', True, (0, 0, 0)), (165, 265))
            tela.blit(fonte.render('ou s para arregar', True, (0, 0, 0)), (261, 302))

            pygame.display.update()

    if balac_2.colliderect(p1c) and p1 == carrega_1 or balac_2.colliderect(p1c) and p1 == tiro_1:
        morreu2 = True
        while morreu2:
            # deixaremos a tela branca
            tela.fill((0, 255, 0))
            for event in pygame.event.get():
                # entao ele podera sair
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        recomeco()
                        morreu2 = False
                    if event.key == K_s:
                        pygame.quit()
                        exit()

            tela.blit(fontet.render('Lucky venceu!', True, (0, 0, 0)), (230, 90))
            tela.blit(fonte.render('precione r para tentar denovo', True, (0, 0, 0)), (165 , 265))
            tela.blit(fonte.render('ou s para arregar', True, (0, 0, 0)), (261, 302))


            pygame.display.flip()



    #o que aparecera na tela:
    tela.blit(tela, (0, 0))
    pygame.draw.rect(tela, (255, 0, 0), p2c, 4)
    pygame.draw.rect(tela, (255, 0, 0), p1c, 4)
    pygame.draw.rect(tela, (255, 0, 0), balac_1, 4)
    pygame.draw.rect(tela, (255, 0, 0), balac_2, 4)
    tela.blit(parede, (0, 0))
    tela.blit(bala_1, (x_bala1, y_bala1))
    tela.blit(bala_2, (x_bala2, y_bala2))
    tela.blit(p1, (x_p1, y_p1))
    tela.blit(p2, (x_p2, y_p2))
    tela.blit(pontos1, (10, 250))
    tela.blit(pontos2, (620, 250))
    tela.blit(fonte.render('Frank', True, (255, 0, 0)), (40, 210))
    tela.blit(fonte.render('Lucky', True, (0, 255, 0)), (650, 210))


    pygame.display.flip()
