# -*- coding: utf-8 -*-
"""
Melhore a coleção de TIRAS que determina quando alguém ganha no Velha3D.
Pode ganhar com tiras em x (horizontal) em y (vertical) ou em z (profundidade)
Veja se consegue testar também em todas as diagonais nas frentes nos lados e topos
Ainda tem as quatro diagonais que ligam os cantos do cubo
"""
from glow import *
TAM = (-1, 0, 1)
SP = 9
SZ = 3
print("oi")
# melhore o código de TIRAS para que teste mais possibilidades de ganhar
TIRAS = [[(x*SP, y*SP, z*SP) for x in TAM] for y in TAM for z in TAM]+[
    [(x*SP, y*SP, z*SP) for y in TAM] for x in TAM for z in TAM]+[
        [(x*SP, y*SP, z*SP) for z in TAM] for x in TAM for y in TAM]

pecas = [box, sphere] * 14
cores = [color.red, color.blue] * 14


class Casa:
    CASAS = {}  # esta coleção serve para achar o objeto casa a partir de sua posicão

    def __init__(self, x, y, z):
        self.pos = (x*SP, y*SP, z*SP)
        self.e_casa = box(pos=self.pos, size=(SZ, SZ, SZ), opacity=0.2)
        Casa.CASAS[self.pos] = self  # adiciona esta casa na coleção de casas
        self.peca = None

    def recebe(self, algo3d):
        self.peca = algo3d
        vencedores = self.testa_ganhou()
        if vencedores:
            print("ganhou")
            self.pinta_vencedores(vencedores)
        return algo3d

    def tipo_peca(self):
        #print("tipo_peca", self.peca.tipo if self.peca is not None else 0)
        return self.peca.tipo if self.peca else 0

    def clicou(self):
        coluna, linha, camada = self.pos  # aposição da peça vai ser a posição da casa
        peca = Peca(pecas.pop(), coluna, linha, camada, cores.pop())  # cria uma peça aqui
        #Casa.CASAS.pop(self.pos)  # remove esta da lista de casas para não ser clicada
        self.recebe(peca)  # avisa a casa que ela esta é a peça que está nela

    def pinta_vencedores(self, vencedores):
        SP = SZ+1
        for vencedor in vencedores:
            for posicao in vencedor:
                print("box", posicao)
                box(pos=posicao, color=color.yellow,  size=(SP, SP, SP), opacity=0.3)
                # modifique para ser um box amarelo transparente do tamanho da casa

    def testa_ganhou(self):
        def casas_ganhadoras(tira):
            tipo_tira = [Casa.CASAS[casa].tipo_peca() for casa in tira if isinstance(casa, tuple)]
            return tipo_tira == [1, 1, 1] or tipo_tira == [2, 2, 2]
        tiras = [tira for tira in TIRAS if casas_ganhadoras(tira)]  # crie aqui um teste para saber se alguem venceu
        #print("testa_ganhou", tiras,  casas_ganhadoras(tiras))
        return tiras


class Peca:
    def __init__(self, tipo_peca, x, y, z, cor):
        self.e_peca = tipo_peca(pos=(x, y, z), color=cor,  size=(SZ, SZ, SZ), opacity=0.6)
        self.tipo = 1 if tipo_peca == box else 2


def main():

    def clicou(event):
        cc = cena.mouse.pick().pos  # pega a posição do objeto clicado pelo mouse
        casa_clicada = (cc.x, cc.y, cc.z)  # cria uma tripla ordenada no espaço
        if casa_clicada in Casa.CASAS.keys():  # procura a tripla na coleção de casas
            casa_clicada = Casa.CASAS[casa_clicada]
            if casa_clicada in TABULEIRO:
                TABULEIRO.remove(casa_clicada)
                casa_clicada.clicou()  # chama o clicou da casa escolhida
    _gs = glow('main')
    cena = canvas()
    cena.width = 400
    cena.height = 400
    cena.bind("mousedown", clicou)

    TABULEIRO = [Casa(coluna, linha, camada)
                 for coluna in TAM for linha in TAM for camada in TAM]
    return TABULEIRO

if __name__ == "__main__":
    main()
