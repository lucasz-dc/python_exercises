import random
from time import sleep

comput = random.randint(0, 5)

print('\033[31m-=-\033[m' * 18)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('\033[36m-=-\033[m' * 18)

n = int(input('Em qual número eu pensei? '))
print('Processando...')
sleep(1)

if n == comput:
    print('\033[7;32m Pensei no número {}. Você acertou! \033[m'.format(comput))
else:
    print('\033[7;31m Pensei no número {}. Você errou! \033[m'.format(comput))
