while True:
    multiplication_table = int(input('Quer ver a tabuada de qual número? '))
    if multiplication_table < 0:
        break
    print('-' * 40)
    for c in range(1, 11):
        print(f'{multiplication_table} x {c} = {multiplication_table * c} ')
    print('-' * 40)

print('Programa encerrado.')
