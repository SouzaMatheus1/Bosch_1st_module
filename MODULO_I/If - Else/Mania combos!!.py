print("Seja bem-vindo ao big mania combos!")
print("\nOs combos são apenas válidos no salão - não fazem parte do nosso delivery")

combo1 = "Combo 1: X-salada + Fritas + KS(Sabores)"
combo2 = "Combo 2: X-Picanha Bacon + Fritas + KS(Sabores)"
combo3 = "Combo 3: X-Calabresa Vinagrete + Nuggets + KS(Sabores)"
combo4 = "Combo 4: X-Frango Salada + Anéis de cebola + KS(Sabores)"
combo5 = "Combo 5: Duplo Cheddar Bacon + Fritas + KS(Sabores)"
combokids = "Combo Kids: X-Burguer + Batata Sorriso + Coca 200ml ou Suco (consulte) + Danoninho"

escolhacombo = input("Qual seria o seu pedido? ")
escolhacombo.lower()
if escolhacombo == 'combo 1':
    print("O combo 1 sai por R$ 23,99")
elif escolhacombo == 'combo 2':
    print("O combo 2 sai por R$ 27,99")
elif escolhacombo == 'combo 3':
    print("O combo 3 sai por R$ 26,99")
elif escolhacombo == 'combo 4':
    print("O combo 4 sai por R$ 25,99")
elif escolhacombo == 'combo 5':
    print("O combo 5 sai por R$ 32,99")
elif escolhacombo == 'combo kids':
    print("O combo kids sai por R$ 16,99")
else:
    print('Escolha um dos combos disponíveis.')