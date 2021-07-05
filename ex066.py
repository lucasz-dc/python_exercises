type_number = counter = sum = 0

while True:
    sum += type_number
    counter += 1
    type_number = int(input('Digite um número (999 para encerrar): '))
    if type_number == 999:
        break

print(f'Você digitou {counter - 1} números, que juntos somam {sum}.')
