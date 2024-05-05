import pandas as pd
import numpy as np

# 替换为您的CSV文件路径
file_path = r'E:\桌面存储\数学建模\2024年美赛\C题\Wimbledon_featured_matchescopy.csv'

# 加载CSV文件
df = pd.read_csv(file_path)

# 从'player1'和'player2'列提取唯一名称
unique_player1 = df['player1'].unique()
unique_player2 = df['player2'].unique()

# 结合两个数组并获取所有唯一的参赛选手名称
all_players_set = set(unique_player1) | set(unique_player2)

# 将集合转换回列表以便显示
all_players_list = list(all_players_set)

# 打印所有独特的参赛选手名称
print(all_players_list)
