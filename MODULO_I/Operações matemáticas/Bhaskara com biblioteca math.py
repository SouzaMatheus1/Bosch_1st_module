import math

a = float(input('Insira o valor de "a": '))
b = float(input('Insira o valor de "b": '))
c = float(input('Insira o valor de "c": '))

delta = b**2 - 4*a*c
if delta < 0:
    print("Não há raízes para delta negativo. ")
    
else:
    x1 = -b + math.sqrt(delta) / 2*a
    x2 = -b - math.sqrt(delta) / 2*a
    print("o valor de X1 é {} e de X2 é {}".format(x1, x2))