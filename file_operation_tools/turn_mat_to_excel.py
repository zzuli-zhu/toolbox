"""
    将mat文件转换为excel文件
"""


import scipy.io
import pandas as pd

mat_path = ''
excel_path = ''
excel_name = ''
excel_name += '.xlsx'

# 加载mat文件
mat_data = scipy.io.loadmat(mat_path)

# 获取变量名和值
variable_names = [n for n in mat_data.keys() if not n.startswith('__')]
variable_values = [mat_data[n] for n in variable_names]

# 创建pandas dataframe
df = pd.DataFrame({'Variable Name': variable_names, 'Variable Value': variable_values})

# 将数据保存到Excel文件
writer = pd.ExcelWriter(excel_path+excel_name)
df.to_excel(writer, 'Sheet1', index=False)
writer.save()
