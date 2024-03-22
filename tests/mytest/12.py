import pandas as pd
import csv

# 读取 TSV 文件
df = pd.read_csv('/home/liang/pdbmu2_file.tsv', sep='\t')

# 定义生成 CSV 的函数
def generate_csv_row(row):
    mutation = row['Mutation']
    uniprot_id = row['UniProt_ID']
    ddg = row['DDG']
    
    # 构建文件路径
    profile_path = f"/home/liang/code/acdc-nn/tests/profiles/{uniprot_id}.prof"
    pdb_path = f"/home/liang/code/acdc-nn/tests/structures/{uniprot_id}.pdb"
    
    # 返回 CSV 行
    return [mutation, profile_path, pdb_path, 'A']
    #return [mutation, profile_path]

# 生成 CSV 数据
csv_data = df.apply(generate_csv_row, axis=1)

# 将 CSV 数据写入文件
with open('/home/liang/testpdbmu2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')  # 使用制表符作为分隔符
    # 写入标题行
    #writer.writerow(['Mutation', 'Profile_Path', 'PDB_Path', 'A'])
    # 逐行写入数据
    for row in csv_data:
        writer.writerow(row)
