s = float(input('Qual o seu salário? R$'))

if s > 1250:
    a1 = s * 0.1
    s1 = a1 + s
    print('Com o aumento de R${:.2f}, seu salário será R${:.2f}.'.format(a1, s1))

if s <= 1250:
    a2 = s * 0.15
    s2 = a2 + s
    print('Com o aumento de R${:.2f}, seu salário será de R${:.2f}.'.format(a2, s2))
