n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

med = (n1 + n2) / 2
print('Sua média foi {:.2f}.'.format(med))

if med < 5:
    print('Você foi REPROVADO!')

elif 5 <= med < 6.9:
    print('Você está de RECUPERAÇÃO!')

elif med >= 7:
    print('Parabéns! Você foi APROVADO!')
