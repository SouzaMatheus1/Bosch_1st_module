import random

listanum = []
listaorg = []

def aleatorio(n1, n2):
    a = random.randint(n1, n2)
    return a 
    
inicio = int(input("Defina o limite inferior: "))
fim = int(input("Defina o limite superior: "))
tamanholista = int(input("Defina o tamanho da lista: "))

for i in range(tamanholista):
    variavel = aleatorio(inicio, fim)
    listanum.append(variavel)
print('LISTA: ', listanum)

for i in range(tamanholista): 
    listaorg.append(min(listanum))
    listanum.remove(min(listanum))
print('LISTA ORDENADA: ', listaorg)
















