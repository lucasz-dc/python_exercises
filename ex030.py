num = int(input('Digite um número: '))

res = num % 2
print('-=-' * 7)

if res == 0:
    print('O número {} é PAR!'.format(num))

if res == 1:
    print('O número {} é ÍMPAR!'.format(num))
print('-=-' * 7)
