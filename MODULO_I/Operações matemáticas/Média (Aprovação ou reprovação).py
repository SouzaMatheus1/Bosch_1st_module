nomeAluno = input("Insira seu nome completo: ")
nota1 = float(input("Insira a nota da primeira prova: "))
nota2 = float(input("Insira a nota da segunda prova: "))
nota3 = float(input("Insira a nota da terceira prova: "))

mediaNota = (nota1 + nota2 + nota3)/3
mediaNota = round(mediaNota, 2)

print("\nAluno: ", nomeAluno, "Média: ", mediaNota)

if mediaNota >= 6.00:
    print("\nParabéns, você está aprovado!")
else:
    print('\nQue pena! Você está reprovado.')
