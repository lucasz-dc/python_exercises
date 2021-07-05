casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você vai pagar? '))

prest = casa / (anos * 12)
minimo = 30 * salario / 100

print('Para financiar essa casa de R${:.2f} em {} anos, a parcela será de R${:.2f}.'.format(casa, anos, prest))

if prest <= minimo:
    print('Empréstimo CONCEDIDO!')

else:
    print('Empréstimo NEGADO!')
