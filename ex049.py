n = int(input('Digite um número: '))

print('=' * 17)

for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n*c))
