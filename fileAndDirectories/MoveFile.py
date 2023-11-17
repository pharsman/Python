import os

source = "./fileAndDirectories/folder"
destination = "/home/pharsman/Desktop/folder"

try:
    if os.path.exists(destination):
        print('There is already file there')
    else:
        os.replace(source, destination)
        print(source + ' was moved')
except FileNotFoundError:
    print(source + " was not founf")