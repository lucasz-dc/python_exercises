mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

pairs_sum = bigger = column_sum = 0

for line in range(0, 3):

    for column in range (0, 3):
        mat[line][column] = int(input(f'Digite um valor para [{line}, {column}]: '))

print('-=-' * 15)

for line in range(0, 3):

    for column in range(0, 3):
        print(f'[{mat[line][column]:^5}]', end='')

        if mat[line][column] % 2 == 0:
            pairs_sum += mat[line][column]

    print()

print('-=-' * 15)

print(f'A soma dos valores pares é {pairs_sum}.')

for line in range(0, 3):
    column_sum += mat[line][2]

print(f'A soma dos valores da terceira coluna é {column_sum}.')

for column in range(0, 3):

    if column == 0:
        bigger = mat[1][column]

    elif mat[1][column] > bigger:
        bigger = mat [1][column]

print(f'O maior valor da segunda linha é {bigger}.')