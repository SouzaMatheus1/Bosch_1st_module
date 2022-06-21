idade = []
altura = []
inferiormedia = []

a = 0

while True:
    if a < 10:
        eidade = int(input("Idade: "))
        idade.append(eidade)
        ealtura = float(input("Altura: "))
        altura.append(ealtura)
        a += 1
        continue
    else:
        break

for i in range(len(altura)):
    mediaaltura = (sum(altura)/len(altura))
    if altura[i] < mediaaltura and idade[i] > 13:
        inferiormedia.append(altura[i])


print ("A média de altura é: {:.2f}".format(mediaaltura))
print ("Quantidade de pessoas abaixo da média: ", len(inferiormedia))
print ("As alturas abaixo da média são: ", inferiormedia)