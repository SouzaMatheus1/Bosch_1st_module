pesoElevador = float(input("Qual a capacidade de peso máximo do elevador em Kg? "))

pesoPessoa1 = float(input("Qual é o peso da primeira pessoa em Kg? "))
pesoPessoa2 = float(input("Qual é o peso da segunda pessoa em Kg? "))
pesoPessoa3 = float(input("Qual é o peso da terceira pessoa em Kg? "))
pesoPessoa4 = float(input("Qual é o peso da quarta pessoa em Kg? "))
pesoPessoa5 = float(input("Qual é o peso da quinta pessoa em Kg? "))

pesoPessoas = (pesoPessoa1 + pesoPessoa2 + pesoPessoa3 + pesoPessoa4 + pesoPessoa5)

if pesoPessoas > pesoElevador: 
    print("\nO peso é maior do que o permitido!")
else:
    print("\nBoa viagem!")