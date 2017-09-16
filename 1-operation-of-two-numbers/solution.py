"""Write a program to take input from user two numbers, number1 and number2 
and preferred operation ( +, -, /, * ). Calculate and print the result of the operation.
"""

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