import os
import shutil
'''
    txt文本文件中存储文件名，一行一个
    在source_dir文件夹中查找txt中有的文件
    复制到target_dir文件夹中
'''
# 设置源文件夹和目标文件夹
source_dir = ''  # 源文件夹
target_dir = ''  # 目标文件夹
txt_path = ''  # 存储文件名的txt文件
# 读取文件名列表
with open(txt_path, 'r') as f:
    file_list = f.read().splitlines()

# 遍历源文件夹，将匹配的文件复制到目标文件夹中
for file_name in os.listdir(source_dir):
    if file_name in file_list:
        print("copy: ", file_name)
        source_file = os.path.join(source_dir, file_name)
        target_file = os.path.join(target_dir, file_name)
        shutil.copyfile(source_file, target_file)
