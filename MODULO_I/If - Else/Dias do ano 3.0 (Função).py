def repeat():
    numMes = int(input("Insira um número de 1 a 12, representando os meses do ano: "))
    ano = int(input("Insira o ano: "))

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

    # Verifica se o mês de fevereiro de 28 ou 29 dias #
    if numMes == 2:
        if ano % 400 == 0:
            print("\nO mês de {} tem 29 dias".format(meses[numMes - 1]))
        elif ano % 4 == 0:
                print("\nO mês de {} tem 29 dias".format(meses[numMes - 1]))
        elif ano % 100 != 0:
                print("\nO mês de {} tem 28 dias".format(meses[numMes - 1]))
    
    # Verificação resto dos meses                
    elif numMes % 2 != 0:
        print("O mês de {} tem 31 dias".format(meses[numMes - 1]))
                        
    elif numMes > 6 and numMes % 2 == 0:
        print("O mês de {} tem 31 dias".format(meses[numMes - 1]))
    
    else:
        print("O mês de {} tem 30 dias".format(meses[numMes - 1]))  
repeat()   