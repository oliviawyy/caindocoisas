import os
import sys

#caminho base do script ou do executável
def caminho_relativo(caminho):
    try:
        #quando empacotado com PyIntaller
        base = sys._MEIPASS
    except AttributeError:
        #Quando rodando como script .py
        base = os.path.abspath(".")

    return os.path.join(base, caminho)