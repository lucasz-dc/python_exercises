list = []
count = 0
while True:
    list.append([])
    list[count].append(str(input('Digite o nome do aluno: ')))
    list[count].append(float(input('Digite a primeira nota: ')))
    list[count].append(float(input('Digite a segunda nota: ')))

    average = (list[count][1] + list[count][2]) / 2
    list[count].append(average)

    parar = str(input('Deseja continuar? [S/N] '))

    if parar in 'Nn':
        break
    count += 1

print('-'*25)
print('Nº Nome          Média')
print('-'*25)

for position, student in enumerate(list):
    print(position, f'{student[0]:<15}', student[3])

while True:
    print('-' * 25)
    student = int(input('Deseja ver a nota de qual aluno? (999 para parar): '))

    if student == 999:
        break

    else:
        print(f'As notas de {list[student][0]} são {list[student][1:3]}')
print('Programa Finalizado\nVolte sempre!')
