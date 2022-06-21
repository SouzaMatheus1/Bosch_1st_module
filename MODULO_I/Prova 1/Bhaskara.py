Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math

a = float(input('Insira o valor de "a": '))
b = float(input('Insira o valor de "b": '))
c = float(input('Insira o valor de "c": '))

delta = b**2 - 4*a*c
if delta < 0:
    print("Não há raízes para delta negativo. ")
    
else:
    x1 = -b + math.sqrt(delta) / (2*a)
    x2 = -b - math.sqrt(delta) / (2*a)
    print("o valor de X1 é {} e de X2 é {}".format(x1, x2))