n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

#if n1 > n2 > n3:
#    print('O maior valor é {}.'.format(n1))
#    print('O menor valor é {}.'.format(n3))
#if n1 > n3 > n2:
#    print('O maior valor é {}.'.format(n1))
#    print('O menor valor é {}.'.format(n2))
#if n2 > n3 > n1:
#    print('O maior valor é {}.'.format(n2))
#    print('O menor valor é {}.'.format(n1))
#if n2 > n1 > n3:
#    print('O maior valor é {}.'.format(n2))
#    print('O menor valor é {}.'.format(n3))
#if n3 > n2 > n1:
#    print('O maior valor é {}.'.format(n3))
#    print('O menor valor é {}.'.format(n1))
#if n3 > n1 > n2:
#    print('O maior valor é {}.'.format(n3))
#    print('O menor valor é {}.'.format(n2))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2

if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    n2 = maior

if n3 > n1 and n3 > n2:
    n3 = maior

print('O maior valor é {}.'.format(maior))
print('O menor valor é {}.'.format(menor))
