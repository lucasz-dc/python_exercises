import random

a = str(input('Preimeiro aluno: '))
b = str(input('Segundo aluno: '))
c = str(input('Terceiro aluno: '))
d = str(input('Quarto aluno: '))

lista = (a, b, c, d)
escolha = random.choice(lista)

print('O aluno escolhido para limpar o quadro foi {}.'.format(escolha))
