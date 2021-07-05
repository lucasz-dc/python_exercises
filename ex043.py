peso = float(input('Qual é o seu peso (kg)? '))
alt = float(input('Qual é a sua altura? '))

imc = peso / (alt ** 2)
print('Seu índice de massa corporal é de {:.2f}.'.format(imc))

if imc <= 18.5:
    print('Você está abaixo do peso ideal.')

elif 18.5 < imc <= 25:
    print('Você está com o peso ideal.')

elif 25 < imc <= 30:
    print('Você está com sobrepeso.')

elif 30 < imc <= 40:
    print('Você está com obesidade.')

else:
    print('Você está com obesidade mórbida.')
