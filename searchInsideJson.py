import sys 
import os
import glob

# https://pynative.com/python-glob/

# see what if anything was passed in on the command line
# #######################################
# python3 readJson.py popcorn
# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))

search_word = 'event'
# if we have an arg passed use it to search for
if (len(sys.argv) > 1):
    search_word = str(sys.argv[1])

baseFolderFilter = "data"
fileFilter = "*"
extFilter = ".json"
currentPath = os.getcwd()
path = f'{currentPath}/{baseFolderFilter}/{fileFilter}{extFilter}'

print(f'search path (recursive) = {path}')

# # using glob to match every pathname
# #######################################
print(f'Files matching {fileFilter}{extFilter}')
print(f'Inside {currentPath}/{baseFolderFilter}')
# for an object to be used in a for loop the object must be a list (or iterable) 
# glob.glob returns a list of files 
for item in glob.iglob(path, recursive=True):
    print('\t' + item)

print(f'Searching for the word \'{search_word}\' in these files')
# list to store files that contain matching word
# #######################################
final_files = []
for file in glob.iglob(path, recursive=True):
    try:
        with open(file) as fp:
            # read the file as a string
            data = fp.read()
            if search_word in data:
                final_files.append(file)
                print('\t' + file)
    except:
        print('Exception while reading file')

print(f'{len(final_files)} file(s) found with search word => {search_word}')