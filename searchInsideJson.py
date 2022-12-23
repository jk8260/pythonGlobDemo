import sys 
import os
import glob

# https://docs.python.org/3.9/library/glob.html#module-glob

# see what if anything was passed in on the command line
# #######################################
# python3 readJson.py popcorn

# this will show the command line args
# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))

search_word = 'event'
# if we have an arg passed use it to search for
if (len(sys.argv) > 1):
    search_word = str(sys.argv[1])


#searchroot = "../../.." 
currentPath = os.getcwd()
dataFolderFilter = "data"
searchroot = f'{currentPath}/{dataFolderFilter}'
fileFilter = "*"
extFilter = "json"
searchFilePatern = f'{fileFilter}.{extFilter}'

#searchpath = f'{currentPath}/{baseFolderFilter}/{searchFilePatern}'
searchpath = f'{searchroot}/{searchFilePatern}'

print(f'CurrentPath = {currentPath}')
print(f'search path (relative to currentPath) = {searchpath}')

# # using iglob to match every pathname
# #######################################
print(f'Files matching {searchFilePatern}')
print(f'Inside {searchpath}')

# for an object to be used in a for loop the object must be a list (or iterable) 
# glob.glob Returns a list of files which can get huge
# glob.iglob Returns an iterator which yields the same values as glob() 
# without actually storing them all simultaneously

for item in glob.iglob(searchpath, recursive=True):
    print('\t' + item)

print(f'Searching for the word \'{search_word}\' in the above listed files')
# list to store files that contain matching word
# #######################################
finalFiles = []
for file in glob.iglob(searchpath, recursive=True):
    try:
        with open(file) as fp:
            # read the file as a string
            data = fp.read()
            if search_word in data:
                finalFiles.append(file)
                print('\t' + file)
    except:
        print('Exception while reading file')

print(f'{len(finalFiles)} file(s) found with search word => {search_word}')