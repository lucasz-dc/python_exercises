from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0

for c in range(1, 8):

    ano = int(input('Ano de nascimento da {}ª pessoa: '.format(c)))
    idade = atual - ano

    if idade >= 18:
        totmaior += 1

    else:
        totmenor += 1

print('Ao todo foram \033[1;36m{}\033[m maiores de idade e \033[1;36m{}\33[m menores de idade.'.format(totmaior, totmenor))
