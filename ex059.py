from time import sleep

first_value = int(input('Primeiro valor: '))
second_value = int(input('Segundo valor: '))
choice = 0

options_menu = '''          -----------------
Digite, de acordo com cada finalidade:
\033[1m[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] indicar o maior valor
[ 4 ] inserir novos valores
[ 5 ] sair do programa\033[m
          -----------------'''
print(options_menu)

while choice != 5:
    choice = int(input('Qual sua escolha? '))

    if choice == 1:
        print(f'{first_value} + {second_value} = {first_value + second_value}')

    elif choice == 2:
        print(f'{first_value} x {second_value} = {first_value * second_value}')

    elif choice == 3:
        if first_value > second_value:
            print(f'O maior valor entre {first_value} e {second_value} é {first_value}.')
        elif first_value == second_value:
            print('Os dois valores são iguais.')
        else:
            print(f'O maior valor entre {first_value} e {second_value} é {second_value}.')

    elif choice == 4:
        first_value = int(input('Insira o primeiro valor: '))
        second_value = int(input('Insira o segundo valor: '))
        print(options_menu)

        if choice == 1:
            print(f'{first_value} + {second_value} = {first_value + second_value}')

        elif choice == 2:
            print(f'{first_value} x {second_value} = {first_value * second_value}')

        elif choice == 3:
            if first_value > second_value:
                print(f'O maior valor entre {first_value} e {second_value} é {first_value}.')
            elif first_value == second_value:
                print('Os dois valores são iguais.')
            else:
                print(f'O maior valor entre {first_value} e {second_value} é {second_value}.')

    elif choice == 5:
        print('''          -----------------
Até logo!''')

    else:
        print('Opção inválida!')
        print('\033[33m---\033[m' * 13)

print('Encerrando programa...')
sleep(1)
