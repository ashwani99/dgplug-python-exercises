for number in range(1, 101):
    print(number)
    if number%3 == 0 and number%7 == 0:
        print('Scooby Doo')
    elif number%3 == 0:
        print('Scooby')
    elif number%7 == 0:
        print('Doo')