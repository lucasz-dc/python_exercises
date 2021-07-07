calculation = str(input('Digite a expressão numérica: '))
parentheses = []

for simbol in calculation:

    if simbol == '(':
        parentheses.append('(')

    elif simbol == ')':

        if len(parentheses) > 0:
            parentheses.pop()

        else:
            parentheses.append(')')
            break

if len(parentheses) == 0:
    print('Sua expressão está válida.')

else:
    print('Sua expressão está inválida.')
