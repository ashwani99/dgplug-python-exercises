number_1 = float(input('Enter first number: '))
number_2 = float(input('Enter second number: '))
operation = input('Choose an operation to perform (+, -, /, *): ')

if operation == '+':
    result = number_1 + number_2
elif operation == '-':
    result = number_1 - number_2
elif operation == '/':
    result = number_1 / number_2
elif operation == '*':
    result = number_1 * number_2
else:
    print('Invalid operation.')
    exit()

print('Result: {}'.format(result))