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
SUBF = "NO CARTA AGUA CHAVE ZOOLO SEISPA TRAIL VERBAL DESIGN COLOR SORT TWENTY WORD TOWER".split()
SUBC = dict(NO=(0, 0, 0), CARTA=(UP // 2, 0, 0), AGUA=(0, UP, 0), CHAVE=(0, 0, UP),
            ZOOLO=(UP // 2, UP, 0), SEISPA=(0, UP, UP),
            TRAIL=(UP // 2, 0, UP), VERBAL=(UP // 2, 0, 0), DESIGN=(0, UP, 0), COLOR=(0, 0, UP),
            SORT=(UP // 2, UP, 0), TWENTY=(0, UP, UP), WORD=(UP // 2, UP // 2, 0), TOWER=(UP // 2, 0, UP)

            )
FUNTEST = "Funções Executivas/ Jogos,Jogo das Cartas,Jogo da Água," \
        "Jogo da Chave,Jogo do Zoológico,Jogo das 6 Partes," \
          "Trail Making,Verbal Fluency,Design Fluency,Color-Word Interference,Sorting," \
          "Twenty Questions,Word Context,Tower,Proverb".split(",")
FUNKEYS = "Capacidade,Sequencia,Atenção,Resistência," \
          "Feedback,Coordenação,Ambientação," \
          "Habilidade,Controle,Formação,Transfere".split(",")
FUNEXEC = "Capacidade de Planejamento,Sequenciamento de Comportamento,Atenção Sustentada,Resistência a Interferência," \
          "Uso de Feedback,Coordenação de Atividade Simultânea,Troca de Ambientação," \
          "Habilidade de lidar com novas situações,Controle Inibitorio," \
          "Formação de Conceito,Transferência de Conceitos para ações".split(",")
PREF = "https://activufrj.nce.ufrj.br/wiki/NeuroXIV_1/"
TBL = '<table border="1" cellpadding="0" cellspacing="0">'
THD = "\t<thead>"
TBD = "\t<tbody>"
TRO = "\t\t<tr>"
TCO = '\t\t\t<td style="width:%dpx;background-color: rgb(%d, %d, %d);">'
TCH = '\t\t\t<th style="width:%dpx;background-color: rgb(%d, %d, %d);">'
FTBL = "</table>"
FTHD = "\t</thead>"
FTBD = "\t</tbody>"
FTRO = "\t\t</tr>"
FTCO = "\t\t\t</td>"
PDATA = '\t\t\t\t<p align="center">%s</p>'
TDATA = TCO + "\n" + PDATA + "\n" + FTCO
THH = TCH + PDATA + "\t\t\t</th>"
LINK = '<a href="https://activufrj.nce.ufrj.br/wiki/NEURO_XV/%s#%s">%s</a>'
TITULO = '\t<h2><a id="%s" name="%s"></a>%s</h2>\n\t\t<p>&nbsp; %s</p>'
HEADC = tuple(x+y for s in SUBF for x, y in zip([GR]*3, SUBC[s]))
HEADO = [tuple(x+y+UP for x, y in zip([GR]*3, SUBC[s])) for s in SUBF]


def encode(string):
    return string.replace(' ', '_').replace('Á', 'A').replace('ó', 'o')\
        .replace('ç', 'c').replace('ã', 'a').replace('ê', 'e')


def tabela():
    print(TBL)
    print(THD)
    print(TRO)
    for fkey, fname in zip(SUBF, FUNTEST):
        cellw = 250 if fkey == "NO" else 150
        cell = THH % ((cellw,) + tuple(GR + color for color in SUBC[fkey]) + (fname,))
        print(cell)
        # print(HEAD % head)
    odd = False
    print(FTRO)
    print(FTHD)
    print(TBD)
    for funkey, funex in zip(FUNKEYS, FUNEXEC):
        print(TRO)
        for fkey, fname in zip(SUBF, FUNTEST):
            cellw = 280 if fkey == "NO" else 150
            name = funex if fkey == "NO" else funkey + fkey
            anchor = LINK % (encode(fname), encode(name), name) if fkey != "NO" else name
            bcolor = GR if odd else GR + 24
            cell = TDATA % ((cellw,) + tuple(bcolor + color for color in SUBC[fkey]) + (anchor,))
            print(cell)
            # print(HEAD % head)
        print(FTRO)
        odd = not odd
    print(FTBD)
    print(FTBL)


def codigos():
    for fkey, fname in zip(SUBF, FUNTEST)[1:]:
        print('</hr><H1>%s</H1>' % fname)
        for funkey, funex in zip(FUNKEYS, FUNEXEC):
            sigla = funkey+fkey
            text = "%s para %s" % (funex, fname)
            print(TITULO % (sigla, encode(sigla), text, text))


tabela()
# codigos()
