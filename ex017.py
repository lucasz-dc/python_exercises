import math

co = float(input('Medida do cateto oposto: '))
ca = float(input('Medida do cateto adjacente: '))

h = math.sqrt(co**2 + ca**2)
print('A hipotenusa equivale a {:.2f}.'.format(h))
