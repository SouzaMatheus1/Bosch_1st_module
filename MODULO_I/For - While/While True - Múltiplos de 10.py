while True:
    numeros = float(input("Insira numero: " ))
    if numeros < 0:
        break
    if numeros %10 == 0:
        print("Esse número é múltilplo de 10.")
    else:
        print("Esse número não é múltilplo de 10.")
        continue