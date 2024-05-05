import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
import matplotlib

# 加载数据
file_path = 'E:\\桌面存储\\数学建模\\2024年美赛\\C题\\xlsx\\0.65 相减势头vsp1累计分数.xlsx'
df = pd.read_excel(file_path)
# 指定中文字体为微软雅黑
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
matplotlib.rcParams['font.size'] = 10  # 可以调整字体大小
# 选择“相减势头”的时间序列数据
ts = df['相减势头']

# 绘制ACF图
plt.figure(figsize=(14, 7))
plot_acf(ts, lags=20, alpha=0.05)
plt.title('Autocorrelation Function (ACF) for 相减势头')
plt.show()

# 绘制PACF图
plt.figure(figsize=(14, 7))
plot_pacf(ts, lags=20, alpha=0.05, method='ywm')
plt.title('Partial Autocorrelation Function (PACF) for 相减势头')
plt.show()
