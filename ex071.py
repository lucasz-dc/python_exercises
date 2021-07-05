print('-' * 30)
print('{:^30}'.format('Banco CEV'))
print('-' * 30)

value = int(input('Valor a ser sacado: R$'))

total = value
money = 50
money_counter = 0

while True:
    if total >= money:
        total -= money
        money_counter += 1

    else:

        if money_counter > 0:
            print(f'Total de {money_counter} cédulas de R${money:.2f}')

        if money == 50:
            money = 20
        elif money == 20:
            money = 10
        elif money == 10:
            money = 1
        money_counter = 0

        if total == 0:
            break

print('-' * 30)
