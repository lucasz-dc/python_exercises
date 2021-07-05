from datetime import date

ano = int(input('Qual seu ano de nascimento? '))

atual = date.today().year
idade = atual - ano
print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Categoria: MIRIM.')

elif 9 < idade <= 14:
    print('Categoria: INFANTIL.')

elif 14 < idade <= 19:
    print('Categoria: JUNIOR.')

elif 19 < idade <= 25:
    print('Categoria: SÊNIOR.')

else:
    print('Categoria: MASTER.')
