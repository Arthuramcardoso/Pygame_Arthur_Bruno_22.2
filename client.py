import pygame
import random
import time
from pygame.locals import *
from pygame import mixer
import sys
import os

pygame.init()
# ----- Gera tela principal
altura_da_tela = 500
largura_da_tela = 1000
window = pygame.display.set_mode((largura_da_tela, altura_da_tela))
pygame.display.set_caption('Jogo')

escala_botao = 100

tela_de_fundo_img = pygame.image.load('recursos/capamenu2.jpeg').convert()
tela_de_fundo_img = pygame.transform.scale(tela_de_fundo_img,(largura_da_tela, altura_da_tela))

window.blit(tela_de_fundo_img, (0, 0))

img_ver1 = pygame.image.load('Recursos/ver1.png').convert()
img_ver1 = pygame.transform.scale(img_ver1,(1.77*escala_botao, escala_botao))

img_ver2 = pygame.image.load('Recursos/ver2.png').convert()
img_ver2 = pygame.transform.scale(img_ver2, (1.77*escala_botao, escala_botao))

img_quit = pygame.image.load('Recursos/quit.png').convert()
img_quit = pygame.transform.scale(img_quit,(1.77*escala_botao, escala_botao))

img_menu = pygame.image.load('Recursos/menu.png').convert()
img_menu = pygame.transform.scale(img_menu,(1.77*escala_botao, escala_botao))

game = True

class botao:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicado = False
    def draw(self):
        mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicado == False:
                self.clicado == True
                return(1)

        window.blit(self.image, (self.rect.x, self.rect.y))


ver1 = botao(250, 200, img_ver1)
ver2 = botao(550, 200, img_ver2)
bquit = botao(400, 350, img_quit)


while game:
    ver1.draw()
    ver2.draw()
    bquit.draw()
    if ver1.draw():
        pygame.quit()
        os.system("Ver1.py")
    if ver2.draw():
        pygame.quit()
        os.system("Ver2.py")
    if bquit.draw():
        pygame.quit()
    
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    pygame.display.update()

pygame.quit()