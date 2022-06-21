a = 0
for i in range(15):
    print("For: ", i)
    while(a < 10):
        print('While: ', a)
        if ( a == 4):
            print('Entrou no if')
            break
        a += 1