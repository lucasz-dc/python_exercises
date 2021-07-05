numbers_list = []

for c in range(0, 5):
    number = int(input('Digite um valor: '))

    if c == 0 or number > numbers_list[-1]:
        numbers_list.append(number)
        print('Adicionado ao final da lista...')

    else:
        position = 0
        while position < len(numbers_list):
            if number <= numbers_list[position]:
                numbers_list.insert(position, number)
                print(f'Adicionado na posição {position}.')
                break
            position += 1

print('-=-' * 22)
print(f'Os valores digitados, em ordem crescente, foram {numbers_list}.')
