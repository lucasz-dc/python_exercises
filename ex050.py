soma = 0
cont = 0

for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c)))

    if n % 2 == 0:
        soma = soma + n
        cont += 1

print('{} valores pares. Soma = {}'.format(cont, soma))
