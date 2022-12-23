import glob
import re
import os

# https://pynative.com/python-glob/

fx = input('Enter the file search (case sensitive) ')
# [a-z] for any employee name
# {file_name} is the employee number
regex = r'{fileName}.*'.format(fileName=fx)
print('using this regEx')
print(regex)

baseFolderFilter = "data"
fileFilter = "*"
extFilter = "json"
currentPath = os.getcwd()
path = f'{currentPath}/{baseFolderFilter}/{fileFilter}.{extFilter}'

print(f'search path (recursive) = {path}')

# search folder
for file in glob.glob(path,recursive=True):
    print('\t file:', file)
    if re.search(regex, file):
        print('\t\t MATCH:', file)
    else:
        print('\t\t No match')