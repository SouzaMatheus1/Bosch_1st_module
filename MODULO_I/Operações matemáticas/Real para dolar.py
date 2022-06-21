valorReal = float(input("Insira o valor monetário em real: "))
cotaçãoDolar = float(input("Qual a cotação do dólar hoje? "))
conversãoDolarReal = valorReal * cotaçãoDolar 

print("O valor em dólar é de ${:.2f} ".format(conversãoDolarReal))