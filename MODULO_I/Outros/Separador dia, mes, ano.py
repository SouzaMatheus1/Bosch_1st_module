meses = {1:'janeiro', 2:'fevereiro', 3:'março', 4:'abril', 5:'maio', 6:'junho', 
         7:'julho', 8:'agosto', 9:'setembro', 10:'outubro', 11:'novembro', 12:'dezembro'}

mesnum, mesdata = meses.values(), meses.keys()

while True:
    data = input("Insira data: ")
    dia, mes, ano = data.split('de')
    if data == 'janeiro':
        print("{}/{}/{}".format(dia, 1, ano))
    elif mes == 'fevereiro':
        print("{}/{}/{}".format(dia, 2, ano))