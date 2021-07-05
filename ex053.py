frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

#inverso = ''
#for letra in range(len(junto) -1, -1, -1):
#    inverso += junto[letra]

print('Você digitou a frase {} que é {} ao contrário.'.format(junto, inverso))

if inverso == junto:
    print('É palíndromo!')

else:
    print('Não é palíndromo!')
