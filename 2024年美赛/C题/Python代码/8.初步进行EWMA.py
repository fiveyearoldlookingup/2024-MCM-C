import pandas as pd
import matplotlib.pyplot as plt

# 替换为你的CSV文件路径
file_path = 'E:\\桌面存储\\数学建模\\2024年美赛\\C题\\Wimbledon最终版.csv'

# 读取CSV文件
data = pd.read_csv(file_path)

# 筛选match_id为2023-wimbledon-1301的数据
filtered_data = data[data['match_id'] == '2023-wimbledon-1701']
#filtered_data = data
# 确保数据按照某个顺序排序，比如按照游戏编号或回合数，这里假设按照'round_no'排序
filtered_data = filtered_data.sort_values(by='id')
# 设置EWMA的alpha值
alpha = 0.2  # 根据您的需要调整此值

alpha = 0.95

# 对选定的指标计算EWMA，这里我们以p1_points_won为例
filtered_data['p1_ewma_points_won'] = filtered_data['p1_points_won'].ewm(alpha=alpha, adjust=False).mean()

# 对其他指标重复上述步骤
filtered_data['p1_ewma_aces'] = filtered_data['p1_ace'].ewm(alpha=alpha, adjust=False).mean()
filtered_data['p1_ewma_winners'] = filtered_data['p1_winner'].ewm(alpha=alpha, adjust=False).mean()
filtered_data['p1_ewma_unf_err'] = filtered_data['p1_unf_err'].ewm(alpha=alpha, adjust=False).mean()

# 如果您想同时为球员2计算EWMA，也可以这样做
#data['p2_ewma_points_won'] = data['p2_points_won'].ewm(alpha=alpha, adjust=False).mean()
# ...重复对球员2的其他指标

#import matplotlib.pyplot as plt

# 绘制p1_points_won的EWMA
plt.plot(filtered_data['p1_ewma_points_won'], label='Player 1 EWMA Points Won')
plt.title('Player 1 Performance Trend')
plt.xlabel('Point Number')
plt.ylabel('EWMA of Points Won')
plt.legend()
plt.show()
