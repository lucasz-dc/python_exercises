numbers_list = list()

while True:

    number = int(input(f'Digite um valor: '))

    if number not in numbers_list:
        numbers_list.append(number)
    else:
        print(f'Valor duplicado! Não vou adicionar...')

    answer = str(input(f'Quer continuar [S/N]? '))
    if answer in 'Nn':
        break

print('-=-' * 15)

numbers_list.sort()
print(f'Você digitou os valores {numbers_list}.')
