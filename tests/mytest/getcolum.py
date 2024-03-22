import pandas as pd

# 读取数据库文件
data = pd.read_csv('/home/liang/potapov2156.csv', sep = ',', dtype= str)

# 合并两列并创建新的一列
data['change'] = data['mutation'].astype(str) + data['position'].astype(str) + data['wild_type'].astype(str)

# 提取特定列
desired_columns = ['uniprot_id', 'change', 'ddG']  # 要提取的列
filter_column = 'is_curated' # 用于筛选的列
filter_value = 'true' # 用于筛选的值

# 根据筛选条件提取数据
desired_data = data[data[filter_column] == filter_value][desired_columns]
desired_data.dropna(axis=0, how='any', inplace=True, subset=None) # 删除空值所在行
desired_data = desired_data.drop_duplicates()
#desired_data['pdb_id'] = desired_data['pdb_id'].astype(str).str[:4]

# 保存为 CSV 文件
desired_data.to_csv('test_ddg.csv', index=False)