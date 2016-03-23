__author__ = 'carlo'
from glow import *
_gs = glow('main')
cena = canvas()
cena.width = 400
cena.height = 400
TAM = (-1, 0, 1)
TABULEIRO = []
PECAS = []
print("oi")
pecas = [box, sphere] * 5
cores = [color.blue, color.red] * 5
TABULEIRO = [box(pos=(coluna*3, linha*3, 0), size=(2, 2, 2), opacity=0.2)
             for coluna in TAM for linha in TAM]
cor = color.blue
#peca, cor = pecas.pop()
PECAS = [pecas.pop()(pos=(coluna*3, linha*3, 0), color=cores.pop(),  size=(1, 1, 1), opacity=0.6)
             for coluna in TAM for linha in TAM]