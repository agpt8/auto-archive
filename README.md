# python-copy

This readme is used as a test and trial ground for the code below. Rough code is added/deleted as required. Kindly refer to below mentioned file proper code.

Go to backup.py for a much refined version of the code below

```python
from datetime import datetime
from os import mkdir, path, remove, walk
from shutil import copy2, move
from time import strftime

root_src_dir = path.join('', r'C:\Users\agupta78\Desktop\folder1')
root_dst_dir = path.join('', r'C:\Users\agupta78\Desktop\folder2')

operation = 'copy'  # 'copy' or 'move'

for src_dir, dirs, files in walk(root_src_dir):
    dst_dir = src_dir.replace(root_src_dir, root_dst_dir)
    if not path.exists(dst_dir):
        mkdir(dst_dir)
    for file_ in files:
        src_file = path.join(src_dir, file_)
        dst_file = path.join(dst_dir, file_)
        if path.exists(dst_file):
            remove(dst_file)
        if operation is 'copy':
            copy2(src_file, dst_dir)
        elif operation is 'move':
            move(src_file, dst_dir)

current_date = str(datetime.now().strftime('%d_%m_%Y'))
print(current_date)

files_list = listdir(root_dst_dir)
print(files_list)
chdir(root_dst_dir)
for file_name in files_list:
    rename(file_name, file_name + current_date)

# for dst_file in walk(dst_dir):
#     file_time = str(datetime.now().strftime('%d_%m_%Y'))
#     # tupe_to_string = ''.join(dst_file)
#     full_path = path.join(
#         path.abspath(fsdecode(dst_file)), sep, file_time)


# def replace(folder_path, old, new):
#     for path, subdirs, files in os.walk(folder_path):
#         for name in files:
#             if(old.lower() in name.lower()):
#                 file_path = os.path.join(path,name)
#                 new_name = os.path.join(path,name.lower().replace(old,new))
#                 os.rename(file_path, new_name)
```


```python
from datetime import datetime
import os

file_path = <PASS YOUR FILE HERE>

csv_file = 'myfile_' + str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.csv'

csv_file_full = os.path.join(file_path, os.sep, csv_file)
```

```python
import time
timestr = time.strftime("_%d_%m_%Y")
print(timestr)
```

```python
#%%
from datetime import datetime
import os
import time
from os import mkdir, path, remove, walk
import os 
  
# Function to rename multiple files 

root_src_dir = path.join('', r'C:\Users\JoshiChi\Desktop\folder1') 
i = 0
timestr = time.strftime("_%d_%m_%Y")
print(timestr)
    
for filename in os.listdir(root_src_dir): 
    dst = str(i) + timestr + ".txt"
    src =root_src_dir+ '\\'+ filename 
    dst =root_src_dir+'\\'+ dst 
        
    # rename() function will 
    # rename all the files 
    os.rename(src, dst) 
    i += 1
  

#csv_file = 'myfile_' + str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.csv'

#sv_file_full = os.path.join(file_path, os.sep, csv_file)
#%%
```
