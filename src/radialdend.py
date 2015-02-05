# -*- coding: UTF8 -*-
# Este arquivo é parte do programa Impressious
# Copyright 2014-2015 Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
#
# Impressious é um software livre; você pode redistribuí-lo e/ou
# modificá-lo dentro dos termos da Licença Pública Geral GNU como
# publicada pela Fundação do Software Livre (FSF); na versão 2 da
# Licença.
#
# Este programa é distribuído na esperança de que possa ser útil,
# mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
# a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
# Licença Pública Geral GNU para maiores detalhes.
#
# Você deve ter recebido uma cópia da Licença Pública Geral GNU
# junto com este programa, se não, veja em <http://www.gnu.org/licenses/>
"""
############################################################
Impressious - Pacote cliente
############################################################
Define a função main do módulo impressous, criando uma instância de Impressious
"""
__version__ = "0.1.0"
__author__ = 'carlo'
from math import pi, sin, cos
CF = 2 * pi
GIL = "produto operação conteúdo"
FIL = "matemática linguagem ciência"
FID = range(20)
ONT = range(5)
DIM = []
DEMO = "blue "*8 + "green "*8 + "red "*8 + "yellow "*8 + "purple "*8
DEMO = DEMO.split()


class Dendogram:
    """"Cria um dendograma radial"""
    def __init__(self, browser):
        """Inicia o dendograma"""
        self.b = browser
        self.pena = svg = browser.svg
        title = svg.text('Title',x=70,y=25,font_size=22, text_anchor="middle")
        circle = svg.circle(cx="70", cy="120", r="40", stroke="black", stroke_width="2", fill="red")

        div = browser.doc['pydiv']
        self.tela = panel = svg.svg(width=600, height=600)
        div <= panel

        panel <= title
        panel <= circle
        self.drawline(40, 50, 40, 150)
        self.drawtier()

    def drawdend(self):
        self.drawtier(100, 200, "blue green red yellow purple".split())

    def drawtier(self, l0=100, l1=200, color=DEMO):
        # l0, l1 = 100, 200
        lines = len(color)
        step = CF / lines
        for r in range(lines):
            d0, h0 = sin(r*step), cos(r*step)
            self.drawline(d0*l0, h0*l0, d0*l1, h0*l1, color[r])

    def drawline(self, x0, y0, x1, y1, color="brown"):
        line = self.pena.line(x1=x0, y1=y0, x2=x1, y2=y1,
                stroke=color, stroke_width="2")
        self.tela <= line


def main(browser):
    print('Dendogram '+__version__)
    return Dendogram(browser)
