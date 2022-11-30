# ===== Inicialização =====
# ----- Importa e inicia pacotes
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


# ----- Musica
mixer.init()
mixer.music.load('Recursos/zap zap.ogg')


# ----- funções utilizadas no jogo

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

def cria_camadas(n_camada_final):
    camadas = []
    for i in range(1, n_camada_final*5, 5):
        camadas.append(-i*55)
    return camadas

def cria_obstaculos(n_buracos, camada):
    lista_obstaculo_criado = []
    lista_indices = [0,1,2,3,4]
    for buraco in range(n_buracos):
        indice_sorteado = random.choice(lista_indices)
        lista_indices.remove(indice_sorteado)
    for obstaculo in lista_indices:
        imagem_sorteada = random.choice(lista_das_imagens)
        posição = lista_posições[obstaculo]

        oobstaculo = Obstaculo(imagem_sorteada, posição, camada)
        lista_obstaculo_criado.append(oobstaculo)

    return lista_obstaculo_criado

def cria_todos_obstaculos(camadas):
    lista = []
    numeros_de_buracos = [1,2,3,4]
    for i in camadas:
        lista.append(cria_obstaculos(random.choice(numeros_de_buracos), i))
    return lista

def cria_speed(n_buracos, camada):
    lista_obstaculo_criado = []
    lista_indices = [0,1,2,3,4]
    for buraco in range(n_buracos):
        indice_sorteado = random.choice(lista_indices)
        lista_indices.remove(indice_sorteado)
    for obstaculo in lista_indices:
        imagem_sorteada = speed_pot
        posição = lista_posições[obstaculo]

        oobstaculo = speed(posição, camada)
        lista_obstaculo_criado.append(oobstaculo)
    

    return lista_obstaculo_criado

def cria_todos_speed(camadas):
    lista = []
    numeros_de_buracos = [1,2,3,4,5]
    for i in camadas:
        lista.append(cria_speed(random.choice(numeros_de_buracos), i))
    return lista






# ----- definição tamanhos e propriedades das estruturas

largura_do_personagem = 180
altura_do_personagem = 120

altura_inicial_dos_obstaculos = 120
largura_inicial_dos_obstaculos = 180

velocidade_x_dos_obstaculos = 0
velocidade_y_dos_obstaculos = 0

pontos = 0

escala_botao = 100

img_quit = pygame.image.load('Recursos/quit.png').convert()
img_quit = pygame.transform.scale(img_quit,(1.77*escala_botao, escala_botao))

img_menu = pygame.image.load('Recursos/menu.png').convert()
img_menu = pygame.transform.scale(img_menu,(1.77*escala_botao, escala_botao))

tela_de_fundo_img = pygame.image.load('recursos/fundo.png').convert()
tela_de_fundo_img = pygame.transform.scale(tela_de_fundo_img,(largura_da_tela, altura_da_tela))

personagem_img = pygame.image.load('recursos/imagem_do_personagem.png').convert_alpha()
personagem_img = pygame.transform.scale(personagem_img,(largura_do_personagem, altura_do_personagem))

carro_da_fgv_img = pygame.image.load('recursos/imagem_do_carro_da_fgv.png').convert_alpha()
carro_da_fgv_img = pygame.transform.scale(carro_da_fgv_img, (largura_inicial_dos_obstaculos, altura_inicial_dos_obstaculos))

carro_do_marcao_img = pygame.image.load('recursos/imagem_do_carro_do_marcão.png').convert_alpha()
carro_do_marcao_img = pygame.transform.scale(carro_do_marcao_img,(largura_inicial_dos_obstaculos, altura_inicial_dos_obstaculos))

carro_da_espm_img = pygame.image.load('recursos/imagem_do_carro_da_espm.png').convert_alpha()
carro_da_espm_img = pygame.transform.scale(carro_da_espm_img,(largura_inicial_dos_obstaculos, altura_inicial_dos_obstaculos))

carro_da_puc_img = pygame.image.load('recursos/imagem_do_carro_da_puc.png').convert_alpha()
carro_da_puc_img = pygame.transform.scale(carro_da_puc_img, (largura_inicial_dos_obstaculos, altura_inicial_dos_obstaculos))

carro_do_mackenzie_img = pygame.image.load('recursos/imagem_do_carro_do_mackenzie.png').convert_alpha()
carro_do_mackenzie_img = pygame.transform.scale(carro_do_mackenzie_img, (largura_inicial_dos_obstaculos, altura_inicial_dos_obstaculos))

tela_de_fundo_menu_img = pygame.image.load('Recursos/capamenu1.jpeg').convert()
tela_de_fundo_menu_img = pygame.transform.scale(tela_de_fundo_menu_img,(largura_da_tela, altura_da_tela))

