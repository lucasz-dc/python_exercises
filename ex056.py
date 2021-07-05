from time import sleep

somaidade = 0
mediaidade = 0
homemvelho = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print('\033[1;36m----- {}ª PESSOA -----\033[m'.format(p))

    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = str(input('Sexo (M/F): ')).strip()
    somaidade += i
    mediaidade = somaidade / 4

    if p == 1 and s in 'Mm':
        homemvelho = i
        nomevelho = n

    elif s in 'Mm' and i > homemvelho:
        homemvelho = i
        nomevelho = n

    elif s in 'Ff' and i < 20:
        totmulher20 += 1

print('''\033[1;36m---------------------
ANALISANDO DADOS...
---------------------\033[m''')
sleep(1)

print('A média de idade é de {:.1f} anos.'.format(mediaidade))
print('O homem mais velho é o {}, com {} anos de idade.'.format(nomevelho, homemvelho))
print('Há {} mulheres com menos de 20 anos.'.format(totmulher20))
