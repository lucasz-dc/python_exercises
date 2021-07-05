numbers_list = []

bigger = 0
smaller = 0

for c in range(0, 5):
    numbers_list.append(int(input(f'Digite um valor para a posição {c}: ')))

    if c == 0:
        bigger = smaller = numbers_list[c]
    else:
        if numbers_list[c] > bigger:
            bigger = numbers_list[c]
        if numbers_list[c] < smaller:
            smaller = numbers_list[c]

print('-=-' * 18)
print(f'Você digitou os valores {numbers_list}.')

print(f'O maior valor digitado foi {bigger} nas posições ', end='')
for i, v in enumerate(numbers_list):
    if v == bigger:
        print(f'{i}... ', end='')
print()

print(f'O menor valor digitado foi {smaller} nas posições ', end='')
for i, v in enumerate(numbers_list):
    if v == smaller:
        print(f'{i}... ', end='')
