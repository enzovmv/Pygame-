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
pygame.mixer.music.load(os.path.join(pasta, "musica.wav"))
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

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

    desenha_tabuleiro(tela)
    desenha_na_casa(tela, moeda, comida)
    if pos_chance != None:
        desenha_na_casa(tela, moeda_chance, pos_chance)
    if pos_tempo != None:
        desenha_na_casa(tela, moeda_tempo, pos_tempo)
    desenha_cobra(tela, cobra, foto_cabeca)

    escreve(tela, fonte, "Pontos: " + str(pontos), 10, 14, branco)
    escreve(tela, fonte, "Recorde: " + str(recorde), 150, 14, amarelo)
    desenha_pixel_art(tela, coracao, 318, 13)
    escreve(tela, fonte, "x" + str(chances), 352, 14, branco)
    if lento:
        segundos = int((lento_ate - agora) / 1000) + 1
        desenha_pixel_art(tela, moeda_tempo, 420, 9)
        escreve(tela, fonte, str(segundos) + "s", 458, 14, azul)

    if estado == "inicio":
        desenha_quadro(tela, 30, 110, LARGURA - 60, 330)
        escreve_no_meio(tela, fonte_grande, "PY SNAKE", 130, amarelo)
        desenha_pixel_art(tela, moeda_chance, 50, 215)
        escreve(tela, fonte, "Moeda da chance: volta 5 passos", 92, 220, branco)
        desenha_pixel_art(tela, moeda_tempo, 50, 265)
        escreve(tela, fonte, "Moeda do tempo: devagar por 10s", 92, 270, branco)
        escreve_no_meio(tela, fonte, "Quanto maior a cobra, mais rápido!", 325, azul)
        escreve_no_meio(tela, fonte, "Aperte uma seta para começar", 385, amarelo)

    if estado == "voltou":
        desenha_quadro(tela, 30, 70, LARGURA - 60, 70)
        escreve_no_meio(tela, fonte, "Voltou no tempo!", 80, amarelo)
        escreve_no_meio(tela, fonte, "Aperte uma seta para continuar", 108, branco)

    if estado == "fim":
        desenha_quadro(tela, 30, 170, LARGURA - 60, 200)
        escreve_no_meio(tela, fonte_grande, "FIM DE JOGO", 190, branco)
        escreve_no_meio(tela, fonte, "Pontos: " + str(pontos), 265, branco)
        escreve_no_meio(tela, fonte, "Recorde: " + str(recorde), 295, amarelo)
        escreve_no_meio(tela, fonte, "Enter para jogar de novo", 335, branco)

    pygame.display.flip()

    if estado == "jogando":
        relogio.tick(calcula_velocidade(cobra, lento))
    else:
        relogio.tick(30)

pygame.quit()