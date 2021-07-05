words = ('aprender', 'programar', 'linguagem', 'python', 'curso',
         'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
         'programador', 'futuro')

for vogals in words:
    print(f'\nNa palavra {vogals.upper()} temos ', end='')

    for letter in vogals:

        if letter in 'aeiou':
            print(letter, end=' ')
