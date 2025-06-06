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
# Move 'bem_caindo' down

lista_obstaculo = [Obstaculo("imagem/mal.png",200, 200),
                  Obstaculo("imagem/mal2.png", 200, 200),
                  Obstaculo("imagem/mal3.png", 200, 200)]

lista_bem = [Obstaculo("imagem/bem.png", 200, 200),
             Obstaculo("imagem/bem.png", 200, 200),
             Obstaculo("imagem/bem.png", 200, 200)]

#CRIANDO A FONTE DO PLACAR
placar = py.font.SysFont("Goudy Stout",13)

# loop infinito
estado = "jogando"
fimjogo = False

while not fimjogo:
    for eventos in py.event.get():    
        if eventos.type == py.QUIT:
            fimjogo = True

    tela.blit(fundo, (0, 0))  # desenha o fundo
    tela.blit(homem.imagem, (homem.posicao_x, homem.posicao_y))
        
    for obstaculo in lista_bem:
            obstaculo.movimentar()
            tela.blit(obstaculo.imagem,(obstaculo.posicao_x, obstaculo.posicao_y))
            #bem
            if homem.mascara.overlap(obstaculo.mascara,(homem.posicao_x-obstaculo.posicao_x,homem.posicao_y-obstaculo.posicao_y)):
                obstaculo.posicao_x = obstaculo.x_inicial
                obstaculo.posicao_y = obstaculo.y_inicial
                obstaculo.pontos += 10
                print(homem.pontos)

    for obstaculo in lista_obstaculo:
            obstaculo.movimentar()
            tela.blit(obstaculo.imagem,(obstaculo.posicao_x, obstaculo.posicao_y))
            #finn
            if homem.mascara.overlap(obstaculo.mascara,(homem.posicao_x-obstaculo.posicao_x,homem.posicao_y-obstaculo.posicao_y)):
                obstaculo.posicao_x = obstaculo.x_inicial
                obstaculo.posicao_y = obstaculo.y_inicial
                obstaculo.pontos -= 5
                estado = "fimjogo"
                                                                                                                                                  
            #CRIANDO O PLACAR
            placar_homem = placar.render(f"PONTOS: {homem.pontos}",True,CORES["BRANCO"],(57, 42, 173))
            tela.blit(placar_homem,(0,0))

    homem.movimentar(py.K_w,                                                                                                                                                                                                   
                        py.K_s, 
                        py.K_d, 
                        py.K_a)                                  
    if homem.posicao_y <= 10:                                   
        homem.posicao_y = homem.y_inicial

    
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

    

    py.display.update() # atualiza a teladd
    clock.tick(60)      
       














