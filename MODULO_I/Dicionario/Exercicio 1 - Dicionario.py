#EXERCICIO 1
agenda = []

while True:
    nome = input("Insira um nome: ")
    if nome == "":
        break
    telefone = input("Insira um número de telefone: ")
    pessoa = {"Nome: " : nome, "Telefone" : telefone}
    agenda.append(pessoa)
    print(agenda)