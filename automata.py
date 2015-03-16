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
Cria a tabela do automata
############################################################
"""
__author__ = 'carlo'
GR = 204
UP = 24
SUBF = "M C L".split()
SUBC = dict(M=(UP//2, 0, 0), C=(0, UP, 0), L=(0, 0, UP))
ONTO = "S T I".split()
FILO = "PI PM PS ME".split()
PSUBF = "M. C. L.".split()
OFILO = "Cajado,Diferencia Cores,Grupos;Fogo,Sinais,Conta Alimentos;Tinta,Desenho Rupestre,Desenho Rupestre;" \
        "Palafita,Marca Habitação,Conta Animais".split(";")
OFILO = [tuple(filo.split(",")) for filo in OFILO]
PONTO = "_Sistema _Transformacao _Implicacao".split()
PFILO = "P.I. P.M. P.S. ME.".split()
TFILO = "PALEOLÍTICO INFERIOR,PALEOLÍTICO MÉDIO,PALEOLÍTICO SUPERIOR,MESOLÍTICO".split(",")
MICRO = "ORC PAR SIP PRO INF INO EXP COP REG PSS TRA PAS".split()
MICROT = "Objeto Real do Conhecimento,Paradoxo,Situação Problema,Prototipagem,Inferência,Inovação,Expansão Pioneira," +\
    "Conteúdo Processo,Regras Generativas,Processos Simultâneos e Sucessivos,Transcendência,Patamares Superiores"
NMICROT = ["%d.%s" % (n+1, t) for n, t in enumerate(MICROT.split(","))]
PREF = "https://activufrj.nce.ufrj.br/wiki/NeuroXIV_1/"
TBL = '<table border="1" cellpadding="0" cellspacing="0">'
TBD = "\t<tbody>"
TRO = "\t\t<tr>"
TCO = '\t\t\t<td style="background-color: rgb(%d, %d, %d);">'
FTBL = "</table>"
FTBD = "\t</tbody>"
FTRO = "\t\t</tr>"
FTCO = "\t\t\t</td>"
LINK = '<a href="https://activufrj.nce.ufrj.br/wiki/NeuroXIV_1/%s#%s">%s</a>'
TITULO = '<p><a id="%s" name="%s"></a>%s</p><p>&nbsp;</p>'
HEADC = tuple(x+y for s in SUBF for x, y in zip([GR]*3, SUBC[s]))
HEADO = [tuple(x+y+UP for x, y in zip([GR]*3, SUBC[s])) for s in SUBF]
HEAD = """
<tr>
        <td colspan="10" style="width:1188px;">
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
    </tr>
    <tr>
        <td colspan="3" style="width:290px;background-color: rgb(%d, %d, %d);">
        <p align="center">Ontog&ecirc;nese - %s</p>
        </td>
        <td colspan="3" style="width:287px;background-color: rgb(%d, %d, %d);">
        <p align="center">Ontog&ecirc;nese - %s</p>
        </td>
        <td colspan="3" style="width:269px;background-color: rgb(%d, %d, %d);">
        <p align="center">Ontog&ecirc;nese - %s</p>
        </td>
    </tr>
    <tr>
        <td style="width:93px;">
        <p align="center">Sistema</p>
        </td>
        <td style="width:104px;">
        <p align="center">Transforma&ccedil;&atilde;o</p>
        </td>
        <td style="width:93px;">
        <p align="center">Implica&ccedil;&atilde;o</p>
        </td>
        <td style="width:91px;">
        <p align="center">Sistema</p>
        </td>
        <td style="width:104px;">
        <p align="center">Transforma&ccedil;&atilde;o</p>
        </td>
        <td style="width:92px;">
        <p align="center">Implica&ccedil;&atilde;o</p>
        </td>
        <td style="width:90px;">
        <p align="center">Sistema</p>
        </td>
        <td style="width:90px;">
        <p align="center">Transforma&ccedil;&atilde;o</p>
        </td>
        <td style="width:90px;">
        <p align="center">Implica&ccedil;&atilde;o</p>
        </td>
    </tr>
"""


def tabela():
    print(TBL)
    print(TBD)
    for a, f, o in zip(FILO, TFILO, OFILO):
        headc = tuple(x+(y,) for y, x in zip(o[::-1], HEADO))
        head = tuple((f,)+HEADC+headc)
        odd = False
        print(head)
        print(HEAD % head)
        for b, t in zip(MICRO, MICROT.split(",")):
            color = GR if odd else GR + UP
            odd = not odd
            color = (color,)*3
            print(TRO)
            print (TCO % color+t+FTCO)
            for c in SUBF:
                color = tuple(x+y for x, y in zip(color, SUBC[c]))
                for d, e in zip(ONTO, PONTO):
                    print(TCO % color)
                    link = a+c+e
                    sigla = b+a+c+d
                    print(LINK % (link, sigla, sigla))
                    print(FTCO)
            print(FTRO)
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