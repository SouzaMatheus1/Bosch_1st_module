print('Bem-vindo ao programa "Calculadora"!')
entradanum1 = float(input("Insira um número: "))
entradaoperaçao = input("+, -, /, *  ")
entradanum2 = float(input("Insira um número: "))

if entradaoperaçao == '+':
    soma = entradanum1 + entradanum2
    print("A soma dos valores é: ", soma)
elif entradaoperaçao == '-':
    subtraçao = entradanum1 - entradanum2
    print("A subtração dos valores é: ", subtraçao)
elif entradaoperaçao == '/':
    divisao = entradanum1 / entradanum2
    print("A divisão dos valores é: ", divisao)
elif entradaoperaçao == '*':
    multiplicacao = entradanum1 * entradanum2
    print("A múltiplicação dos valores é: ", multiplicacao)