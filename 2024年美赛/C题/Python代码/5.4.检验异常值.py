import pandas as pd
import matplotlib.pyplot as plt

# 读取数据集
data = pd.read_csv('E:\\桌面存储\\数学建模\\2024年美赛\\C题\\Wimbledon_featured_matchescopy.csv')

# 指定有效值的集合
valid_values = {0,15, 30, 40, 50}

# 检测不在有效值集合中的异常值
data['is_outlier'] = ~data['p1_score'].isin(valid_values)

# 可视化异常值
plt.figure(figsize=(10, 6))

# 绘制所有值的散点图
plt.scatter(data.index, data['p1_score'], label='All data', color='blue')

# 突出显示异常值
outliers = data[data['is_outlier']]
plt.scatter(outliers.index, outliers['p1_score'], label='Outliers', color='red')

# 设置图例和标题
plt.legend()
plt.title('Outliers in p1_score')
plt.xlabel('Index')
plt.ylabel('p1_score')

# 显示图形
plt.show()

# 打印异常值的信息
print("Detected outliers:")
print(outliers)
