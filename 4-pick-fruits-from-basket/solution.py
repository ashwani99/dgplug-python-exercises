"""Given a list basket = ["apple", "banana", "pineapple", "mango"] pick out the 
fruits whose name starts with a vowel."""

basket = ["apple", "banana", "pineapple", "mango"]

print('Fruits whose name start with a vowel are:')
for fruit in basket:
    if fruit[0] in ('a', 'e',  'i', 'o', 'u'):
        print(fruit)