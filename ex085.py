pair = []
odd = []

value = 0
count = 0

while True:

    value = int(input(f'Digite o {count+1}º valor: '))
    count += 1

    if value % 2 == 0:
        pair.append(value)

    else:
        odd.append(value)

    if count == 7:
        break

print('-=-' * 15)

pair.sort()
odd.sort()

print(f'Os valores pares foram: {pair}.')
print(f'Os valores ímpares foram: {odd}.')
