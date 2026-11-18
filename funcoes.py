import random
import pygame
from pixel_arts import *

COLUNAS = 17
LINHAS = 15
CELULA = 32
TOPO = 50
LARGURA = COLUNAS * CELULA
ALTURA = LINHAS * CELULA + TOPO


def desenha_pixel_art(tela, desenho, x, y):
    linha = 0
    for texto in desenho:
        coluna = 0
        for letra in texto:
            if letra != ".":
                pygame.draw.rect(tela, CORES[letra], (x + coluna * 4, y + linha * 4, 4, 4))
            coluna += 1
        linha += 1

def desenha_na_casa(tela, desenho, posicao):
    desenha_pixel_art(tela, desenho, posicao[0] * CELULA, TOPO + posicao[1] * CELULA)

def desenha_tabuleiro(tela):
    pygame.draw.rect(tela, (47, 79, 62), (0, 0, LARGURA, TOPO))
    pygame.draw.rect(tela, (140, 95, 50), (0, TOPO - 5, LARGURA, 5))
    for x in range(COLUNAS):
        for y in range(LINHAS):
            if (x + y) % 2 == 0:
                cor = (236, 230, 214)
                pontinhos = piso_bege
            else:
                cor = (204, 208, 214)
                pontinhos = piso_cinza
            pygame.draw.rect(tela, cor, (x * CELULA, TOPO + y * CELULA, CELULA, CELULA))
            desenha_pixel_art(tela, pontinhos, x * CELULA, TOPO + y * CELULA)
            pygame.draw.rect(tela, (160, 158, 150), (x * CELULA, TOPO + y * CELULA, CELULA, 1))
            pygame.draw.rect(tela, (160, 158, 150), (x * CELULA, TOPO + y * CELULA, 1, CELULA))

def desenha_quadro(tela, x, y, largura, altura):
    pygame.draw.rect(tela, (140, 95, 50), (x - 6, y - 6, largura + 12, altura + 12))
    pygame.draw.rect(tela, (47, 79, 62), (x, y, largura, altura))

def desenha_cobra(tela, cobra, foto_cabeca):
    for i in range(1, len(cobra)):
        desenha_na_casa(tela, corpo, cobra[i])
    x = cobra[0][0] * CELULA - 4
    y = TOPO + cobra[0][1] * CELULA - 4
    tela.blit(foto_cabeca, (x, y))