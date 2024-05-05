import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
# 读取Excel文件
file_path = 'E:\\桌面存储\\数学建模\\2024年美赛\\C题\\Wimbledon最终版.xlsx'
df = pd.read_excel(file_path)
# 指定中文字体为微软雅黑
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
matplotlib.rcParams['font.size'] = 10  # 可以调整字体大小
# 选择你想要进行统计的特征列
selected_features = ['serve_no', 'server','p1_ace','p2_ace','winner_shot_type','p1_double_fault','p2_double_fault','p1_unf_err','p2_unf_err','p1_net_pt','p2_net_pt','p1_break_pt','p2_break_pt']


# 创建一个空的DataFrame来存储统计结果
statistics_df = pd.DataFrame(columns=['特征', '取值', '频次'])

# 计算每个特征中不同取值的频次，并添加到DataFrame中
for feature in selected_features:
    value_counts = df[feature].value_counts().reset_index()
    value_counts.columns = ['取值', '频次']
    value_counts['特征'] = feature
    statistics_df = pd.concat([statistics_df, value_counts], ignore_index=True)

# 打印整理后的统计结果表格
print(statistics_df)

# 可视化结果
plt.figure(figsize=(10, 6))
bars = plt.bar(statistics_df['特征'] + ' ' + statistics_df['取值'].astype(str), statistics_df['频次'])
plt.xlabel('Characteristics and values')
plt.ylabel('Frequency')
plt.title('Classification feature frequency statistics for selected features')
plt.xticks(rotation=45)

# 在每个柱状图上添加标签
for bar in bars:
    height = bar.get_height()
    plt.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),  # 3 points vertical offset
                 textcoords="offset points",
                 ha='center', va='bottom')

# 添加图例
#plt.legend(selected_features)
# 调整横坐标标签的位置向左移动一点
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()