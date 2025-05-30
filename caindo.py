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
#homem = Jogador("imagem/homem.png", 100, 100, 420, 614)
homem = Jogador("imagem/homem.png",300, 300, 100, 500)
#homem = py.transform.scale(homem, (300, 300))
#x_inicial = 100
#y_inicial = 500


lista_obstaculo = [Obstaculo("imagem/bem.png",130, 100),
                  Obstaculo("imagem/bem.png", 130, 100),
                  Obstaculo("imagem/bem.png", 140, 100)]


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
        py.display.update()       # atualiza a tela


#x inicial y inicial (homem.posicao_x, homem.posicao_y))
#(homem.x_inicial, homem.y_inicial))




















