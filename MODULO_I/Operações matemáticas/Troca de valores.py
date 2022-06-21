variavelA = int(input("Insira o primeiro valor : "))
variavelB = int(input("Insira o segundo valor : "))

variavelControle = variavelA
variavelA = variavelB
variavelB = variavelControle 


print("\nO valor dos valores trocados são: ", "\nValor 1:", variavelA, "\nValor 2:", variavelB)