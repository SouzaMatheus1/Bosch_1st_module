listasal = []
listaidade = []
listaF = []
listaM = []
totalPessoas = []


quantidadeF = 0
quantidadeM = 0
quantidadeSal = 0

while True:
    sexo = input("Informe seu sexo (M/F): ")
    sexo = sexo.lower()
    if sexo == 'f':
        totalPessoas.append('F')
    else:
        totalPessoas.append('M')
    idade = int(input("Informe sua idade: "))
    salario = int(input("Informe seu salário: "))
    if idade < 0:
        break
    else:
        listaidade.append(idade)
        print("A menor idade registrada é: {} anos".format(min(listaidade)), "\ne a maior idade registrada é: {} anos.".format(max(listaidade)))
    listasal.append(salario)
    mediaSal = sum(listasal)/len(listasal)
    print("A média de salário é: R${:.2f}".format(mediaSal))
    print("A quantidade de muulheres é: ", totalPessoas.count('F')) 
    index = listasal.index(min(listasal))
    menoridade = listaidade[index]
    menorsexo =  totalPessoas[index]
    print("A idade com menor salário é:", menoridade, "\nE o sexo com menor salário é:", menorsexo)
         