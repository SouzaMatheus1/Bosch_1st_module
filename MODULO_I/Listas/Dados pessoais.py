#Exercicio 4
nome = input("Digite seu nome: ")
telefone = int(input("Digite seu telefone sem DDD: "))
idade = int(input("Digite sua idade: "))

nome2 = input("Digite seu nome: ")
telefone2 = int(input("Digite seu telefone sem DDD: "))
idade2 = int(input("Digite sua idade: "))

listanome = [nome , nome2]
listatelefone = [telefone , telefone2]
listaidade = [idade , idade2]
listageral = listanome + listatelefone + listaidade

print("Nomes:", listanome)
print("Telefones:", listatelefone)
print("Idades:", listaidade)

if nome.isdigit() == False:
    print("Numerais")
    print(listatelefone + listaidade)  