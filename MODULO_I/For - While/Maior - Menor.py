#EXERCICIO 2
listanum = []
    
for i in range (10):
    entranum = int(input("Insira um valor: "))
    listanum.append(entranum)

maxnum = max(listanum)
minnum = min(listanum)
print("O maior número é", maxnum, "e o menor número é", minnum)