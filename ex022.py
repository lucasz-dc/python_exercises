nome = str(input('Digite seu nome: ')).strip()

print('Nome em maiúsculas: {}'.format(nome.upper()))
print('Nome em minúsculas: {}'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))

separa = nome.split()

print('Seu primeiro nome é {} e possui {} letras.'.format(separa[0], len(separa[0])))
