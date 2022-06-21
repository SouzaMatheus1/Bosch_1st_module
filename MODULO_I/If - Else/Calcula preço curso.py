print("Bem vindo ao programa! Por favor insira seus dados abaixo.")
nomeAluno = input("Insira seu nome: ")
diasSem = int(input("Quantos dias na semana você estuda? "))
tipoCurso = int(input("Qual é o tipo de curso? \n(1 - Básico, 2 - Intermediário ou 3 - Avançado) "))



if tipoCurso == 1:
    print("O valor a ser pago é de R${:.0f},00".format((diasSem *7)*15))
    
elif tipoCurso == 2:
    print("O valor a ser pago é de R${:.0f},00".format((diasSem *8.5)*20))
    
elif tipoCurso == 3:
    print("O valor a ser pago é de R${:.0f},00".format((diasSem*10)*25))