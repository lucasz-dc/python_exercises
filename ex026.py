frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra A aparece {} vezes na frase acima.'.format(frase.count('A')))
print('A letra A aparece, pela primeira vez, na posição {}.'.format(frase.find('A')+1))
print('A letra A aparece, pela última vez, na posição {}.'.format(frase.rfind('A')+1))
