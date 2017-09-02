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
from browser import document, html, window
from random import randint


class Game:
    def __init__(self, last, nodeid):
        self.last = self.this = last
        self.nid = nodeid
        self.peer = None
        self.conn = []
        window.addEventListener("beforeunload", self.leave_connection)
        print("XXXXXXX>>>> __init__(self, last, nodeid)", last, self.nid % last)
        self.init_peer(last)
        canvas = document["pydiv"]
        self.base = base = html.DIV(style={"background-color": "gray", "min-height": "400px"})
        base.onclick = self.put_rect
        canvas <= base
        base <= html.DIV(style={"background-color": "white", "min-height": "40px", "width": "40px", "float": "left"})
        base <= html.DIV(style={"background-color": "red", "min-height": "40px", "width": "40px", "float": "left"})

    def remote_action(self, data=""):
        self.receive_rect(data)

    def init_peer(self, last):
        self.peer = peer = window.Peer.new(self.nid % last, {'key': '49rhnah5bore8kt9', 'debug': 0})

        def do_connect(node_id):
            print("XXXXXXX>>>> init_peer.channel.do_connect", node_id)
            conn = peer.connect(node_id)
            conn.on('data', self.receive_rect)
            return conn
        peer.on('connection', self.get_connection)
        self.conn = [do_connect(self.nid % nid) for nid in range(1, last) if nid != self.this]

    def get_connection(self, conn):
        print("XXXXXXX>>>> get_connection(self, a_node)", str(conn.peer))
        if conn.peer not in [cn.peer for cn in self.conn]:
            print("XXXXXXX>>>> append_connection(self, a_node)", str(conn.peer))
            self.conn.append(self.peer.connect(str(conn.peer)))
        conn.on('data', self.receive_rect)
        conn.send("10 20 30")

    def receive_rect(self, rgb):
        print("XXXXXXX>>>> receive_rect(self, rgb)", ">%s<" % rgb)
        color = tuple([int(cl) for cl in rgb.split()])
        self.base <= html.DIV(style={"background-color": "rgb(%d, %d, %d)" % color,
                                     "min-height": "40px", "width": "40px", "float": "left"})

    def put_rect(self, _=0):
        rgb = (randint(50, 250), randint(50, 250), randint(50, 250))
        alphargb = " ".join([str(cl) for cl in rgb])
        print("XXXXXXX>>>> def put_rect(self, _=0)", alphargb, rgb, [conn.peer for conn in self.conn])
        [conn.send(alphargb) for conn in self.conn]
        self.base <= html.DIV(style={"background-color": "rgb(%d, %d, %d)" % rgb,
                                     "min-height": "40px", "width": "40px", "float": "left"})

    def leave_connection(self, _=0):
        [conn.close() for conn in self.conn]
        print("XXXXXXX>>>> leave_connection conn.close()", self.conn)
        # self.peer.disconnect()
        # print("XXXXXXX>>>> leave_connection.peer.disconnect()", self.peer.destroyed)
        # self.peer.destroy()
        # print("XXXXXXX>>>> leave_connection", self.peer.destroyed)


def main(last, nodeid):
    Game(last, nodeid)
