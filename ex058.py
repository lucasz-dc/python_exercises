import random
from time import sleep

random_number = random.randint(0, 10)
counter = 1

print('\033[31m-=-\033[m' * 18)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar!')
print('\033[36m-=-\033[m' * 18)
n = int(input('Em qual número eu pensei? '))

while n != random_number:
    n = int(input('Você errou, tente novamente: '))
    counter += 1
if n == random_number:
    print(f'Você acertou na {counter}ª tentativa.')
elif n < random_number:
    n = int(input('Mais... tente novamente: '))
elif n > random_number:
    n = int(input('Menos... Tente novamente: '))
