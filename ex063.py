print('-=-' * 12)
print('      Sequência de Fibonacci')
print('-=-' * 12)

total_terms = int(input('Quantos termos você quer mostrar? '))

t1 = 0
t2 = 1
print(f'{t1} \033[33m-→\033[m {t2}', end='')
counter = 3

while counter <= total_terms:
    t3 = t1 + t2
    print(f' \033[33m-→\033[m {t3}', end='')
    t1 = t2
    t2 = t3
    counter += 1

print(' \033[33m-→\033[m Fim.')
