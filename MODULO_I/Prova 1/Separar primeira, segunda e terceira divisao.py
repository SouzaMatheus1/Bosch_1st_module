times = ['1_palmeiras', '2_coritiba', '1_corintians', '3_juventude','2_fluminense','3_bahia',
  '1_cuiaba','2_cascavel','3_ponte preta', '2_parana clube','3_volta redonda']

primeiradiv = []
segundadiv = [] 
terceiradiv = []

times1 = ('1_palmeiras'.split('1_'), '1_cuiaba'.split('1_'))
primeiradiv.append(times1)

times.remove('1_palmeiras')
primeiradiv.append('1_palmeiras')

times.remove('1_corintians')
primeiradiv.append('1_corintians')

times.remove('1_cuiaba')
primeiradiv.append('1_cuiaba')

times.remove('2_coritiba')
segundadiv.append('2_coritiba')

times.remove('2_fluminense')
segundadiv.append('2_fluminense')

times.remove('2_cascavel')
segundadiv.append('2_cascavel')

times.remove('2_parana clube')
segundadiv.append('2_parana clube')

times.remove('3_juventude')
terceiradiv.append('3_juventude')

times.remove('3_bahia')
terceiradiv.append('3_bahia')

times.remove('3_ponte preta')
terceiradiv.append('3_ponte preta')

times.remove('3_volta redonda')
terceiradiv.append('3_volta redonda')

print(primeiradiv)
print(segundadiv)
print(teceiradiv)
