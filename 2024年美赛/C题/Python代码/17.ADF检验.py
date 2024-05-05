import pandas as pd
from statsmodels.tsa.stattools import adfuller

# 读取Excel文件
file_path = r"C:\Users\35274\Desktop\第三题的相关分析的数据.xlsx"
output_file_path = r"C:\Users\35274\Desktop\差分后的数据(xin).xlsx"  # 设置输出文件路径
df = pd.read_excel(file_path)

# 提取 "match_momentum" 特征的数据列
data = df["Subtractive momentum_won"]

# 初始ADF检验
result = adfuller(data)
adf_statistic = result[0]
p_value = result[1]
print(f"初始ADF检验统计量：{adf_statistic}")
print(f"初始ADF检验P值：{p_value}")

# 设置阈值，通常选择0.05
threshold = 0.05

# 迭代差分直到通过ADF检验
d = 0
while p_value > threshold:
    d += 1
    differenced_data = data.diff(periods=1).dropna()
    result = adfuller(differenced_data)
    adf_statistic = result[0]
    p_value = result[1]
    print(f"第{d}次差分后的ADF检验统计量：{adf_statistic}")
    print(f"第{d}次差分后的ADF检验P值：{p_value}")

print(f"经过{d}次差分后，通过ADF检验。")

# 保存差分后的数据到新的Excel文件
df["differenced_data"] = differenced_data  # 添加差分后的列
df.to_excel(output_file_path, index=False)  # 保存到Excel文件

print(f"差分后的数据已保存到 {output_file_path}")
