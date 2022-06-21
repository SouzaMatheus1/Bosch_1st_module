#Exercicio 7
lista = []

for numero in range(10):
    entrada = float(input("Insira um valor: " ))
    if entrada < 0:
        lista.append(0)
    if entrada > 0:
        lista.append(entrada)
        
print(lista)