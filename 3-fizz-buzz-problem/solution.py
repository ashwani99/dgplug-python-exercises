"""The problem is called "Scooby Doo". Print numbers from 1 to 100 and for every number which is 
multiple of 3 print Scooby, for number multiple of 7 print Doo and for 3 and 7 print Scooby Doo."""

for number in range(1, 101):
    print(number)
    if number%3 == 0 and number%7 == 0:
        print('Scooby Doo')
    elif number%3 == 0:
        print('Scooby')
    elif number%7 == 0:
        print('Doo')