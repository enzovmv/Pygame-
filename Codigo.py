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