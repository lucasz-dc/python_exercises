print('-=-' * 10)
print('     10 termos de uma PA')
print('-=-' * 10)

first_term = int(input('Primeiro termo: '))
reason = int(input('Razão: '))
tenth_term = first_term + (10 - 1) * reason

for c in range(first_term, tenth_term + reason, reason):
    print(c, end=' \033[33m-→\033[m ')

print('Fim!')
