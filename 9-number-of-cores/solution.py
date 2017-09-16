"""Write a function which will tell us the number of cores in your computer."""

def get_number_of_cores():
    cores = 0
    with open('/proc/cpuinfo') as fileobj:
        text = fileobj.read()
        # Get the number of virtual cores 
        cores = text.count('processor')
    return cores

print(get_number_of_cores())