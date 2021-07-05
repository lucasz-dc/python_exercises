r1 = float(input('Tamanho da primeira reta: '))
r2 = float(input('Tamanho da segunda reta: '))
r3 = float(input('Tamanho da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO.')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('ISÓSCELES.')
    else:
        print('ESCALENO.')

else:
    print('Os segmentos acima não podem formar um triângulo.')
