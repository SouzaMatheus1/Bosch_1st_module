import random

vitorias = 0
escolhapc = int(random.randint(0, 100))

while True:
    parouimpar = str(input("Par ou ímpar? "))
    parouimpar.lower()
    escolhapc = int(random.randint(0, 10))
    if parouimpar == 'par' or parouimpar == 'impar':
        num = int(input("Jogue um número! "))
        resultado = (escolhapc + num)
        print("Você jogou: {} + PC jogou: {} = {}".format(num, escolhapc, resultado))
    else: 
        print("Apenas PAR ou ÍMPAR!!" )
        continue
        
    if parouimpar == 'par' and resultado % 2 == 0:
        vitorias += 1
        print('Você ganhou! \nVitórias =', vitorias)
        continue
    elif parouimpar == 'impar' and resultado % 2 != 0:
        vitorias += 1
        print('Você ganhou! \nVitórias =', vitorias)
        continue
    else:
        print('PC ganhou! ' )
        resposta = str(input("Deseja continuar? (S/N) "))
        resposta.lower()
        if resposta == 's':
            print("Vitórias: ", vitorias)
            continue
        else:
            print("Vitórias: ", vitorias)
            break