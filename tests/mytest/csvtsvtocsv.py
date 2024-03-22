import pandas as pd

# 读取CSV文件
csv_data = pd.read_csv('/home/liang/output.csv')

# 读取TSV文件，使用制表符作为分隔符
tsv_data = pd.read_csv('/home/liang/pdbmu2_file.tsv',sep='\t',engine='python')
#tsv_data = pd.read_csv('/home/liang/result3.csv')

# 合并两个数据框
merged_data = pd.concat([tsv_data, csv_data], axis=1)

# 写入到一个新的CSV文件中
merged_data.to_csv('result4.csv', index=False)
