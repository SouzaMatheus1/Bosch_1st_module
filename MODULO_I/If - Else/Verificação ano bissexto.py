ano = int(input("Insira o ano: "))

if ano % 400 == 0:
    print("Este ano é bissexto.")
elif ano % 4 == 0:
    print("Este ano é bissexto.")
elif ano % 100 != 0:
    print("Este ano não é bissexto.")