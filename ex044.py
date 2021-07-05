preço = float(input('Qual é o preço do produto? '))

avd = preço - 10 / 100 * preço
avc = preço - 5 / 100 * preço
pcl = preço + 0.2 * preço

print('\033[1;33m-=-\033[m' * 25)
print('''Digite [ 1 ] para pagar à vista com dinheiro ou cheque (10% de desconto);
Digite [ 2 ] para pagar à vista no cartão (5% de desconto);
Digite [ 3 ] para pagar em até 2x no cartão (preço formal);
Digite [ 4 ] para pagar em 3x ou mais no cartão (20% de juros).''')
print('\033[1;33m-=-\033[m' * 25)

opçao = int(input('Escolha a forma de pagamento: '))

if opçao == 1:
    print('O valor final ficará R${:.2f}'.format(avd))

elif opçao == 2:
    print('O valor final ficará R${:.2f}'.format(avc))

elif opçao == 3:
    print('O valor final ficará R${:.2f}'.format(preço))

elif opçao == 4:
    ctao = int(input('Quantas parcelas? '))
    vm = pcl / ctao
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(ctao, vm))
    print('O valor final ficará R${:.2f}'.format(pcl))

else:
    print('Opção inválida.')
