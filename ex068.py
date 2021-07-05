from random import randint
wins = 0

print('-' * 35)
print('     \033[1;33mVamos jogar Par ou Ímpar!\033[m')
print('-' * 35)

while True:

    value = int(input('Diga um valor: '))
    choice = ' '

    random = randint(0, 10)
    final_value = value + random

    while choice not in 'PI':
        choice = str(input('Par ou Ímpar (P/I)? ')).upper().strip()[0]

    print(f'Computador jogou {random}. Você jogou {value}.')
    print(f'\033[1;36m{random} + {value} = {final_value}\033[m.', end=' ')

    if choice == 'P':
        if final_value % 2 == 0:
            print('Deu par, \033[4mvocê venceu\033[m.')
            wins += 1
        else:
            print('Deu ímpar, \033[4mvocê perdeu\033[m.')
            break

    elif choice == 'I':
        if final_value % 2 != 0:
            print('Deu ímpar, \033[4mvocê venceu\033[m.')
            wins += 1
        else:
            print('Deu par, \033[4mvocê perdeu\033[m.')
            break

print(f'Game Over! Você venceu {wins} vezes.')
