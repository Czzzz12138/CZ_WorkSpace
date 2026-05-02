# python——os库
## 1. os库简介
os库是Python中一个非常重要的标准库，提供了丰富的函数来处理文件和目录的操作。它允许我们与操作系统进行交互，进行文件和目录的创建、删除、重命名、移动等操作，还可以获取文件和目录的属性信息。
## 2. os库常见用法
### 2.1 获取当前工作目录
```python
import os
current_directory = os.getcwd()
print(current_directory)
```
### 2.2 切换工作目录
```python
import os
os.chdir('/path/to/new/directory')
```
### 2.3 创建目录
```python
import os
os.mkdir('new_directory')
```
### 2.4 删除目录
```python
import os
os.rmdir('new_directory')
```

### 2.5 重命名文件或目录
```python
import os
os.rename('old_name.txt', 'new_name.txt')
```
### 2.6 删除文件
```python
import os
os.remove('file_to_delete.txt')
```
### 2.7 获取文件和目录的属性信息
```python
import os
file_info = os.stat('file.txt')
print(file_info)
```
### 2.8 列出目录中的文件和子目录
```python
import os
entries = os.listdir('.')
print(entries)
```
### 2.9 判断路径是否存在
```python
import os
if os.path.exists('file.txt'):
    print('文件存在')
else:
    print('文件不存在')
```
### 2.10 判断路径是文件还是目录
```python
import os
if os.path.isfile('file.txt'):
    print('这是一个文件')
elif os.path.isdir('directory'):
    print('这是一个目录')
else:
    print('路径不存在')
```
### 2.11 获取文件的绝对路径
```python
import os
absolute_path = os.path.abspath('file.txt')
print(absolute_path)
```
### 2.12 获取文件的大小
```python
import os
file_size = os.path.getsize('file.txt')
print(file_size)
```
### 2.13 获取文件的修改时间
```python
import os
modification_time = os.path.getmtime('file.txt')
print(modification_time)
```
### 2.14 获取文件的创建时间
```python
import os
creation_time = os.path.getctime('file.txt')
print(creation_time)
```
### 2.15 获取文件的访问时间
```python
import os
access_time = os.path.getatime('file.txt')
print(access_time)
```
### 2.16 递归创建目录
```python
import os
os.makedirs('parent_directory/child_directory')
```
### 2.17 递归删除目录
```python
import os
import shutil
shutil.rmtree('parent_directory')
```
### 2.18 递归列出目录中的所有文件和子目录
```python
import os
for root, dirs, files in os.walk('.'):
    print(root)  # 当前目录路径
    print(dirs)  # 当前目录下的子目录列表
    print(files)  # 当前目录下的文件列表
```
