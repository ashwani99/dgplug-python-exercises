"""Write a function when calling it, it will return a tuple:

- first value is the name of the distribution, 
- second value is the version id of the distribution."""

import re

# Without using regex
def get_distro_details_v1():
    with open('/etc/os-release', 'r') as file:
        for line in file:
            key, value = line.split('=')
            if key == 'NAME':
                distro_name = value.strip('"\n')
            elif key == 'VERSION_ID':
                version_id = value.strip('"\n')

    return distro_name, version_id


# Using regex
def get_distro_details_v2():
    with open('/etc/os-release', 'r') as file:
        file_content = file.read()
        distro_name = re.search(r'NAME="*(\w+)"*', file_content).group(1)
        version_id = re.search(r'VERSION_ID="*([.\w]+)"*', file_content).group(1)

    return distro_name, version_id


print(get_distro_details_v1())
print(get_distro_details_v2()) 