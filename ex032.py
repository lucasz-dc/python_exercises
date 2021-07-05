from datetime import date

ano = int(input('Qual ano você quer analisar? (Digie 0 se deseja pesquisar o ano atual). '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} É BISSEXTO!'.format(ano))
else:
    print('O ano de {} NÃO É BISSEXTO!'.format(ano))
