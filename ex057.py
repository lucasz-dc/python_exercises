s = str(input('Informe seu sexo: ')).strip().upper()[0]

while s not in 'MmFf':
    s = str(input('Comando inválido. Informe seu sexo novamente: '))

    if s in 'Mm':
        print('Sexo masculino registrado com sucesso!')

    elif s in 'Ff':
        print('Sexo feminino registrado com sucesso!')
