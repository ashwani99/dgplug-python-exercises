lines = """MemTotal:        7858500 kB
MemFree:          647000 kB
MemAvailable:    2487576 kB
Buffers:          244416 kB
"""

for line in lines.split('\n'):
    # Skip empty line
    if line == '':
        continue
    key, value = line.split(':')
    value = int(value.strip(' kB'))
    if key == 'MemTotal':
        total_memory = value // 1024
    elif key == 'MemFree':
        free_memory = value // 1024
    elif key == 'MemAvailable':
        available_memory = value // 1024

print('Total memory: {} MB'.format(total_memory))
print('Available memory: {} MB'.format(available_memory))
print('Free memory: {} MB'.format(free_memory))