ganhou_img = pygame.image.load('Recursos/imagem_ganhou.jpeg').convert()
ganhou_img = pygame.transform.scale(ganhou_img,(largura_da_tela, altura_da_tela))

perdeu_img = pygame.image.load('Recursos/imagem_perdeu.jpeg').convert()
perdeu_img = pygame.transform.scale(perdeu_img,(largura_da_tela, altura_da_tela))

speed_pot = pygame.image.load('Recursos/velocidade.png').convert_alpha()
speed_pot = pygame.transform.scale(speed_pot,(2*80, 80))

heart = pygame.image.load('Recursos/life.png').convert_alpha()
heart = pygame.transform.scale(heart,(160, 160))

r1 = pygame.image.load('Recursos/Fox1.png').convert_alpha()
r1 = pygame.transform.scale(r1,(160, 160))

r2 = pygame.image.load('Recursos/Fox2.png').convert_alpha()
r2 = pygame.transform.scale(r2,(160, 160))

r1Esquerda = pygame.image.load('Recursos/Fox1Esquerda.png').convert_alpha()
r1Esquerda = pygame.transform.scale(r1Esquerda,(160, 160))

r2Esquerda = pygame.image.load('Recursos/Fox2Esquerda.png').convert_alpha()
r2Esquerda = pygame.transform.scale(r2Esquerda,(160, 160))


lista_das_imagens = [carro_da_fgv_img, carro_do_marcao_img, carro_da_espm_img, carro_da_puc_img, carro_do_mackenzie_img]

# ----- Posições e velocidades iniciais
muito_esquerda = [0, -altura_inicial_dos_obstaculos, velocidade_x_dos_obstaculos, velocidade_y_dos_obstaculos]
esquerda = [200, -altura_inicial_dos_obstaculos, velocidade_x_dos_obstaculos, velocidade_y_dos_obstaculos]
meio = [400, -altura_inicial_dos_obstaculos, velocidade_x_dos_obstaculos, velocidade_y_dos_obstaculos]
direita = [600, -altura_inicial_dos_obstaculos, velocidade_x_dos_obstaculos, velocidade_y_dos_obstaculos]
muito_direita = [800, -altura_inicial_dos_obstaculos, velocidade_x_dos_obstaculos, velocidade_y_dos_obstaculos]

lista_posições = [muito_esquerda, esquerda, meio, direita, muito_direita]

camadas = cria_camadas(60)

menu = botao(300, 250, img_menu)
bquit = botao(500, 250, img_quit)

# ----- Inicia estruturas de dados
# definindo os novos tipos de estruturas

power = 1
extra_life = 0
now = 0

aumento_da_velocidade = 10


class speed(pygame.sprite.Sprite):
    def __init__(self, posição, camada):
        pygame.sprite.Sprite.__init__(self)

        #self.velocidade = aumento_da_velocidade
        self.image = speed_pot
        self.rect = self.image.get_rect()
        self.posição = posição
        self.rect.x = posição[0]
        self.rect.y = camada
        self.speedx = posição[2]
        self.speedy = posição[3]

    def update (self):
        #atualizando posição do obstaculo
        self.rect.x += self.speedx
        acelaracao = int(self.speedy*((tempo_passado))*0.15)
        self.rect.y += velocidade_y_dos_obstaculos + acelaracao

        #reiniciando posição
        if self.rect.top > 400:
            pot_speed.remove(self)
            sprites.remove(self)
        if self.rect.x < 400:
            pot_speed.remove(self)
            sprites.remove(self)


class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, img, posição, camada):
        pygame.sprite.Sprite.__init__(self)

        #self.velocidade = aumento_da_velocidade
        self.image = img
        self.rect = self.image.get_rect()
        self.posição = posição
        self.rect.x = posição[0]
        self.rect.y = camada
        self.speedx = posição[2]
        self.speedy = posição[3]
        self.ta = random.choice([0,1,2,3])

    def update (self):
        #atualizando posição do obstaculo
        self.rect.x += self.speedx
        acelaracao = int(self.speedy*((tempo_passado))*0.15)
        self.rect.y += velocidade_y_dos_obstaculos + acelaracao

        #reiniciando posição
        if self.rect.top > 400:
            todosobstaculos.remove(self)
            sprites.remove(self)


