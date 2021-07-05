print('-=-' * 10)
print('     10 termos de uma PA')
print('-=-' * 10)

first_term = int(input('Primeiro termo: '))
reason = int(input('Razão: '))
term = first_term
counter = 1
total = 0
more_terms = 10

while more_terms != 0:

    total += more_terms

    while counter <= total:
        print(f'{term} \033[33m-→\033[m ', end='')
        term += reason
        counter += 1

    print('Pausa...')

    more_terms = int(input('Quantos termos você quer a mais? '))

print(f'Progressão Aritmética finalizada com {total} termos mostrados.')
