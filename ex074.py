from random import randint
from time import sleep

random_numbers = (randint(0, 10), randint(0, 10), randint(0, 10),
                  randint(0, 10), randint(0, 10))

print(f'Os 5 números sorteados são: ', end='')

for n in random_numbers:
    print(n, end=' ')

sleep(2)

print(f'\nO maior valor é {max(random_numbers)}.')
print(f'O menor valor é {min(random_numbers)}.')
