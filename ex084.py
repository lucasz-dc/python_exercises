temporary = []
main = []
bigger = smaller = 0

while True:

    temporary.append(str(input('Nome: ')))
    temporary.append(float(input('Peso: ')))

    if len(main) == 0:
        bigger = smaller = temporary[1]

    else:

        if temporary[1] > bigger:
            bigger = temporary[1]
        if temporary[1] < smaller:
            smaller = temporary[1]

    main.append(temporary[:])
    temporary.clear()

    answer = str(input('Quer continuar [S/N]? '))

    if answer in 'Nn':
        break

print('-=-' * 20)

print(f'Ao todo, você cadastrou {len(main)} pessoas.')
print(f'O maior peso foi de {bigger}Kg. Peso de', end=' ')

for p in main:
    if p[1] == bigger:
        print(f'[{p[0]}] ', end='')

print()
print(f'O menor peso foi de {smaller}Kg. Peso de', end=' ')

for p in main:
    if p[1] == smaller:
        print(f'[{p[0]}] ', end='')
