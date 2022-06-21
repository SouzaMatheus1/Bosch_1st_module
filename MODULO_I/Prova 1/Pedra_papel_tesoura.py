import random
movimentos = ['1 - Pedra', '2 - Papel', '3 - Tesoura']

iniciar = int(input('Deseja iniciar? \n 1 - Sim \n 2 - Não \n'))

while iniciar == 1:
    movmaq = random.choice(movimentos)
    escolhajogador = int(input('Escolha sua jogada: \n 1 - Pedra \n 2 - Papel \n 3 - Tesoura \n 0 - Sair \n'))
    if movmaq == '1 - Pedra':
        print('Máquina jogou: 1 - Pedra')
    elif movmaq == '2 - Papel':
        print('Máquina jogou: 2 - Papel')
    elif movmaq == '3 - Tesoura':
        print('Máquina jogou: 3 - Tesoura')
        
    if escolhajogador == 1 and movmaq == '2 - Papel':
        print('Você perdeu!')
    elif escolhajogador == 1 and movmaq == '3 - Tesoura':
        print('Você ganhou!')
    elif escolhajogador == 2 and movmaq == '1 - Pedra':
        print('Você ganhou!')
    elif escolhajogador == 2 and movmaq == '3 - Tesoura':
        print('Você ganhou!')
    elif escolhajogador == 3 and movmaq == '1 - Pedra':
        print('Você perdeu!')
    elif escolhajogador == 3 and movmaq == '2 - Papel':
        print('Você ganhou!')
    elif escolhajogador == 3 and movmaq == '3 - Tesoura':
        print('Empate!')
    elif escolhajogador == 2 and movmaq == '2 - Papel':
        print('Empate!')
    elif escolhajogador == 1 and movmaq == '1 - Pedra':
        print('Empate!')
    elif escolhajogador == 0:
        print('Obrigado por jogar!')
        break;
