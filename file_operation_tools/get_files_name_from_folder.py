import os
"""
    获取一个文件夹中所有文件的名字
    存储在txt文件当中，一行一个
"""
# 设置要遍历的文件夹路径和要保存文件名的 .txt 文件路径
folder_path = ''
txt_file_path = ''

# 遍历文件夹，获取所有文件名
file_names = []
for filename in os.listdir(folder_path):
    # 排除文件夹和隐藏文件
    if not filename.startswith('.') and not os.path.isdir(os.path.join(folder_path, filename)):
        file_names.append(filename)

# 将文件名写入 .txt 文件
with open(txt_file_path, 'w') as f:
    for filename in file_names:
        f.write(filename + '\n')
