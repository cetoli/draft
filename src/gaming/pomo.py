# -*- coding: utf-8
'''
Created on 14/07/2014
License: GLP
@author: Unknown
@Tradutor: Davi
'''

import time
apples = 0
gold = 0

def start():
   print("Olá e Bem-Vindo!")
   name = input("Qual é o seu nome?: ")
   print("Bem-Vindo," + name)
   print("O objetivo do jogo é coletar maçãs.")
   print("Depois de coletadas você as vende.")
   print("Para vendê-las, basta não coleta-las,")
   print("faça isso quando achar que tem")
   print("o número suficiente para vender,")
   print("o objetivo é conseguir vender de uma")
   print("vez só o suficiente apra ganhar o jogo,")
   print("embora consiga ganhar continuando a jogar,")
   print(" a intenção é conseguir de primeira! Boa Sorte!")
   choice = input("Você quer jogar? S/N? ")
   if choice == "S":
       begin()
   else:
       print("Tá certo, Adeus...")
def begin():
   global apples
   print("Vamos começar!")
   if gold > 77:
       print("Você Ganhou o Jogo!")
       play = input("Você quer jogar de novo?")
       if play == "S":
           begin()
       elif play == "N":
           print("Ok! Parabéns!")
   pick = input("Você quer pegar uma maçã? S/N? ")
   if pick == "S":
       global apples
       time.sleep(1)
       print("Você pegou uma maçã.")
       apples = apples + 1
       print("Você tem,", apples , " maçãs")
       begin()
       
   
   elif pick == "N":
       sell = input("Você quer vender suas maçãs? S/N? ")
       if sell == "S":
           global gold
       global apples
       print("Você está com," , apples , " Maçãs")
       print("Você vendeu suas maçãs.")
       gold = apples*10
       apples ==0
       print("Seu total de ouro é: ", gold)
       begin()
start()

