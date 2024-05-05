
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

# 指定中文字体为微软雅黑
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
matplotlib.rcParams['font.size'] = 10  # 可以调整字体大小

# 加载数据
data = pd.read_csv('E:\\桌面存储\\数学建模\\2024年美赛\\C题\\Wimbledon_featured_matches缺失值已处理.csv')#updated_data.csv#E:\\桌面存储\\数学建模\\2024年美赛\\C题\\Wimbledon_featured_matchescopy.csv
# 检查数据中的缺失值
missing_values = data.isnull()

# 绘制热力图
plt.figure(figsize=(18, 10)) # 增加图像大小
sns.heatmap(missing_values, cbar=False, yticklabels=False, cmap='viridis')

# 旋转横坐标标签
plt.xticks(rotation=90) # 旋转90度

# 调整字体大小
plt.tick_params(axis='x', labelsize=8) # 减小字体大小

# 选择性显示标签（例如每隔10个标签显示一个）
# plt.xticks(ticks=np.arange(0, len(data.columns), 10), labels=data.columns[::10])

# 调整子图间隔
plt.subplots_adjust(bottom=0.2) # 增加底部间隔

plt.title('Heat map of missing data')
plt.show()
