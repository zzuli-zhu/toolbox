
"""
    读取图像通道数量 
"""


from PIL import Image

# 打开图像文件
img = Image.open("D:\\1毕业设计\\code_resource\\data_set\\Significance_Target\\EORSSD_reshape\\train_labels\\0001.png")

# 获取图像的通道数
channels = img.getbands()

# 输出图像的通道数
print("通道数：", channels)
