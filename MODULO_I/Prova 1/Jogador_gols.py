partidas = []
gols = []
somatoriagols = []
nomejogador = input("Nome do jogador: ")
partidasjogadas = int(input('Partidas jogadas: '))
geral = {'Nome' : nomejogador, 'Gols' : gols, 'Total de gols' : somatoriagols}
 
for i in range(partidasjogadas):
    partidas.append(partidasjogadas)
    golsporpartida = int(input('Gols na partida {}: '.format(len(partidas))))
    gols.append(golsporpartida)

somagols = sum(gols)
somatoriagols.append(somagols)

print("\nNa partida {} fez {} gols. ".format(partidasjogadas, golsporpartida))
print("\nO jogador {}, jogou {} partidas".format(nomejogador, partidasjogadas))
print(geral)
