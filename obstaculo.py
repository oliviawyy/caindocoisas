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
        self.faixas = [740,220,310,410,520,700]
        self.y_inicial = 0
        self.posicao_x = self.y_inicial
        self.posicao_y = random.choice(self.faixas)

    #controlando a velocidade do obstaculo
        self.velocidade = random.randint(5,10)


    def movimentar(self):
        self.posicao_y += self.velocidade
        if self.posicao_y > 700 - self.largura:
            self.posicao_y = self.y_inicial
            self.velociade = random.randint(5,10)
            self.posicao_x = random.choice(self.faixas)
