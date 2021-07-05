factorial_number = int(input('Digiteum número para calcular seu fatorial: '))
counter = factorial_number
factor = 1

print(f'Calculando {factorial_number}! = ', end='')
while counter > 0:
    print(f'{counter}', end='')
    print(' x ' if counter > 1 else ' = ', end='')
    factor *= counter
    counter -= 1
print(f'{factor}')
