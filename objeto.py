import pygame
import random

image = pygame.image.load('bolinhapapel.png')
image = pygame.image.load('Lixeira.png')

LARGURA = 600 #tamanho da largura da tela
ALTURA = 400  #tamanho da altura da tela

class Bolinha(pygame.sprite.Sprite):#cria o objeto bolinha
    def __init__(self, x, y):#construtor do objeto
        super().__init__()# chamando construtur da super classe mãe
        #self.image = pygame.image.load('bolinhapapel.png').convert_alpha()# objeto com imagem
        #self.rect = self.image.get_rect()#armazena o retângulo da imagem em rect
        self.rect.x = x #posiciona a imagem nas coordenadas passadas como parâmetro
        self.rect.y = y


class Lixeira(pygame.sprite.Sprite):#cria o objeto lixeira
    def __init__(self, x, y ):
        super().__init__()
        self.image = pygame.image.load('Lixeira.png').convert_alpha()#objeto com imagem
        self.rect = self.image.get_rect()#armazena o retângulo da imagem em rect
        self.rect.x = x #posiciona a imagem nas coordenadas passadas como parâmetro
        self.rect.y = y

    #método para movimentar o bloco
    def mover(self, x, y):
        self.rect.x = x #posiciona a imagem nas coordenadas passadas como parametro
        self.rect.y = y

    #método colidir bloco
    def colide(self, other_sprite):
        col = self.rect.colliderect(other_sprite)#vai verificar se houve colisão entre os objetos
        if col:
            del other_sprite
            return 1 #verifica se houve colisão e se houve returna 1 se nao retorna 0
        else:
            return 0