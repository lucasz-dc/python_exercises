average = counter = total_sum = highest_value = lower_value = 0
want_to_continue = 'Y'

while want_to_continue in 'Yy':
    type_number = int(input('Enter a number: '))
    total_sum += type_number
    counter += 1
    want_to_continue = str(input('\033[33m→\033[m Do you want to continue? (Y/N)? ')).upper().strip()[0]

    if counter == 1:
        highest_value = lower_value = type_number
    else:
        if type_number > highest_value:
            highest_value = type_number
        if type_number < lower_value:
            lower_value = type_number

average = total_sum / counter
print('-' * 44)
print(f'The highest value is {highest_value} and the lower is {lower_value}.')
print(f'The average of the {counter} values is {average:.2f}.')
