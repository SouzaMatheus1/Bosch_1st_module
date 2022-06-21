# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 09:55:54 2022

@author: DISRCT
"""

#Exercicio 6.3 - Função 

import time

def contador(num1, num2, passo):
    if passo > 0:
        for i in range(num1, num2+1, passo):
            time.sleep(0.5)
            print(i)
    else:
        for i in range(num1, num2-1, passo):
            print(i)
            



contador(1, 20, 1)
contador(20, 0, -2)
contador(0, 105, 5)
contador(96, 52, -2)
contador(3, 41, 1)
contador(75, 15, -5)
contador(390, 39, -10)
contador(0, 70, 7)







