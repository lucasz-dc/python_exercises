from datetime import date

atual = date.today().year
ano = int(input('Em qual ano voê nasceu? '))

idade = atual - ano

if idade > 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
    x = atual - (ano + 18)
    print('Você já deveria ter se alistado há {} anos.'.format(x))

elif idade == 18:
    print('Você tem 18 anos.')
    print('Agora é sua hora de se alistar!')

else:
    y = ano + 18 - atual
    z = ano + 18
    print('Ainda faltam {} ano(s) para seu alistamento.'.format(y))
    print('Em {} o dever lhe chama!'.format(z))

