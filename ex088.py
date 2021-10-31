from random import randint
from time import sleep

roster = list()
games = list()

print('-' * 30)
print('      JOGA NA MEGA SENA      ')
print('-' * 30)

amount = int(input('Quantos jogos você quer que eu sorteie? '))

total = 1

while total <= amount:

    count = 0

    while True:
        number = randint(1, 60)

        if number not in roster:
            roster.append(number)
            count += 1

        if count >= 6:
            break

    roster.sort()
    games.append(roster[:])
    roster.clear()

    total += 1

print('-=' * 3, f'Sorteando {amount} jogos...', '-=' * 3)

sleep(1)

for i, l in enumerate(games):

    print(f'Jogo {i + 1}: {l}')
    sleep(1)

print('-=' * 5, '< Boa sorte! >', '-=' * 5)
