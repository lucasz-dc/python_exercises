values = []
pair = list()
odd = list()

while True:

    values.append(int(input('Digite um número: ')))
    want_to_continue = str(input('Quer continuar [S/N]? '))

    if want_to_continue in 'Nn':
        break

for i, v in enumerate(values):

    if v % 2 == 0:
        pair.append(v)

    elif v % 2 == 1:
        odd.append(v)

print('-=-' * 16)

print(f'Os valores digitados são {values}.')
print(f'Os valores pares são {pair}.')
print(f'Os valores ímpares são {odd}.')
