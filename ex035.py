r1 = float(input('Medida da primeira reta: '))
r2 = float(input('Medida da segunda reta: '))
r3 = float(input('Medida da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo!')

else:
    print('Os segmentos acima não podem formar um triângulo!')
