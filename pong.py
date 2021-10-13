import sys, pygame
from pygame.locals import *
from sys import exit
import random

pygame.init() # Iniciando todas as bibliotecas e funcoes da biblioteca PyGame

largura_do_mapa = 500     
altura_do_mapa = 500
geografia = largura_do_mapa, altura_do_mapa
mapa = pygame.display.set_mode(geografia)       # Criando o mapa

relogio = pygame.time.Clock() # Criando um objecto que ira controlar o fps (quadros por segundo)

pontos = 0  # Pontuacao que ira aparecer na tela

x_bolinha = 400  # Onde a bolinha ira nascer
y_bolinha = 250

direcaox = -2   # Direcao da bolinha 
direcaoy = random.choice([1, -2, 3, -1, 2, -3]) # Qual direcao a bolinha ira tomar

x =  10 # Possicao do jogador
y = altura_do_mapa // 2 # Possicao do jogador

fonte = pygame.font.SysFont("arial", 20, True, False)  # Criando a fonte do texto que ira contar a pontuacao

pygame.display.set_caption("Jogo da Cobrinha")  # Titulo do jogo

while True: # Todo jogo acontece em um loop infinito. 
    mapa.fill((0, 0, 0))

    mensagem = f'Pontos: {pontos}'  # Mensagem de texto de pontuacao
    
    texto = fonte.render(mensagem, True, (255, 255, 255))

    relogio.tick(100) # A quantidade de quadros por segundo (quanto maior mais rapido) [linha12]
    
    for event in pygame.event.get(): # Acada interacao do loop principal ele ira checar se algum evento ocorreu.O loop que controla
        if event.type == QUIT: # Sair do jogo se voce apertar quit.
            pygame.quit()  # Fecha o jogo
            exit()
        """
        if event.type == KEYDOWN:
            if event.key == K_a:
                x -= 10
            if event.key == K_d:     Esse codigo serve para dar uma passo de cada vez
                x += 10
            if event.key == K_w:
                y -= 10
            if event.key == K_s:
                y += 10
        """

    if pygame.key.get_pressed()[K_s]:  # Mover o jogador para baixo
        y += 10
    if pygame.key.get_pressed()[K_w]:  # Mover o jogador para cima
        y -= 10

    
    
    pygame.draw.rect(mapa, (255, 0, 0), (x, y, 10, 100)) # Criand um quadrado(jogador) Prametros: Local, (cor), (cordenada, cordenada, largura, altura)
    pygame.draw.rect(mapa, (0, 255, 0), (x_bolinha , y_bolinha, 10, 10))
    pygame.draw.line(mapa, (255, 255, 255), (0, 0), (0, 500), 5) # Criando uma linha
    pygame.draw.line(mapa, (255, 255, 255), (499, 500), (499, 0), 5) # Criando outra linha
    
    if y >= 400: # O jogador nao ira passar do chao
        y = 399 
    if y <= 0:   # O jogador nao ira passar do teto
        y = 1

    x_bolinha += direcaox # A direcao da bolina
    y_bolinha += direcaoy

    if y_bolinha > altura_do_mapa or y_bolinha < 0:  # A bolinha ira bater no teto ou no chao 
        direcaoy *= -1

    if y - 10 <= y_bolinha <= y + 90 :
        if 1 <= x_bolinha <= 10: #A bolinha ira bater e voltar se o jogador defender               
            direcaox *= -1
    
    if x_bolinha >= 500:        # A boliha bate na parede
        direcaox *= -1

    if x_bolinha < 0:
        pontos += 1      #Se a bolinha passar do jogador ira contar um ponto e aparecer do oultro lado
        x_bolinha = 490

    
    mapa.blit(texto, (200, 50))
    pygame.display.update() # A cada loop(While) ele ira carregar uma nova imagem se nao ele vai travar.     
