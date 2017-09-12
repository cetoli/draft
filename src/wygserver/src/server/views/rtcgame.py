#! /usr/bin/env python
# -*- coding: UTF8 -*-
# Este arquivo é parte do programa Marayho
# Copyright 2014-2017 Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://j.mp/GNU_GPL3>`__.
#
# Marayho é um software livre; você pode redistribuí-lo e/ou
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

"""Handle http requests.

.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

"""
from browser import document, html
from random import randint
from connector import Connect


class Game:
    def __init__(self, last, nodeid):
        self.conn = Connect(last, nodeid, self.receive_rect)
        canvas = document["pydiv"]
        self.base = base = html.DIV(style={"background-color": "gray", "min-height": "400px"})
        base.onclick = self.put_rect
        canvas <= base
        base <= html.DIV(style={"background-color": "white", "min-height": "40px", "width": "40px", "float": "left"})
        base <= html.DIV(style={"background-color": "red", "min-height": "40px", "width": "40px", "float": "left"})

    def receive_rect(self, rgb):
        print("XXXXXXX>>>> remote_action(self, rgb)", ">%s<" % rgb)
        color = tuple([int(cl) for cl in rgb.split()])
        self.base <= html.DIV(style={"background-color": "rgb(%d, %d, %d)" % color,
                                     "min-height": "40px", "width": "40px", "float": "left"})

    def put_rect(self, _=0):
        rgb = (randint(50, 250), randint(50, 250), randint(50, 250))
        alphargb = " ".join([str(cl) for cl in rgb])
        print("XXXXXXX>>>> def put_rect(self, _=0)", alphargb, rgb)
        self.conn.send(alphargb)
        self.base <= html.DIV(style={"background-color": "rgb(%d, %d, %d)" % rgb,
                                     "min-height": "40px", "width": "40px", "float": "left"})


def main(last, nodeid):
    Game(last, nodeid)
