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

"""Recursiv Item List.

.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

"""
from browser import document, html, window
from random import randint
from connector import Connect
from javascript import JSObject


class NoItem:
    LAST = 0
    NODEID = ""

    def __init__(self, last=None, nodeid=None, *_, **__):
        NoItem.LAST = last or NoItem.LAST
        NoItem.NODEID = nodeid or NoItem.NODEID
        self.node_id_list = 0
        self.node_id_dict = {}

    def create_id(self):
        self.node_id_list += 1
        return self.node_id_list
NOITEM = NoItem()
SIZE = (50, 50)
GRAY = (50, 50, 50)


class Item:
    conn = None
    item = {}
    prefix = "S_N_O_D_E_%03x" % randint(0x111, 0xfff) + "-%02d"

    def __init__(self, node_id, rgb, size=SIZE):
        self.container = []
        self.capacity = self.item_count = self.rows = self.cols = 1
        self.parent, self.node_id, self.rgb, self.size = self._init(node_id, rgb, size)

    def _init(self, node_id, rgb, size):
        print("XXXXXXX>>>> _init", ">%s<" % [node_id, rgb, size])
        height, width = size
        self.side = min(height, width)
        self.base = base = html.DIV(style={"background-color": "rgb(%d, %d, %d)" % rgb,
                                           "min-height": "%dpx" % height, "width": "%dpx" % width, "float": "left"})
        base.onclick = self.add_item
        parent = Item.item[tuple(node_id[:-1])]
        parent <= self
        return parent, node_id, rgb, size

    def create(self, rgb=None, node_id=None, size=SIZE):  # last=None, nodeid=None):
        nodeid = node_id if node_id else self.node_id + (len(self.container),)
        rgb = rgb or (randint(50, 250), randint(50, 250), randint(50, 250))
        # Item.conn.send(rgb=rgb, node_id=nodeid)
        item = Item(node_id=nodeid, rgb=rgb, size=size)
        # self.container.append(item)
        Item.item[nodeid] = item
        # item.send()
        return item

    def compute_grid(self):
        height, width = self.size
        while self.item_count > self.capacity:
            if height / (self.rows + 1) >= width / (self.cols + 1):
                self.rows = self.rows + 1
            else:
                self.cols = self.cols + 1
            self.capacity = self.rows * self.cols
        return height / self.rows, width / self.cols

    def resize(self, size):
        height, width = self.size = size
        self.base.stile.width = width
        self.base.stile.min_height = height
        [item.resize((height/self.rows, width/self.cols)) for item in self.container]

    def __le__(self, square):
        self.container.append(square)
        self.base <= square.base

    def add_item(self, _=0):
        self.item_count += 1
        print("XXXXXXX>>>> _add_item(data)", ">%s<" % [list(self.node_id), list(self.rgb), list(self.size)])
        self.create().send()
        # Item(self, self.compute_grid())

    def send(self):
        data = [list(self.node_id), list(self.rgb), list(self.size)]
        Item.conn.send(data)


class Base(Item):
    def __init__(self, last, node_id, rgb=GRAY):
        self.base = canvas = document["pydiv"]

        def _add_item(data):
            # print("XXXXXXX>>>> _add_item(data)", ">%s<" % data)
            _node_id, _rgb, _size = tuple(data[0]), tuple(data[1]), tuple(data[2])
            # print("XXXXXXX>>>> Item.item", ">%s<" % Item.item.keys())
            # print("XXXXXXX>>>> Item.item[key]", ">%s<" % type(_node_id), _node_id, _node_id[:-1])
            Item.item[_node_id[:-1]].create(_rgb, _node_id, _size)

        class NoItem:
            def __le__(self, square):
                canvas <= square.base

        Item.prefix = node_id
        self.no_item = NoItem()
        height,  width = window.innerHeight - 40, window.innerWidth - 100
        size = height,  width
        Item.item[()], Item.item[(0,)] = self.no_item, self
        Item.__init__(self, (0,), rgb, size)
        Item.conn = Connect(last, node_id, _add_item)
        self.base.style.left = 40
        self.base.style.top = 10
        self.base.style.position = "absolute"


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
        print("XXXXXXX>>>> remote_action(self, rgb)", "rgb[0]>%s<" % rgb[0])
        print("XXXXXXX>>>> remote_action(self, rgb)", ">rgb(%d, %d, %d)<" % tuple(rgb[1]))
        print("XXXXXXX>>>> remote_action(self, rgb)", "type>%s<" % dict(JSObject(rgb[0])))
        color = tuple(rgb[1])
        # color = tuple([int(cl) for cl in rgb.split()])
        self.base <= html.DIV(style={"background-color": "rgb(%d, %d, %d)" % color,
                                     "min-height": "40px", "width": "40px", "float": "left"})

    def put_rect(self, _=0):
        rgb = (randint(50, 250), randint(50, 250), randint(50, 250))
        # rgb = (randint(50, 250), randint(50, 250), randint(50, 250))
        alphargb = [dict(a=1, b=2), list(rgb)]  # " ".join([str(cl) for cl in rgb])
        print("XXXXXXX>>>> def put_rect(self, _=0)", alphargb, rgb)
        self.conn.send(alphargb)
        # self.conn.send(alphargb)
        self.base <= html.DIV(style={"background-color": "rgb(%d, %d, %d)" % tuple(rgb),
                                     "min-height": "40px", "width": "40px", "float": "left"})


def main(last, nodeid):
    Base(last, nodeid)
    # Item.conn = Connect(last, nodeid, Item().create().add_item)
    # Game(last, nodeid)
