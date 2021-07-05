ap = float(input('Qual é a altura da parede (em metros)? '))
lp = float(input('Qual é a largura da parede (em metros)? '))

area = ap * lp

print('A área de parede é de {:.2f} m².'.format(area))

lt = area / 2
print('Para pintar a parede, serão necessários {:.2f} litros de tinta.'.format(lt))
