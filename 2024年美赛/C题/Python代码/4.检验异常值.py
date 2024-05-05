import pandas as pd
import matplotlib.pyplot as plt

# 读取数据集
# 请将'path_to_your_data.csv'替换成您数据集的实际路径
data = pd.read_csv('E:\\桌面存储\\数学建模\\2024年美赛\\C题\\Wimbledon_featured_matchescopy.csv')

# 选择您想要检测异常值的列
# 这里假设我们检测名为'feature_to_check'的特征列
feature_to_check = 'p1_score'

# 箱线图
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.boxplot(data[feature_to_check].dropna())  # 确保去除NaN值
plt.title('Box Plot of ' + feature_to_check)

# 计算IQR分数来识别异常值
Q1 = data[feature_to_check].quantile(0.25)
Q3 = data[feature_to_check].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# 散点图
plt.subplot(1, 2, 2)
plt.scatter(x=data.index, y=data[feature_to_check], color='blue')
plt.axhline(y=lower_bound, color='r', linestyle='--', label='Lower Bound')
plt.axhline(y=upper_bound, color='r', linestyle='--', label='Upper Bound')
plt.title('Scatter Plot with Outliers for ' + feature_to_check)
plt.legend()

# 显示图形
plt.tight_layout()
plt.show()

# 打印异常值
outliers = data[(data[feature_to_check] < lower_bound) | (data[feature_to_check] > upper_bound)]
print("Detected outliers:")
print(outliers)
