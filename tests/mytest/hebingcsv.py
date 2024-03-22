import csv

def merge_csv_columns(input_csv1, input_csv2, output_csv):
    # 读取第一个CSV文件
    with open(input_csv1, 'r', newline='', encoding='utf-8') as csv_file1:
        reader1 = csv.reader(csv_file1)
        data1 = list(reader1)

    # 读取第二个CSV文件
    with open(input_csv2, 'r', newline='', encoding='utf-8') as csv_file2:
        reader2 = csv.reader(csv_file2)
        data2 = list(reader2)

    # 合并列
    merged_data = []
    for i, (row1, row2) in enumerate(zip(data1, data2)):
        merged_row = row1 + row2
        merged_data.append(merged_row)

    # 写入合并后的数据到新的CSV文件
    with open(output_csv, 'w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file, delimiter='\t')
        writer.writerows(merged_data)

# 使用示例
input_csv1 = '/home/liang/pdbmu2_file.tsv'  # 替换为第一个CSV文件路径
input_csv2 = '/home/liang/output.csv'  # 替换为第二个CSV文件路径
output_csv = 'result4.csv'  # 替换为合并后的CSV文件路径
merge_csv_columns(input_csv1, input_csv2, output_csv)
