print('-' * 35)
print('         Lista de compras')
print('-' * 35)

total_cost = cost_1000 = cheap_product = counter_product = 0
name_cheap = ' '

while True:
    product_name = str(input('Nome do produto: '))
    product_cost = float(input('Preço do produto: R$'))
    counter_product += 1

    if counter_product == 1:
        cheap_product = product_cost
        name_cheap = product_name
    else:
        if product_cost < cheap_product:
            cheap_product = product_cost
            name_cheap = product_name

    total_cost += product_cost

    if product_cost > 1000:
        cost_1000 += 1

    want_to_continue = ' '
    while want_to_continue not in 'SN':
        want_to_continue = str(input('Quer continuar? ')).strip().upper()[0]
    if want_to_continue == 'N':
        break

    print('-' * 35)

print('-' * 35)
print(f'Total gasto = R${total_cost:.2f}')
print(f'{cost_1000} produtos custaram mais de R$1000.00')
print(f'{name_cheap} é o produto mais barato, custando R${cheap_product:.2f}')
