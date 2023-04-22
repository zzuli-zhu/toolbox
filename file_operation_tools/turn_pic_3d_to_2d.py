"""
    将一个文件夹的图片全部转换为灰度图(三维转二维)
"""

import os
from PIL import Image

# 定义输入和输出文件夹路径
input_dir = ''
output_dir = ''

# 创建输出文件夹
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print("开始转换")

# 遍历输入文件夹中的所有图像文件
for filename in os.listdir(input_dir):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        # 加载图像
        img = Image.open(os.path.join(input_dir, filename))

        # 将图像转换为灰度图像
        gray_img = img.convert('L')
        print("正在转换：", filename)
        # 保存图像到输出文件夹
        gray_img.save(os.path.join(output_dir, filename))


print("转换结束")
