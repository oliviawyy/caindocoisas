from jogador import Jogador
from obstaculo import Obstaculo
import pygame as py

print(""" 
                                    _               
 _ __   ___  __ _  __ _    ___ ___ (_)___  __ _ ___ 
| '_ \ / _ \/ _` |/ _` |  / __/ _ \| / __|/ _` / __|
| |_) |  __/ (_| | (_| | | (_| (_) | \__ \ (_| \__ \
| .__/ \___|\__, |\__,_|  \___\___/|_|___/\__,_|___/
|_|         |___/                                   

      

""")

py.init()
clock = py.time.Clock()


CORES = {"BRANCO":(255,255,255),
         "AMARELO":(255,255,0),
         "ROSA": (255,200,255),
         "CINZA":(100,100,100)}

# criar tela
tela = py.display.set_mode((1280,780))

# carregar fundo
fundo = py.image.load("imagem/fundo-fantasma.png")
fundo = py.transform.scale(fundo, (1280,780))
# Criar personagem

bem = Jogador("imagem/bem.png", 200, 200, 530, 100)
bem = Jogador("imagem/bem.png", 200, 200, 200, 120)
mal = Obstaculo("imagem/mal.png", 200, 200)

#homem = Jogador("imagem/homem.png", 100, 100, 420, 614)
homem = Jogador("imagem/homem.png",300, 300, 100, 500)

#homem = py.transform.scale(homem, (300, 300))
#x_inicial = 100
#y_inicial = 500
# Move 'bem_caindo' down

lista_obstaculo = [Obstaculo("imagem/mal.png",200, 200),
                  Obstaculo("imagem/mal.png", 200, 200),
                  Obstaculo("imagem/mal.png", 200, 200)]

lista_bem = [Obstaculo("imagem/bem.png", 200, 200),
             Obstaculo("imagem/bem2.png", 200, 200),
             Obstaculo("imagem/bem3.png", 200, 200)]

# loop infinito
estado = "jogando"
fimjogo = False

while not fimjogo:
    for eventos in py.event.get():    
        if eventos.type == py.QUIT:
            fimjogo = True

    for obstaculo in lista_obstaculo:
        homem.movimentar(py.K_w, 
                         py.K_s, 
                         py.K_d, 
                         py.K_a)
        if homem.posicao_y <= 10:
            homem.posicao_y = homem.y_inicial


        tela.blit(fundo, (0, 0))  # desenha o fundo
        tela.blit(homem.imagem, (homem.posicao_x, homem.posicao_y))
        #mal
        tela.blit(lista_obstaculo[0].imagem, (lista_obstaculo[0].posicao_x, lista_obstaculo[0].posicao_y))
        tela.blit(lista_obstaculo[0].imagem, (lista_obstaculo[0].posicao_x, lista_obstaculo[0].posicao_y))
        tela.blit(lista_obstaculo[0].imagem, (lista_obstaculo[0].posicao_x, lista_obstaculo[0].posicao_y))

        #bem
        tela.blit(lista_bem[0].imagem, (lista_bem[0].posicao_x, lista_bem[0].posicao_y))
        tela.blit(lista_bem[0].imagem, (lista_bem[0].posicao_x, lista_bem[0].posicao_y))
        tela.blit(lista_bem[0].imagem, (lista_bem[0].posicao_x, lista_bem[0].posicao_y))
        tela.blit(lista_bem[0].imagem, (lista_bem[0].posicao_x, lista_bem[0].posicao_y))
        tela.blit(lista_bem[0].imagem, (lista_bem[0].posicao_x, lista_bem[0].posicao_y))

        py.display.update()       # atualiza a tela
        lista_obstaculo[0].movimentar()
        lista_bem[0].movimentar()

#x inicial y inicial (homem.posicao_x, homem.posicao_y))
#(homem.x_inicial, homem.y_inicial))


#colisão da tela

        #PARAR NAS BARREIRAS
        if homem.posicao_x <= -60:
            homem.posicao_x = -60
        
        if homem.posicao_y <= 0:
           homem.posicao_y = 0

        if homem.posicao_x >= 1090:
            homem.posicao_x = 1090

        if homem.posicao_y >= 700:
           homem.posicao_y = 700


















