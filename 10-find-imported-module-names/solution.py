def get_module_names(path):
    modules = []
    with open(path, 'r') as fileobj:
        for line in fileobj:
            if line.startswith('from'):
                # Get the module name only
                modules.append(line.split()[3])
            elif line.startswith('import'):
                # Get the module name only
                modules.append(line.split()[1])

    return modules

print(get_module_names('test_file.py'))