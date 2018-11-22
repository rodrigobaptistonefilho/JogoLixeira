import pygame
from objeto import Lixeira, Bolinha
from random import randrange

#Definindo cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

#criação da tela
pygame.init()

LARGURA = 600
ALTURA = 400
pontos = 0
fonte = pygame.font.SysFont("comicsansms", 30)#determina a fonte do jogo
tela = pygame.display.set_mode([LARGURA, ALTURA])#controei a tela de acorda com a LARGURA e ALTURA declarada
pygame.display.set_caption("Lixeira")#Nome do projeto
mouse = pygame.mouse# encurta o nome
mouse.set_visible(False)# esconde o ponteiro
clock = pygame.time.Clock()#usado para atualizar o tempo da pagina do jogo

todosObjetos = pygame.sprite.Group()
lixeira = Lixeira(50, 50)
todosObjetos.add(lixeira)


def things(thingx, thingy, thingw, thingh, color):#funcao usada para objetos cairem na tela
    return pygame.draw.rect(tela, color, [thingx, thingy, thingw, thingh])

thing_startx = randrange(0, LARGURA)#largura em que objeto vai nascer
thing_starty = ALTURA #a partir de qual altura vai cair
thing_speed = 7 #velocidade
thing_width = 40 #tamanho do objeto
thing_height = 20 #tamanho do objeto
while True:
    filaEventos = pygame.event.get()

    preto = things(thing_startx, thing_starty, thing_width, thing_height, PRETO)
    # percorre a fila de eventos
    for evento in filaEventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if evento.type == pygame.MOUSEMOTION:
            pos = mouse.get_pos()
            if pos[0] <= 524 and pos[1] <= 315:
                lixeira.mover(pos[0], pos[1])
                pontos += lixeira.colide(preto)

    tela.fill(BRANCO)
    preto = things(thing_startx, thing_starty, thing_width, thing_height, PRETO)
    thing_starty += thing_speed

    if thing_starty > ALTURA:
        thing_starty = 0 - thing_height
        thing_startx = randrange(0, LARGURA)

    todosObjetos.draw(tela)
    tela.blit(fonte.render("Pontos: " + str(pontos), True, (PRETO)), (0, 0))
    pygame.display.update()#Usado para atualizar o jogo
    clock.tick(60)
