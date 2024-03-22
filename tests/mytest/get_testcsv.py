import pandas as pd

# 读取原始CSV文件
df = pd.read_csv('/home/liang/test_ddg.csv', header=None, names=['Protein', 'Mutation', 'Value'])


# 生成新的CSV文件名
output_filename = "test.csv"

# 打开CSV文件并写入数据
with open(output_filename, 'w') as f:
#    f.write("Mutation Profile Structure Value\n")  # 写入CSV文件标题行
    for index, row in df.iterrows():
        protein_name = row['Protein']
        mutation = row['Mutation']
        data_row = [mutation, f'/home/liang/code/acdc-nn/tests/profiles/{protein_name}.prof']
        #data_row = [mutation, f'/home/liang/code/acdc-nn/tests/profiles/{protein_name}.prof', f'/home/liang/code/acdc-nn/tests/structures/{protein_name}.pdb', 'A']
        f.write('\t'.join(map(str, data_row)) + '\n')  # 使用逗号分隔数据
