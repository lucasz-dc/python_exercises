mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for line in range (0, 3):

    for column in range (0, 3):
        mat[line][column] = int(input(f'Digite um valor para [{line}, {column}]: '))

print('-=-' * 15)

for line in range (0, 3):

    for column in range (0, 3):
        print(f'[{mat[line][column]:^5}]', end='')

    print()
