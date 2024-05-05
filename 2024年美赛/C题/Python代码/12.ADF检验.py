import pandas as pd
from statsmodels.tsa.stattools import adfuller

# 加载数据
# 请将下面的路径替换为您的实际文件路径
file_path = 'E:\\桌面存储\\数学建模\\2024年美赛\\C题\\xlsx\\0.65 相减势头vsp1累计分数.xlsx'
df = pd.read_excel(file_path)

# 选择您需要进行ADF检验的列
# 这里以'相减势头'和'p1_points_won'为例
column1 = '相减势头'
column2 = 'p1_points_won'
#column2 = 'point_victor'

# 进行ADF检验
adf_test_result1 = adfuller(df[column1])
adf_test_result2 = adfuller(df[column2])

# 打印结果
print(f'ADF检验结果 - {column1}:')
print(f'ADF Statistic: {adf_test_result1[0]}')
print(f'p-value: {adf_test_result1[1]}')
print(f'Critical Values:')
for key, value in adf_test_result1[4].items():
    print(f'\t{key}: {value}')

print(f'\nADF检验结果 - {column2}:')
print(f'ADF Statistic: {adf_test_result2[0]}')
print(f'p-value: {adf_test_result2[1]}')
print(f'Critical Values:')
for key, value in adf_test_result2[4].items():
    print(f'\t{key}: {value}')
