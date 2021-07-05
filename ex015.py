k = float(input('Quantos km foram percorridos? '))
d = int(input('Por quantos dias o carro foi alugado? '))

p = 60 * d + 0.15 * k
print('Conforme os kilômetros e os dias percorridos, o total a pagar é de {:.2f} reais.'.format(p))
