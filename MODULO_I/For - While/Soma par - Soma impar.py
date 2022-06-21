#EXERCICIO 4
listapar = []
listaimpar = []
entrada = 0
resultado = 0
s_impar = 0
s_par = 0

while entrada < 1000:
    entrada = int(input("numero inteiro: "))
    if entrada % 2:
        s_impar = s_impar + entrada
    else:
        s_par = s_par + entrada
        
print("A soma dos números pares é", s_par, "e a soma dos números ímpares é", s_impar)