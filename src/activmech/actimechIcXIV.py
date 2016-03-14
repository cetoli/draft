#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Calculo das notas para plotagem
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: $Date: 2011/11/10  $
:Status: This is a "work in progress"
:Revision: $Revision: 0.01 $
:Home: `Labase <http://labase.nce.ufrj.br/>`__
:Copyright: ©2010, `GPL <http://is.gd/3Udt>__. 
"""
from login import Main

__author__ = "Carlo E. T. Oliveira (cetoli@yahoo.com.br) $Author: cetoli $"
__version__ = "1.0 $Revision$"[10:-1]
__date__ = "2011/02/19 $Date$"

'''
import matplotlib.pyplot as plt
import mechanize
from BeautifulSoup import BeautifulSoup as soup
'''
ACTIV = 'https://activufrj.nce.ufrj.br'
PAGE = 'Inteligencia_Coletiva'

CAPITULOS = '''Introducao_livro_Programando_a_Inteligencia_Coletiva:apcavadas e Rubens
Capitulo_2_-_Making_Recommendations:thaisviana e ericalil
Capitulo_3_-_Descobrindo_Grupos:RaquelMachado e veluar
Capitulo_4_-_Searching_and_Ranking:Adnet e amrangel e Willi
CAP5_OTIMIZACAO:Rafaeldutrac e fmaraujo1981 e joseluiz
Capitulo_6_-_Document_Filtering:Estermp e Josy'''.split("\n")
CAPITULOS = {cap.split(":")[0]: cap.split(":")[-1].split(" e ") for cap in CAPITULOS}
ALUNOS = '''Fabiano Machado Araujo
fmaraujo1981
Raquel Moreira Machado
RaquelMachado
Jose Luiz Fonseca Pereira
joseluiz
THAIS DO NASCIMENTO VIANA
thaisviana
Rubens Lacerda Queiroz
Rubens
Alexandre Rangel
amrangel
Rafael Dutra
Rafaeldutrac
Érica Calil Nogueira
ericalil
Josemary kopke
Josy
Ester Morsoletto Poegere
Estermp
Rafael Adnet Pinho
Adnet
Ana Paula Cavadas Rodrigues
apcavadas
Anderson Silva
Willi'''.split('\n')
ALUNOS = {ALUNOS[index + 1]: ALUNOS[index] for index in range(0, len(ALUNOS) - 1, 2)}
NOPEERS = '''diana - Não votou
fmaraujo1981 - Não votou
sfdanielrg - Não votou
Willi - Não votou
diogo.mvieira - Não votou
simonecristina - Não votou
troppo - Não votou
vanessaferreira - Não votou
Estermp - Capitulo_2_-_Making_Recommendations Capitulo_6_-_Document_Filtering Capitulo_3_-_Descobrindo_Grupos CAP5_OTIMIZACAO Capitulo_4_-_Searching_and_Ranking Introducao_livro_Programando_a_Inteligencia_Coletiva
carlo - Não votou
Josy - Capitulo_2_-_Making_Recommendations Capitulo_6_-_Document_Filtering Capitulo_3_-_Descobrindo_Grupos CAP5_OTIMIZACAO Capitulo_4_-_Searching_and_Ranking Introducao_livro_Programando_a_Inteligencia_Coletiva
paulo - Não votou
chrisbarreira - Não votou
amrangel - Não votou
rj.armandoluiz - Não votou
Adnet - Capitulo_4_-_Searching_and_Ranking Capitulo_2_-_Making_Recommendations Capitulo_3_-_Descobrindo_Grupos Introducao_livro_Programando_a_Inteligencia_Coletiva CAP5_OTIMIZACAO Capitulo_6_-_Document_Filtering
flavio - Não votou
claudiam - Não votou
myriamkitz - Não votou
mauricioribeirogomes - Não votou
Thiago - Não votou
Carol - Não votou
rodgpp - Não votou
Rafaeldutrac - Não votou
edelbem - Não votou
thaisviana - Capitulo_2_-_Making_Recommendations Introducao_livro_Programando_a_Inteligencia_Coletiva Capitulo_4_-_Searching_and_Ranking Capitulo_3_-_Descobrindo_Grupos CAP5_OTIMIZACAO Capitulo_6_-_Document_Filtering
cristiane - Não votou
pcamargo - Não votou
avelinoferreiragf - Não votou
ramos - Não votou
RodrigoPadula - Não votou
leticiamedeiros - Não votou
crisanches - Não votou
lucianax - Não votou
joseluiz - Capitulo_2_-_Making_Recommendations Introducao_livro_Programando_a_Inteligencia_Coletiva Capitulo_3_-_Descobrindo_Grupos CAP5_OTIMIZACAO Capitulo_4_-_Searching_and_Ranking Capitulo_6_-_Document_Filtering
flaviocbarreto - Não votou
rafamachadoalves - Não votou
walkir - Não votou
apcavadas - Não votou
eduardomax - Não votou
soraiapacheco - Não votou
RaquelMachado - Não votou
Rubens - Não votou
ericalil - Não votou
walterbic - Não votou'''.split("\n")
NOPEERS = list(set(peer.split(" - ")[0] for peer in NOPEERS) - set(ALUNOS.keys()))
NPUBLICATION_DIR = '/home/carlo/Dropbox/Public/share/activ/'
PUBLICATION_DIR = '/home/carlo/Imagens/'
grades, averages = 'icxv_gradesa.png', 'icxv_averagesa.png'
OWNERS = dict(
    Aula_IC12_1_Redes_Sociais='rodgpp walkir'.split(),
    Aula_IC12_2_Percepcao_e_Contexto='diogo.mvieira leticiamedeiros'.split(),
    Aula_IC12_3_Sistemas_de_Recomendacao='diogo.mvieira walkir'.split(),
    Aula_IC12_4_Mobilidade_e_Ubiquidade_para_Colaboracao='RodrigoPadula leticiamedeiros'.split(),
    Aula_IC12_5_Aprendizagem_Colaborativa_com_Suporte_Computacional='crisanches mauricioribeirogomes'.split(),
    Aula_IC12_6_Conhecimento_Coletivo='crisanches rodgpp'.split(),
    Aula_IC12_7_Inteligencia_Artificial_para_Sistemas_Colaborativos='ramos RodrigoPadula'.split(),
    mauricioribeirogomes=['mauricioribeirogomes'],
    crisanches=['crisanches'],
    walkir=['walkir'],
    ramos=['ramos'],
    leticiamedeiros=['leticiamedeiros'],
    rodgpp=['rodgpp'],
    RodrigoPadula=['RodrigoPadula']
)
OWNERS.update({name: [name] for name in 'rj.armandoluiz diogo.mvieira'.split()})
OWNERS.update({'Inteligencia_Coletiva/' + name: value for name, value in OWNERS.items()})
# DEGRADE = list(range(9, 0, -1)) + [-1, -2]
DEGRADE = [90, 85, 78, 71, 64, 57, 50, 43, 36, 29, 22, 15, 8, 1, -10, -20]
NONOPEERS = 'Carol carlo claudiam abrapacarla edelbem myriamkitz'.split() + \
            ' sfdanielrg rafamachadoalves vanessaferreira flaviocbarreto'.split() + \
            ' rj.armandoluiz lucianax flavio cristiane simonecristina'.split()
AVALS = {}
OWNERS = {dono: [dono] for dono in ALUNOS.keys()}
OWNERS.update(CAPITULOS)

if __name__ == "__main__":
    print(CAPITULOS)
    print(ALUNOS)
    print(NOPEERS)
    print(OWNERS)
    Main(PAGE, OWNERS, AVALS, NOPEERS, DEGRADE, PUBLICATION_DIR, grades, averages).main()
