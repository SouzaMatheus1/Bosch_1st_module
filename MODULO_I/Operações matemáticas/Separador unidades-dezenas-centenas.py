numeroInteiro = int(input("Insira qualquer número inteiro menor que mil: "))
numeroUnidade = numeroInteiro % 10 
numeroDezena = numeroInteiro % 100 - numeroUnidade 
numeroCentena = numeroInteiro % 1000 - numeroDezena - numeroUnidade

if numeroInteiro > 1000:
    print("Insira um valor menor que mil!")

print("O número tem {} unidades, {} dezenas e {} centenas.".format(numeroUnidade, numeroDezena // 10, numeroCentena // 100))