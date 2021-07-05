print('- ' * 15)
print('     Cadastro de pessoas.')
print('- ' * 15)

age_counter = 0
man_counter = 0
woman_counter = 0

while True:

    age = int(input('Idade: '))

    sex = ' '
    while sex not in 'MF':
        sex = str(input(('Sexo (M/F): '))).strip().upper()[0]

    if age >= 18:
        age_counter += 1
    if sex == 'M':
        man_counter += 1
    if sex == 'F' and age < 20:
        woman_counter += 1

    want_to_continue = ' '
    while want_to_continue not in 'SN':
        want_to_continue = str(input('Quer continuar (S/N)? ')).strip().upper()[0]
    if want_to_continue == 'N':
        break

    print('- ' * 15)

print('- ' * 15)
print(f'{age_counter} pessoas têm mais de 18 anos.')
print(f'{man_counter} homens foram cadastrados.')
print(f'{woman_counter} mulheres têm menos de 20 anos.')
