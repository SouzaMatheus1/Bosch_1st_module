data = input("Insira data: ")
dia, mes, ano = data.split('de')

if mes == ' janeiro ':
    print("{}/{}/{}".format(dia,1,ano))
elif mes == ' fevereiro ':
    print("{}/{}/{}".format(dia,2,ano))
elif mes == ' março ':
    print("{}/{}/{}".format(dia,3,ano))
elif mes == ' abril ':
    print("{}/{}/{}".format(dia,4,ano))
elif mes == ' maio ':
    print("{}/{}/{}".format(dia,5,ano))
elif mes == ' junho ':
    print("{}/{}/{}".format(dia,6,ano))
elif mes == ' julho ':
    print("{}/{}/{}".format(dia,7,ano))
elif mes == ' agosto ':
    print("{}/{}/{}".format(dia,8,ano))
elif mes == ' setembro ':
    print("{}/{}/{}".format(dia,9,ano))
elif mes == ' outubro ':
    print("{}/{}/{}".format(dia,10,ano))
elif mes == ' novembro ':
   print("{}/{}/{}".format(dia,11,ano))
elif mes == ' dezembro ':
    print("{}/{}/{}".format(dia,12,ano))
else:
    print("Verifique o que foi digitado!" )
