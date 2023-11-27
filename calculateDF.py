import pandas as pd
import math
import os

# 设置文档总数N的值
N = 3624  # 示例，你需要替换为实际的文档总数

# 指定文件夹和文件名模式
folder_path = 'output/TF_IDF_freq'
file_names = [f'output_2022_season{season}.csv' for season in range(3, 5)] + \
             [f'output_2023_season{season}.csv' for season in range(1, 5)]

# 遍历每个文件
for file_name in file_names:
    file_path = os.path.join(folder_path, file_name)
    
    # 读取CSV文件
    df = pd.read_csv(file_path)
    
    # 计算文档频率并添加到新列
    df.sort_values(by='TF_IFD', ascending=False, inplace=True)
    # 保存回CSV
    df.to_csv(file_path, index=False)

print("Document frequencies have been calculated and updated.")
