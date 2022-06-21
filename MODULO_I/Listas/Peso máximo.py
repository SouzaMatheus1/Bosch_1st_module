peso1 = int(input("Qual o peso da primeira pessoa? "))
peso2 = int(input("Qual o peso da segunda pessoa? "))
peso3 = int(input("Qual o peso da terceira pessoa? "))
peso4 = int(input("Qual o peso da quarta pessoa? "))
peso5 = int(input("Qual o peso da quinta pessoa? "))

lista = [peso1, peso2, peso3, peso4, peso5]
print(lista)

pesomax = max(lista)

print("O maior peso registrado é de {} Kg.".format(pesomax))