import pandas as pd
import matplotlib.pyplot as plt

# 替换为你的CSV文件路径
file_path = 'E:\\桌面存储\\数学建模\\2024年美赛\\C题\\Wimbledon最终版.csv'

# 读取CSV文件
data = pd.read_csv(file_path)

# 筛选match_id为2023-wimbledon-1301的数据
filtered_data = data[data['match_id'] == '2023-wimbledon-1301']
#filtered_data = data
# 确保数据按照某个顺序排序，比如按照游戏编号或回合数，这里假设按照'round_no'排序
filtered_data = filtered_data.sort_values(by='id')

# 绘制折线图
plt.plot(filtered_data['id'], filtered_data['p1_score_rate'], marker='o', linestyle='-')
plt.title('Score Rate for Match ID 2023-wimbledon-1301')
plt.xlabel('Round Number')
plt.ylabel('Score Rate')

# 显示图表
plt.show()
