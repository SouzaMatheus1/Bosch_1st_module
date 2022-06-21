# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 08:11:51 2022

@author: DISRCT
"""

#EXERCICIO 6.1 - Jogo par ou ímpar

import random 

random = random.randrange(10)
if random > 5:
    print(random)

import random

vitorias = 0

while True:
    parouimpar = str(input("Par ou ímpar? "))
    num = int(input("Jogue um número! "))
    escolhapc = int(random.randint(0, 100))
    resultado = (escolhapc + num)
    parouimpar.lower()
    print("{} + {} = {}".format(num, escolhapc, resultado))

    if parouimpar == 'par' and resultado % 2 == 0:
        vitorias += 1
        print('Você ganhou! \nVitórias =', vitorias)
        continue
    elif parouimpar == 'impar' and resultado % 2 != 0:
        vitorias += 1
        print('Você ganhou! \nVitórias =', vitorias)
        continue
    else:
        print('PC ganhou! ' )
        break



















