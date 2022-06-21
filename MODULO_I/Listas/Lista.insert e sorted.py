#Exercicio 5
listanome1, listanome2, listanome3 = map(str, input("Digite três nomes: ").split())
listanum1, listanum2, listanum3 = map(int, input("Digite três números inteiros: ").split())

listanomes = []

listanomes.insert(0, listanome1)
listanomes.insert(1, listanome2)
listanomes.insert(2, listanome3)

listanumeros = []

listanumeros.insert(0, listanum1)
listanumeros.insert(1, listanum2)
listanumeros.insert(2, listanum3)

listageral = listanomes + listanumeros

listageral = sorted(listanomes)
print(listageral)

listageral = sorted(listanumeros)
print(listageral)