total = 0
varinum1, varinum2, varinum3, varinum4, varinum5 = map(int,input("Digite cinco números: ").split())
#somatudo = varinum1 + varinum2 + varinum3 + varinum4 + varinum5

numeros = [varinum1, varinum2, varinum3, varinum4, varinum5]
for numero in numeros:
    print(numero + numero + 5)