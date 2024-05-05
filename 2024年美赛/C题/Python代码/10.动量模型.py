import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 替换为你的Excel文件路径
file_path = 'E:\\桌面存储\\数学建模\\2024年美赛\\C题\\第四题\\乒乓球\\第四题M(t)需要的数据player2.xlsx'

# 读取Excel文件
data = pd.read_excel(file_path)
for column in data.columns:
    column_type = data[column].dtype
    print(f"Column '{column}' has data type: {column_type}")

# 检查y8列是否有'#DIV/0!'，并替换为NaN（根据实际情况调整列名）
# Excel中的错误可能已经是NaN了，如果不是，使用下面的代码将其替换
data['y8'] = data['y8'].replace('#DIV/0!', np.nan)

# 确保'y8'列的数据类型正确，如果'y8'原本是字符串类型的，需要转换为数值类型
data['y8'] = pd.to_numeric(data['y8'], errors='coerce')

# 对于每个match_id分组，计算y8的均值，并用该均值填充同一组内的NaN值
data['y8'] = data.groupby('match_id')['y8'].transform(lambda x: x.fillna(x.mean()))

# 检查结果
print(data.head())

# 如果需要将结果保存回Excel文件
data.to_excel('E:\\桌面存储\\数学建模\\2024年美赛\\C题\\第四题\\乒乓球\\处理后的数据player2.xlsx')
########################################################
# 替换为你的Excel文件路径
file_path = 'E:\\桌面存储\\数学建模\\2024年美赛\\C题\\第四题\\乒乓球\\处理后的数据player2.xlsx'

# 读取Excel文件
data = pd.read_excel(file_path)

# 筛选match_id为2023-wimbledon-1701的数据
filtered_data = data[data['match_id'] == '2023-wimbledon-1309']
# 确保数据按照某个顺序排序，比如按照游戏编号或回合数，这里假设按照'id'排序
filtered_data = filtered_data.sort_values(by='id')

# 定义权重
w = {
    'w1': -0.05058023,  
    'w2': 0.064491906,  
    'w3': 0.145191184,  
    'w4': -0.12017652,
    'w5': -0.072913153,
    'w6': 0.093314621,
    'w7': 0.166185537,
    'w8': 0.031763456,
    'w9': 0.058730213,
    'w10': 0.027298233,
    'w11': 0.106738168,
    'w12': 0.062679284
}

# 计算x(t)
filtered_data['x(t)'] = sum(filtered_data[f'y{i}'] * w[f'w{i}'] for i in range(1, 13))

# 显示计算结果的前几行
print(filtered_data.head())

# 如果需要将结果保存回Excel文件
#filtered_data.to_excel('E:\\桌面存储\\数学建模\\2024年美赛\\C题\\计算结果.xlsx')
# 设置平滑系数a
a = 0.65 # 示例值，实际应用中需要根据具体情况调整

# 初始化M(t)，此时不预先填充任何值
M_t = []

# 遍历filtered_data来计算每个M(t)
for i in range(len(filtered_data)):
    x_t = filtered_data.iloc[i]['x(t)']  # 获取当前的x(t)
    if i == 0:
        # 对于i=0，即t=1的情况，M(0)被认为是0
        M_new = a * x_t
    else:
        # 对于i>0的情况，使用上一个M(t-1)的值进行计算
        M_new = a * x_t + (1 - a) * M_t[i-1]
    M_t.append(M_new)

# 将计算出的M(t)值添加到filtered_data DataFrame中
filtered_data['M(t)'] = M_t

# 显示计算结果的前几行，包括x(t)和M(t)
print(filtered_data[['x(t)', 'M(t)']].head())

# 如果需要将结果保存回Excel文件
filtered_data.to_excel('E:\\桌面存储\\数学建模\\2024年美赛\\C题\\第四题\\乒乓球\\计算结果含M(t) player2 λ=0.65.xlsx')
import pandas as pd
import matplotlib.pyplot as plt

# 替换为您的Excel文件路径
file_path = 'E:\\桌面存储\\数学建模\\2024年美赛\\C题\\第四题\\乒乓球\\计算结果含M(t) player2 λ=0.65.xlsx'

# 读取Excel文件
data = pd.read_excel(file_path)

# 选择并处理数据
# 此处假设已经完成了M(t)的计算并将结果存储在filtered_data中
# 示例代码省略了这一部分，请参照之前的步骤完成M(t)的计算

# 假设filtered_data已经正确准备好了，包含了M(t)的计算结果
# 下面直接展示如何绘制M(t)和y12

# 设置图形大小
plt.figure(figsize=(10, 6))

# 绘制M(t)的折线图
plt.plot(data.index, data['M(t)'], label='M(t)', marker='o')  # 确保data变量已包含M(t)

# 绘制y12的折线图
plt.plot(data.index, data['y12'], label='score_rate', marker='x')

# 添加图例
plt.legend()

# 设置横纵坐标的标签
plt.xlabel('t')
plt.ylabel('Values')

# 设置图形的标题
plt.title('player2 M(t) and score_rate over time λ=0.65')

# 显示图形
plt.show()
