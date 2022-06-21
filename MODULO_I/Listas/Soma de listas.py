lista1 = []
lista2 = []

a = 0
b = 0

while True:
    if a < 10:
        entradalista1 = (input("Insira 10 valores: "))
        lista1.append(entradalista1)
        a += 1
        continue
    elif b < 10:
        entradalista2 = (input("Insira mais 10 valores: "))
        lista2.append(entradalista2)
        b += 1
        continue
    else:
        lista = [*sum(zip(lista1, lista2),())]
        print(lista)
        break