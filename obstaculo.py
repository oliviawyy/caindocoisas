import random
import pygame as py

class Obstaculo:

    def __init__(self, end_imagem, largura, altura):
        #guardando a largura e altura do obstaculo
        self.largura = largura
        self.altura = altura

        #carregando e alterando o tamanho da imagem
        self.imagem = py.image.load(end_imagem)
        self.imagem = py.transform.scale(self.imagem,(self.largura,self.altura))
        self.mascara = py.mask.from_surface(self.imagem)

        #guardando a posição inicial e final
        self.faixas = [620,220,310,410,520,700,800,900,1020,1280,100,120,720,666]
        self.x_inicial = 0
        self.y_inicial = 0
        self.posicao_x = self.y_inicial
        self.posicao_y = random.choice(self.faixas)
        self.pontos = 0

    #controlando a velocidade do obstaculo
        self.velocidade = random.randint(2,5)


    def movimentar(self):
        self.posicao_y += self.velocidade
        if self.posicao_y > 780 - self.largura:
            self.posicao_y = self.y_inicial
            self.velociade = random.randint(2,5)
            self.posicao_x = random.choice(self.faixas)
