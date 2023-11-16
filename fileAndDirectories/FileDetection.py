import os

path = '/home/pharsman/Desktop/file.txt'

if os.path.exists(path):
    print('That location exist!')
    if os.path.isfile(path):
        print("That is a File")
    elif os.path.isdir(path):
        print("That is a Directory")
else:
    print("That location doesn't exist!")