class Personagem(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.xlist = [0,200,400,600,800]
        self.indice = 2
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = self.xlist[self.indice]
        self.rect.y = altura_da_tela - altura_do_personagem
        self.speedx = 0
        self.speedy = 0

    def update (self):
        #self.rect.x = self.xlist[self.indice]
        self.rect.x +=self.speedx
        self.rect.y +=self.speedy

        if self.speedx != 0 and self.rect.x in self.xlist:
            self.speedx = 0

#escreve pontuação na tela
font = pygame.font.SysFont(None, 48)
#text = font.render('{}'.format(pontos), True, (0, 0, 0))

#inicia
game = True


# ----- Ajuste de velocidade

tempo_inicial = time.time()

clock = pygame.time.Clock()
FPS = 60


# ----- Criando obstaculos
todosobstaculos = pygame.sprite.Group()
sprites = pygame.sprite.Group()
pot_speed = pygame.sprite.Group()

personagem = Personagem(personagem_img)
sprites.add(personagem)

lista_lista_obstaculos = cria_todos_obstaculos(camadas)
lista_speed = cria_todos_speed(camadas)

for lista in lista_speed:
    for obstaculo in lista:
        pot_speed.add(obstaculo)
        sprites.add(obstaculo)

for lista in lista_lista_obstaculos:
    for obstaculo in lista:
        todosobstaculos.add(obstaculo)
        sprites.add(obstaculo)





estado = 'inicio'

# ===== Loop principal =====
while game:
    clock.tick(FPS)
    tempo_final = time.time()
    tempo_passado = tempo_final - tempo_inicial
    pontos = tempo_final - tempo_inicial

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False


        if estado == 'inicio':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    estado = 'jogo'
                    velocidade_y_dos_obstaculos = 2
                    tempo_inicial = time.time()
                    #arrumar musica
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and personagem.speedx < 40 and estado == 'jogo':
                if personagem.indice == -1:
                    personagem.indice = -1
                else:
                    personagem.indice -= 1
                    personagem.speedx = -20
                    esquerda = True
                

            if event.key == pygame.K_RIGHT and personagem.speedx < 40 and estado == 'jogo':
                if personagem.indice == 4:
                    personagem.indice = 4
                else:
                    personagem.indice += 1
                    personagem.speedx = 20
                    esquerda = False
            
            if event.key == pygame.K_UP and estado == 'jogo':
                if power == 1:
                    extra_life=1
                    power = 0
       
            
    if pontos >= 61:
        estado = 'ganhou'
    # ----- Atualiza estado do jogo
    sprites.update()

    collect = pygame.sprite.spritecollide(personagem, pot_speed, True)
    if len(collect) > 0:
        velocidade_y_dos_obstaculos = 1
        now = tempo_final
    
    if tempo_final > now+2:
        velocidade_y_dos_obstaculos = 2

    

    # ----- Verifica Colisão
    hits = pygame.sprite.spritecollide(personagem, todosobstaculos, True)
    if len(hits) > 0:
        if extra_life :
            extra_life = 0
        else:
            estado = 'perdeu'
    

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    if estado == 'inicio':
        window.blit(tela_de_fundo_menu_img , (0,0))

    elif estado == 'jogo':
        window.blit(tela_de_fundo_img,(0,0))
        text = font.render('{0:.0f}'.format(pontos), True, (0, 0, 0))
        window.blit(text, (490, 0))
        sprites.draw(window)
        

    elif estado == 'ganhou':
        window.blit(ganhou_img, (0,0))

    elif estado == 'perdeu':
        window.blit(perdeu_img, (0,0))
        menu.draw
        bquit.draw()
        if menu.draw():
            pygame.quit()
            os.system("client.py")
        if bquit.draw():
            pygame.quit()

        #arrumar musica

    if estado == 'jogo':
        if (esquerda == False):
            if str(int(tempo_final))[-1] == "1" or str(int(tempo_final))[-1] == "3" or str(int(tempo_final))[-1] == "5" or str(int(tempo_final))[-1] == "7" or str(int(tempo_final))[-1] == "9":
                window.blit(r2, (personagem.rect.x, personagem.rect.y))
            if str(int(tempo_final))[-1] == "2" or str(int(tempo_final))[-1] == "4" or str(int(tempo_final))[-1] == "6" or str(int(tempo_final))[-1] == "8" or str(int(tempo_final))[-1] == "0":
                window.blit(r1, (personagem.rect.x, personagem.rect.y))
        else:
            if str(int(tempo_final))[-1] == "1" or str(int(tempo_final))[-1] == "3" or str(int(tempo_final))[-1] == "5" or str(int(tempo_final))[-1] == "7" or str(int(tempo_final))[-1] == "9":
                window.blit(r2Esquerda, (personagem.rect.x, personagem.rect.y))
            if str(int(tempo_final))[-1] == "2" or str(int(tempo_final))[-1] == "4" or str(int(tempo_final))[-1] == "6" or str(int(tempo_final))[-1] == "8" or str(int(tempo_final))[-1] == "0":
                window.blit(r1Esquerda, (personagem.rect.x, personagem.rect.y))


                    
                
                
                
            

              

    # ----- Atualiza estado do jogo
    if extra_life == 1:
        window.blit(heart, (0, 0))

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados