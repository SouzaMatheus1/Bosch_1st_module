# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 08:04:26 2022

@author: DISRCT
"""

#EXERCICIO 4        
        
tempmes = []  
inferiormedia = []  
mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho'
       'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
a = 0
        

while True:
    if a < 12:
        entradatemp = int(input("Insira temperatura do mês: "))
        tempmes.append(entradatemp)
        mediatemp = sum(tempmes)/12
        a += 1
        continue     
    else:
        print("\nMédia temperatura anual: {:.2f}Cº".format(mediatemp))
        break
      
for i in range(len(tempmes)):
    mediatemp = sum(tempmes)/12
    if tempmes[i] > mediatemp:
        inferiormedia.append(tempmes[i])

print("O mês {} ficou acima da média de temperatura anual".format(len(inferiormedia)))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        