nom = str(input('Digite seu nome completo: ')).strip()

n = nom.split()

print('Primeiro nome: {}'.format(n[0]))
print('Último nome: {}'.format(n[len(n)-1]))
