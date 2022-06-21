listanum = []
print("Bem vindo ao programa dobro!")
print("Digite SAIR, para encerrar o programa")
entrada = (input("Insira um número a ser multiplicado por 2: "))
entrada.lower()
dobro = int(entrada) * 2
listanum.append(dobro)
print(listanum)

while entrada != 'sair':
    if entrada != 'sair':
        entrada = (input("Insira um número a ser multiplicado por 2: "))
        entrada.lower()
        dobro = int(entrada) * 2
        listanum.append(dobro)
        print(listanum)
        continue
    elif entrada == 'sair':
        print("Programa encerrado.")
        break
    else:
        print("Comando inválido!")