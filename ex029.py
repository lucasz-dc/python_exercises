vel = float(input('Qual a velocidade do carro? '))
print('-=-' * 18)

if vel > 80:
    print('MULTADO! Você excedeu o limite de velocidade (80km/h).')
    exc = (vel - 80) * 7
    print('Sua multa é de R${:.2f}!'.format(exc))

print('Tenha um bom dia. Dirija com segurança.')
print('-=-' * 18)
