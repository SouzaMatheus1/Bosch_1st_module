#EXERCICIO 3
print("Bem vindo, insira 5 valores: ")
entrada1 = int(input("Valor 1: " ))
entrada2 = int(input("Valor 2: " ))
entrada3 = int(input("Valor 3: " ))
entrada4 = int(input("Valor 4: " ))
entrada5 = int(input("Valor 5: " ))
lista1 = [entrada1, entrada2, entrada3, entrada4, entrada5]

minimo = min(lista1)
lista1.remove(minimo)
print(lista1)