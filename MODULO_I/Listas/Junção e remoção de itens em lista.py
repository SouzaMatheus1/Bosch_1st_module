#LISTA A 
entrada1 = int(input("Insira um valor: " ))
entrada2 = int(input("Insira um valor: " ))
entrada3 = int(input("Insira um valor: " ))
entrada4 = int(input("Insira um valor: " ))
entrada5 = int(input("Insira um valor: " ))


listaA = [entrada1, entrada2, entrada3, entrada4, entrada5]
print("\nA lista A agora é: ", listaA)

#LISTA B
entrada6 = int(input("Insira um valor: " ))
entrada7 = int(input("Insira um valor: " ))
entrada8 = int(input("Insira um valor: " ))
entrada9 = int(input("Insira um valor: " ))
entrada10 = int(input("Insira um valor: " ))


listaB = [entrada6, entrada7, entrada8, entrada9, entrada10]
print("A lista B agora é: ", listaB)

#LISTA C
listaC = listaA + listaB
print('Esta são as duas listas juntas: ', listaC)

#REMOÇÃO ITEM
removerItem = int(input("Qual a posição do item que deseja remover da lista? "))

listaC.pop(removerItem + 1)
print(listaC)