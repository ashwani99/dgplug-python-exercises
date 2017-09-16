"""Write a program to take the input from the user start and end. Then print the numbers between 
start to end (with end included) using while loop and infinite while loop."""

start = int(input('Enter start number: '))
end = int(input('Enter end number: '))

# While loop implementation
counter = start
print("While loop output------")
while(counter <= end):
    print(counter)
    counter = counter + 1
    
# Infinite while loop implementation
print("Infinite while loop output------")
counter = start
while True:
    print(counter)
    counter = counter + 1
    if(counter > end):
        break