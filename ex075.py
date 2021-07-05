numbers = (int(input('Digite um valor: ')),
             int(input('Digite um valor: ')),
             int(input('Digite um valor: ')),
             int(input('Digite o último valor: ')))

print('-=-' * 13)
print(f'\033[33mVocê digitou os valores {numbers}.\033[m')
print('-=-' * 13)

print(f'O número 9 aparece {numbers.count(9)} vezes.')

print(f'O número 3 aparece na {numbers.index(3)+1}ª posição.')

for n in numbers:

    if n % 2 == 0:
        print(f'O número par foi {n}.')
