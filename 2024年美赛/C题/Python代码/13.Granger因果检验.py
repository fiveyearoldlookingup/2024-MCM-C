import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import grangercausalitytests
import seaborn as sns
import matplotlib.pyplot as plt

# 加载数据
file_path = 'E:\\桌面存储\\数学建模\\2024年美赛\\C题\\xlsx\\0.65 相减势头vsp1累计分数.xlsx'
df = pd.read_excel(file_path)

# 选取两个时间序列
data = df[['相减势头', 'point_victor']]

# 设置最大滞后阶数
max_lag = 7

# 执行Granger因果检验
granger_test_result = grangercausalitytests(data, max_lag, verbose=False)

# 提取p值
p_values = {lag: round(granger_test_result[lag][0]['ssr_chi2test'][1], 4) for lag in range(1, max_lag+1)}
# 提取Granger因果检验的p值
p_values = [granger_test_result[lag][0]['ssr_ftest'][1] for lag in range(1, max_lag+1)]

# 创建p值热图
plt.figure(figsize=(10, 6))
sns.heatmap([p_values], annot=True, xticklabels=list(range(1, max_lag+1)), yticklabels=['P Value'], cmap='coolwarm', cbar=True)
plt.title('Granger Causality Test P-Values')#格兰杰因果检验 P 值热图
plt.xlabel('Lags')
plt.tight_layout()
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为 SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
plt.show()
# 热力图只需要一个p值矩阵，这里我们创建一个大小为max_lag x max_lag的矩阵
p_matrix = np.zeros((max_lag, max_lag))

# 填充对角线以外的矩阵值
for i in range(max_lag):
    for j in range(max_lag):
        if i == j:
            p_matrix[i, j] = p_values[i+1]

# 绘制热力图
sns.heatmap(p_matrix, annot=True, cmap='coolwarm', cbar=True, 
            xticklabels=range(1, max_lag+1), yticklabels=range(1, max_lag+1))
plt.title('Granger Causality Test P-Values Heatmap')
plt.xlabel('Lag of X causing Y')
plt.ylabel('Lag of Y causing X')
plt.show()
