# python-copy

```python
import os
import shutil

root_src_dir = os.path.join('.', 'C:\\Users\\agupta78\\Desktop\\folder1')
root_target_dir = os.path.join(
    '.', 'C:\\Users\\agupta78\\Desktop\\folder1\\Archive')

operation = 'copy'  # 'copy' or 'move'

for src_dir, dirs, files in os.walk(root_src_dir):
    dst_dir = src_dir.replace(root_src_dir, root_target_dir)
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst_dir, file_)
        if os.path.exists(dst_file):
            os.remove(dst_file)
        if operation is 'copy':
            shutil.copy(src_file, dst_dir)
        elif operation is 'move':
            shutil.move(src_file, dst_dir)
```
