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
