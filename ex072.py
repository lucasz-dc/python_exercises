counter = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:

    number = int(input('Digite um número entre 0 e 20: '))

    if 0 <= number <= 20:
        break

    print('Número inválido. ', end='')

print(f'Você digitou o número {counter[number]}.')
