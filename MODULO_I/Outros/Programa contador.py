import time

def cont(entrada, velocidade):
    for i in range (entrada + 1):
        conta = 0
        conta = entrada + 1
        time.sleep(velocidade)
        print(i)
        continue
        return conta

print("-=-=-=-=-=-Bem-vindo ao programa!-=-=-=-=-=-")
entrada = int(input("Defina o limite da contagem: "))
velocidade = int(input("Digite também a velocidade do contador: "))
cont(entrada, velocidade)