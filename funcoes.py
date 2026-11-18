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
