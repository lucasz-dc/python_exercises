list = ('Lápis', 1.75,
        'Borracha', 2,
        'Caderno', 15.98,
        'Estojo', 25,
        'Transferidor', 4.20,
        'Compasso', 9.99,
        'Mochila', 120.32,
        'Canetas', 22.30,
        'Livro', 34.90)

print('=' * 40)
print(f'{"Listagem de Preços":^40}')
print('=' * 40)

for position in range(0, len(list)):
        if position % 2 == 0:
                print(f'{list[position]:.<30}', end='')
        else:
                print(f'R${list[position]:>7.2f}')

print('=' * 40)
