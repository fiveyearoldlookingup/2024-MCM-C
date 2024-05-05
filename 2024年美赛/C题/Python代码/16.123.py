import pandas as pd

# 读取Excel文件
file_path = "C:\\Users\\35274\\Desktop\\第三题的相关分析的数据.xlsx"
df = pd.read_excel(file_path)
from statsmodels.tsa.stattools import adfuller
import numpy as np

# 定义ADF检验函数
def adf_test(series):
    result = adfuller(series, autolag='AIC')
    p_value = result[1]
    return p_value

# 对每个特征进行ADF检验
features = ['Subtractive momentum_won', 'double_fault', 'winner_shot_type', 'serve', 'serve_no', 'unf_err', 'net_pt', 'break_pt', 'y81', 'y82', 'y9', 'y10', 'ace', 'score_rate', 'M(t) player1', 'M(t) player2', ]
adf_p_values = {}

for feature in features:
    adf_p_values[feature] = adf_test(df[feature])

# 显示ADF检验的p值
print(adf_p_values)
# 对不通过ADF检验的序列进行一阶差分
differenced_data = df.copy()
for feature, p_value in adf_p_values.items():
    if p_value > 0.05:  # 以0.05作为阈值判断是否平稳
        differenced_data[feature] = df[feature].diff().dropna()

from statsmodels.tsa.stattools import grangercausalitytests

from statsmodels.tsa.stattools import grangercausalitytests

# 定义Granger因果检验函数
def granger_test(data, maxlag=12):
    test_result = grangercausalitytests(data, maxlag=maxlag, verbose=False)
    p_values = [round(test_result[i + 1][0]['ssr_chi2test'][1], 4) for i in range(maxlag)]
    return p_values

# 对平稳的序列进行Granger因果检验，检验其他特征对`match_momentum`的影响
granger_p_values = {}
features = [ 'double_fault', 'winner_shot_type', 'serve', 'serve_no', 'unf_err', 'net_pt', 'break_pt', 'y81', 'y82', 'y9', 'y10', 'ace', 'score_rate', 'M(t) player1', 'M(t) player2', ]
for feature in features:
    if feature in differenced_data.columns:
        data = pd.concat([differenced_data['Subtractive momentum_won'], differenced_data[feature]], axis=1).dropna()
        granger_p_values[feature] = granger_test(data)

# 显示Granger因果检验的结果
print(granger_p_values)

