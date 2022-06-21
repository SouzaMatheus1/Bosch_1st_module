def convert():
    hora, minuto = input("Informe a hora: ").split(':', 1) 
    if int(hora) > 12:
        convers = int(hora) - 12
        print("{}:{} P.M".format(convers, minuto))
    elif int(hora) < 12:
        convers = int(hora)
        print("{}:{} A.M".format(convers, minuto))
    return convers

convert()