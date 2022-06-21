numMes = int(input("Insira um número de 1 a 12, representando os meses do ano: "))

meses = ['janeiro',
         'fevereiro',
         'março',
         'abril',
         'maio',
         'junho',
         'julho',
         'agosto',
         'setembro',
         'outubro',
         'novembro',
         'dezembro']

if numMes == 2:
    print("O mês de {} tem 28 dias".format(meses[numMes - 1]))
    
elif numMes % 2 != 0:
    print("O mês de {} tem 31 dias".format(meses[numMes - 1]))

elif numMes > 6 and numMes % 2 == 0:
    print("O mês de {} tem 31 dias".format(meses[numMes - 1]))
    
else:
    print("O mês de {} tem 30 dias".format(meses[numMes - 1]))