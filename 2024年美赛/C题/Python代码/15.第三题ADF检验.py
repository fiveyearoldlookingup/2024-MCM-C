import pandas as pd

# 加载Excel文件
file_path = 'C:\\Users\\35274\\Desktop\\第三题的相关分析的数据.xlsx'
df = pd.read_excel(file_path)
from statsmodels.tsa.stattools import adfuller

# 对每个特征进行ADF检验
adf_results = {}
for column in df.columns:
    result = adfuller(df[column].dropna())
    adf_results[column] = result[1]  # result[1]是p-value
# 已经导入 pandas 和 adfuller

# 一阶差分并重新进行ADF检验
for column in df.columns:
    if adf_results[column] > 0.05:  # 假设使用0.05作为显著性水平
        # 进行一阶差分
        diff_series = df[column].diff().dropna()  # 计算一阶差分并去除NaN值
        
        # 对一阶差分后的序列进行ADF检验
        result_diff = adfuller(diff_series)
        adf_results[column] = (result_diff[1], 'diff')  # 更新结果字典，包括差分后的p-value
        
# 打印更新后的ADF检验结果
for column, (p_value, status) in adf_results.items():
    if status == 'diff':
        print(f"{column}: 差分后的p值 = {p_value}")
    else:
        print(f"{column}: 原始p值 = {p_value}")

from statsmodels.tsa.stattools import grangercausalitytests
import pandas as pd

# 设置滞后项的最大数量
max_lag = 12  # 例如，考虑到4期的滞后

# 初始化字典来存储结果
granger_p_values = {column: [] for column in df.columns if column != 'match_momentum'}

# 对每个特征进行Granger因果检验
for column in granger_p_values.keys():
    test_data = df[['match_momentum', column]].dropna()
    if len(test_data) > max_lag:  # 确保有足够的数据进行检验
        for lag in range(1, max_lag + 1):
            test_result = grangercausalitytests(test_data, maxlag=lag, verbose=False)
            p_value = test_result[lag][0]['ssr_chi2test'][1]  # 获取当前滞后项的p-value
            granger_p_values[column].append(p_value)
    else:
        granger_p_values[column] = [None] * max_lag  # 数据不足时填充None


# 打印ADF检验的p值
print("ADF检验的p值:")
for feature, p_value in adf_results.items():
    print(f"{feature}: {p_value}")

import matplotlib.pyplot as plt

# 绘制每个特征的p值
#plt.figure(figsize=(12, 8))  # 设置图形的大小
#for column, p_values in granger_p_values.items():
#    if any(p_values):  # 确保列表中至少有一个非None值
#        plt.plot(range(1, max_lag + 1), p_values, marker='o', label=column)

#plt.title('Granger因果检验的P值随滞后项的变化')
#plt.xlabel('滞后项')
#plt.ylabel('P值')
#plt.axhline(y=0.05, color='r', linestyle='--', label='显著性阈值 (0.05)')
#plt.legend()
#plt.show()

