import csv

# 打开输入文件
with open('/home/liang/2temp.tsv', 'r', newline='', encoding='utf-8') as infile:
    # 读取 TSV 文件
    reader = csv.DictReader(infile, delimiter='\t')
    
    # 获取列名
    fieldnames = reader.fieldnames
    
    # 打开输出文件
    with open('pdbmu2_file.tsv', 'w', newline='', encoding='utf-8') as outfile:
        # 写入 TSV 文件
        writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        
        # 逐行处理数据
        for row in reader:
            # 检查 Mutation 列是否存在
            if 'Mutation' in row:
                # 删除 Mutation 列前七位的内容
                row['Mutation'] = row['Mutation'][7:]
            
            # 写入更新后的行
            writer.writerow(row)

print("处理完成！")