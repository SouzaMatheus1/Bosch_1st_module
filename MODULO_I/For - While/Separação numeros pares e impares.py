#EXERCICIO 5
listapar = []
listaimpar = []
entrada = 0

for entrada in range (10):
    entrada = int(input("Insira um valor: "))
    if entrada % 2:
        listaimpar.append(entrada)
    else:
        listapar.append(entrada)
print("Os valores pares são:", listapar, "\nE os valores ímpares são:", listaimpar)