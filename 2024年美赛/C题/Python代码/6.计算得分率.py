import pandas as pd
import matplotlib.pyplot as plt
# 替换为你的CSV文件路径
file_path = 'E:\\桌面存储\\数学建模\\2024年美赛\\C题\\第四题\\乒乓球\\原始数据.csv'

# 读取CSV文件
data = pd.read_csv(file_path)

# 计算得分率
p1_score_rates = []
j = 0  # 初始化j为0而不是None

for i in range(len(data)):
    game_no = data['game_no'][i]
    if game_no % 2 == 0 or game_no == 1:
        j = i
    if i < j + 4:
        # 前四个回合的得分率
        score_rate = data['p1_points_won'][i] / (data['p1_points_won'][i] + data['p2_points_won'][i])
    elif i == j + 4 - 1:
        # 第五个回合的得分率，这里使用的计算可能需要根据实际的业务逻辑调整
        score_rate = data['p1_points_won'][i] / 5
    else:
        # 从第六个回合开始的得分率
        score_rate = (data['p1_points_won'][i] - data['p1_points_won'][i-4]) / 5
    p1_score_rates.append(score_rate)

# 将得分率添加到DataFrame中
data['p1_score_rate'] = p1_score_rates

# 保存到新的CSV文件
data.to_csv('E:\\桌面存储\\数学建模\\2024年美赛\\C题\\第四题\\乒乓球\\scoring_rate.csv', index=False)

# 假设您的DataFrame名为data，且已经计算了p1_score_rate列

# 绘制散点图
plt.scatter(data.index, data['p1_score_rate'])
plt.title('Score Rate Scatter Plot')
plt.xlabel('Index (Round Number)')
plt.ylabel('Score Rate')

# 显示图表
plt.show()
# 获取所有唯一的game_no值
game_nos = data['game_no'].unique()

# 为每个game_no绘制散点图
for game_no in game_nos:
    # 选取当前game_no的数据
    subset = data[data['game_no'] == game_no]
    
    # 绘制散点图
    plt.scatter(subset.index, subset['p1_score_rate'], label=f'Game No {game_no}')

plt.title('Score Rate by Game No')
plt.xlabel('Index (Round Number)')
plt.ylabel('Score Rate')
plt.legend()  # 显示图例

# 显示图表
plt.show()
