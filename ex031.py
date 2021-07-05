dist = float(input('Qual a distância da viagem (km)? '))
print('-' * 27)

if dist <= 200:
    p1 = 0.5 * dist
    print('A passagem custa R${:.2f}!'.format(p1))

else:
    p2 = 0.45 * dist
    print('A passagem custará R${:.2f}!'.format(p2))

print('-' * 27)
