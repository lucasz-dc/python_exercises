print('-=-' * 10)
print('     10 termos de uma PA')
print('-=-' * 10)

first_term = int(input('Primeiro termo: '))
reason = int(input('Razão: '))
term = first_term
counter = 1

while counter <= 10:
    print(f'{term} \033[33m-→\033[m ', end='')
    term += reason
    counter += 1

print('Fim!')
