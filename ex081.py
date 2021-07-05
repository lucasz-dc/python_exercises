values = []

while True:

    values.append(int(input('Digite um valor: ')))
    answer = str(input('Quer continuar [S/N]? '))

    if answer in 'Nn':
        break

print('-=-' * 20)

print(f'Foram digitados {len(values)} números.')

values.sort(reverse=True)
print(f'Os valores, em ordem decrescente, são: {values}')

if 5 in values:
    print('O número 5 faz parte da lista.')

else:
    print('O valor 5 não faz parte da lista.')
