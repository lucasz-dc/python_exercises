num = int(input('Digite um valor: '))

print('''Escolha uma das bases para conversão:)
[ 1 ] para BINÁRIO
[ 2 ] para OCTAL
[ 3 ] para HEXADECIMAL''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para binário é {}'.format(num, bin(num)))

elif opcao == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)))

elif opcao == 3:
    print('{} convertido para hex é {}'.format(num, hex(num)))

else:
    print('Opção inválida.')
