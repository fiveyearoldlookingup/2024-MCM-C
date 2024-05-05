import pandas as pd

# 假设'data.csv'是您的数据文件
# 请将'path_to_your_data.csv'替换成您数据集的实际路径
data = pd.read_csv('E:\\桌面存储\\数学建模\\2024年美赛\\C题\\Wimbledon_featured_matchescopy.csv')

# 使用'MD'来填充'return_depth'列中的缺失值
data['return_depth'] = data['return_depth'].fillna('MD')




# 使用向前填充（forward fill）来填充'speed_mph'列中的缺失值
data['speed_mph'] = data['speed_mph'].fillna(method='ffill')

# 找到'serve_width'列和'serve_depth'列的众数
# mode()方法返回的是一个Series，众数可能不止一个，这里我们取第一个众数
serve_width_mode = data['serve_width'].mode()[0]
serve_depth_mode = data['serve_depth'].mode()[0]

# 使用众数来填充这两列的缺失值
data['serve_width'] = data['serve_width'].fillna(serve_width_mode)
data['serve_depth'] = data['serve_depth'].fillna(serve_depth_mode)

# 保存修改后的数据集到新的CSV文件，如果需要可以打开这行代码
data.to_csv('updated_data.csv', index=False)

