from browser import document, html, window
from random import randint

P_N_O_D_E_D = "P_N_O_D_E-%02d"
LISTEN = []


class Game:
    def __init__(self, last, nodeid):
        self.last = self.this = last
        self.nid = nodeid
        # nodeid = nodeid.replace(":", "-")
        window.addEventListener("beforeunload", self.leave_connection)
        print("XXXXXXX>>>> __init__(self, last, nodeid)", last, self.nid % last)
        self.peer = peer = window.Peer.new(self.nid % last, {'key': '49rhnah5bore8kt9', 'debug': 3})

        peer.on('open', lambda pid: print("peer.on('open', lambda pid", pid))
        peer.on('connection', self.get_connection)
        self.conn = [peer.connect(self.nid % nid) for nid in range(1, last) if nid != self.this]
        # [conn.on('open', lambda: self.open_connection(conn)) for conn in self.conn]
        canvas = document["pydiv"]
        self.base = base = html.DIV(style={"background-color": "gray", "min-height": "400px"})
        base.onclick = self.put_rect
        canvas <= base
        base <= html.DIV(style={"background-color": "white", "min-height": "40px", "width": "40px", "float": "left"})
        base <= html.DIV(style={"background-color": "red", "min-height": "40px", "width": "40px", "float": "left"})

    def open_connection(self, conn):
        print("XXXXXXX>>>> open_connection(self, a_node)", conn.peer)
        conn.on('data', self.receive_rect)

    def get_connection(self, conn):
        print("XXXXXXX>>>> get_connection(self, a_node)", str(conn.peer))
        # connec = self.peer.connect(self.nid % str(conn.peer))
        self.cp = conn.peer
        self.conn.append(conn)
        conn.on('data', self.receive_rect)

    def receive_rect(self, rgb):
        print("XXXXXXX>>>> receive_rect(self, rgb)", ">%s<" % rgb)
        color = tuple([int(cl) for cl in rgb.split()])
        # last, color = color.pop(), tuple(color)
        # self.last = last if last > self.last else self.last
        self.base <= html.DIV(style={"background-color": "rgb(%d, %d, %d)" % color,
                                     "min-height": "40px", "width": "40px", "float": "left"})
        connec = self.peer.connect(self.nid % str(self.cp))

    def put_rect(self, _=0):

        rgb = (randint(50, 250), randint(50, 250), randint(50, 250))
        alphargb = " ".join([str(cl) for cl in rgb])
        print("XXXXXXX>>>> def put_rect(self, _=0)", alphargb, rgb, [conn.peer for conn in self.conn])
        [conn.send(alphargb) for conn in self.conn]
        self.base <= html.DIV(style={"background-color": "rgb(%d, %d, %d)" % rgb,
                                     "min-height": "40px", "width": "40px", "float": "left"})

    def leave_connection(self):
        [conn.close() for conn in self.conn]
        print("XXXXXXX>>>> leave_connection conn.close()", self.peer.destroyed)
        self.peer.disconnect()
        print("XXXXXXX>>>> leave_connection.peer.disconnect()", self.peer.destroyed)
        self.peer.destroy()
        print("XXXXXXX>>>> leave_connection", self.peer.destroyed)


def main(last, nodeid):
    Game(last, nodeid)
