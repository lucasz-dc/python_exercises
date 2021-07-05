number = int(input('Digite um número: '))

double = number * 2
triple = number * 3
square_root = number ** (1/2)

print('O dobro de {} é {}.'.format(number, double), end=' ')
print('O triplo de {} é {}.'.format(number, triple), end=' ')
print('A raiz quadrada de {} é {:.2f}.'.format(number, square_root))
