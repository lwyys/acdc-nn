import csv

def extract_even_lines(txt_file, csv_file):
    with open(txt_file, 'r', encoding='utf-8') as txt_f:
        lines = txt_f.readlines()
        even_lines = [line.strip() for idx, line in enumerate(lines) if idx % 2 != 0]

    with open(csv_file, 'w', newline='', encoding='utf-8') as csv_f:
        writer = csv.writer(csv_f)
        writer.writerow(['seq_ddg'])
        for line in even_lines:
            writer.writerow([line])

# 使用示例
txt_file = '/home/liang/test_seq_in.txt'  # 替换为你的txt文件路径
csv_file = 'output.csv'  # 替换为你要保存的csv文件路径
extract_even_lines(txt_file, csv_file)
