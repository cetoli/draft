# -*- coding: UTF8 -*-
# Este arquivo é parte do programa Automata
# Copyright 2014-2015 Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
#
# Automata é um software livre; você pode redistribuí-lo e/ou
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
Cria a tabela do automata
############################################################
"""
__author__ = 'carlo'
GR = 204
UP = 24
SUBF = "NO CARTA AGUA CHAVE ZOOLO SEISPA".split()
SUBC = dict(NO=(0, 0, 0), CARTA=(UP // 2, 0, 0), AGUA=(0, UP, 0), CHAVE=(0, 0, UP),
            ZOOLO=(UP // 2, UP, 0), SEISPA=(0, UP, UP))
FUNTEST = "Funções Executivas/ Jogos,Jogo das Cartas,Jogo da Água," \
        "Jogo da Chave,Jogo do Zoológico,Jogo das 6 Partes".split(",")
FUNKEYS = "Capacidade,Sequenciamento,Atenção,Resistência," \
          "Feedback,Coordenação,Ambientação," \
          "Habilidade".split(",")
FUNEXEC = "Capacidade de Planejamento,Sequenciamento de Comportamento,Atenção Sustentada,Resistência a Interferência," \
          "Uso de Feedback,Coordenação de Atividade Simultânea,Troca de Ambientação," \
          "Habilidade de lidar com novas situações".split(",")
PREF = "https://activufrj.nce.ufrj.br/wiki/NeuroXIV_1/"
TBL = '<table border="1" cellpadding="0" cellspacing="0">'
THD = "\t<thead>"
TBD = "\t<tbody>"
TRO = "\t\t<tr>"
TCO = '\t\t\t<td style="width:%dpx;background-color: rgb(%d, %d, %d);">'
FTBL = "</table>"
FTHD = "\t</thead>"
FTBD = "\t</tbody>"
FTRO = "\t\t</tr>"
FTCO = "\t\t\t</td>"
PDATA = '\t\t\t\t<p align="center">%s</p>'
TDATA = TCO + "\n" + PDATA + "\n" + FTCO
LINK = '<a href="https://activufrj.nce.ufrj.br/wiki/NeuroXIV_1/%s#%s">%s</a>'
TITULO = '<p><a id="%s" name="%s"></a>%s</p><p>&nbsp;</p>'
HEADC = tuple(x+y for s in SUBF for x, y in zip([GR]*3, SUBC[s]))
HEADO = [tuple(x+y+UP for x, y in zip([GR]*3, SUBC[s])) for s in SUBF]
HEAD = """<tr>
        <td colspan="20" style="width:1188px;">
        <p align="center">%s</p>
        </td>
    </tr>
    <tr>
        <td rowspan="4" style="width:342px;height:5px;">
        <p align="center">Microg&ecirc;neses</p>
        </td>
        <td colspan="9" style="width:846px;height:5px;">
        <p align="center">Sub-filog&ecirc;nese</p>
        </td>
    </tr>
    <tr>
        <td colspan="3" style="width:290px;background-color: rgb(%d, %d, %d);">
        <p align="center">Matem&aacute;tica</p>
        </td>
        <td colspan="3" style="width:287px;background-color: rgb(%d, %d, %d);">
        <p align="center">Linguagem</p>
        </td>
        <td colspan="3" style="width:269px;background-color: rgb(%d, %d, %d);">
        <p align="center">Ci&ecirc;ncia</p>
        </td>
    </tr>"""


def tabela():
    print(TBL)
    print(TBD)
    print(TRO)
    for fkey, fname in zip(SUBF, FUNTEST):
        cellw = 250 if fkey == "NO" else 150
        cell = TDATA % ((cellw,) + tuple(GR + color for color in SUBC[fkey]) + (fname,))
        print(cell)
        # print(HEAD % head)
    odd = False
    print(FTRO)
    for funex in FUNEXEC:
        print(TRO)
        for fkey, fname in zip(SUBF, FUNTEST):
            cellw = 250 if fkey == "NO" else 150
            name = funex if fkey == "NO" else funex[:3] + fkey
            bcolor = GR if odd else GR + 24
            cell = TDATA % ((cellw,) + tuple(bcolor + color for color in SUBC[fkey]) + (name,))
            print(cell)
            # print(HEAD % head)
        print(FTRO)
        odd = not odd

        '''
        for b, st in zip(MICRO, MICROT.split(",")):
            color = GR if odd else GR + UP
            odd = not odd
            color = (color,)*3
            print(TRO)
            print (TCO % color+st+FTCO)
            for c in SUBF:
                color = tuple(x+y for x, y in zip(color, SUBC[c]))
                for d, e in zip(ONTO, PONTO):
                    print(TCO % color)
                    link = a+c+e
                    sigla = b+a+c+d
                    print(LINK % (link, sigla, sigla))
                    print(FTCO)
            print(FTRO)
            '''
    print(FTBD)
    print(FTBL)


def codigos():
    for a in FILO:
        for c in SUBF:
            for d, e in zip(ONTO, PONTO):
                link = a+c+e
                print('</hr><H1>%s</H1>' % link)
                for b in MICRO:
                    sigla = b+a+c+d
                    print(TITULO % (sigla, sigla, sigla))


tabela()
# codigos()
