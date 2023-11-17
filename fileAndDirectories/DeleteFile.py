import os
import shutil

# file_path = "./fileAndDirectories/deletefile.txt"
# dir_path = "./fileAndDirectories/Emptyfolder"
path = "./fileAndDirectories/folder"

try:
    # os.remove(file_path)
    # os.rmdir(path)
    shutil.rmtree(path)
except FileNotFoundError:
    print('That file was not found')
except PermissionError:
    print('You do not have permission to delete that')
except OSError:
    print('You cannot delete that using function')
else:
    print(path + " was deleted")
    