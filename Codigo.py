import pygame
import random
import os
from funcoes import *

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Py Snake")
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont("consolas", 22, bold=True)
fonte_grande = pygame.font.SysFont("consolas", 50, bold=True)

pasta = os.path.dirname(os.path.abspath(__file__))
foto_cabeca = pygame.image.load(os.path.join(pasta, "cabeca.png"))

branco = (255, 255, 255)
amarelo = (255, 220, 80)
azul = (150, 210, 255)

recorde = 0
rodando = True
reiniciar = True

while rodando:
    if reiniciar:
        cobra = [[5, 7], [4, 7], [3, 7]]
        direcao = "direita"
        nova_direcao = "direita"
        comida = [12, 7]
        pos_chance = None
        some_chance = 0
        pos_tempo = None
        some_tempo = 0
        chances = 0
        lento_ate = 0
        historico = []
        pontos = 0
        estado = "inicio"
        reiniciar = False

    agora = pygame.time.get_ticks()
    lento = agora < lento_ate

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            tecla = ""
            if evento.key == pygame.K_UP:
                tecla = "cima"
            elif evento.key == pygame.K_DOWN:
                tecla = "baixo"
            elif evento.key == pygame.K_LEFT:
                tecla = "esquerda"
            elif evento.key == pygame.K_RIGHT:
                tecla = "direita"

            if estado == "fim":
                if evento.key == pygame.K_RETURN:
                    reiniciar = True
            elif tecla != "":
                if tecla != direcao_contraria(direcao):
                    nova_direcao = tecla
                estado = "jogando"
    
    if estado == "jogando":
            historico.append([copia_cobra(cobra), direcao, comida, pontos])
            if len(historico) > 6:
                del historico[0]
    
            direcao = nova_direcao
            cabeca = anda(cobra, direcao)

            if bateu(cabeca, cobra):
               if chances > 0:
                 chances = chances - 1
                 cobra = historico[0][0]
                 direcao = historico[0][1]
                 nova_direcao = direcao
                 comida = historico[0][2]
                 pontos = historico[0][3]
                 historico = []
                 estado = "voltou"
               else:
                 estado = "fim"
            else:
                 cobra = [cabeca] + cobra
                 if cabeca == comida:
                     pontos = pontos + 1
                     recorde = max(recorde, pontos)
                     comida = sorteia_posicao(cobra + [pos_chance, pos_tempo])
                 else:
                     del cobra[-1]
                 if cabeca == pos_chance:
                     if chances < 3:
                      chances = chances + 1
                     pos_chance = None

                 if cabeca == pos_tempo:
                     lento_ate = agora + 10000
                     pos_tempo = None

                 if pos_chance == None and pontos >= 3 and random.randint(1, 100) <= 2:
                     pos_chance = sorteia_posicao(cobra + [comida, pos_tempo])
                     some_chance = agora + 8000

                 if pos_tempo == None and pontos >= 3 and random.randint(1, 100) <= 2:
                     pos_tempo = sorteia_posicao(cobra + [comida, pos_chance])
                     some_tempo = agora + 8000

                 if pos_chance != None and agora > some_chance:
                     pos_chance = None

                 if pos_tempo != None and agora > some_tempo:
                     pos_tempo = None

 