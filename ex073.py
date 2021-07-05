teams = ('Corinthians', 'Palmeiras', 'Santos','Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport', 'Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-go')

counter = 0

print('-=-' * 30)
print('A tabela do Brasileirão é:')
print('-=-' * 30)

for t in teams:
    counter += 1
    print(counter,'-', t)

print('-=-' * 30)
print(f'5 primeiros colocados: {teams[0:5]}')

print('-=-' * 30)
print(f'Últimos 4 colocados: {teams[-4:]}')

print('-=-' * 30)
print(f'Ordem alfabética: {sorted(teams)}')

print('-=-' * 30)
print(f'A Chapecoense está na {teams.index("Chapecoense")}ª posição.')
