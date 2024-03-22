import csv
import os
from Bio import ExPASy
from Bio import SeqIO

def fetch_feast(uniprot_id, output_file):
    try:
        handle = ExPASy.get_sprot_raw(uniprot_id)
        record = SeqIO.read(handle, "swiss")
        handle.close()
        with open(output_file, "w") as f:
            SeqIO.write(record, f, "fasta")
        print(f"FEAST file for UniProt ID {uniprot_id} saved to {output_file}")
    except Exception as e:
        print(f"Failed to fetch FEAST file for UniProt ID {uniprot_id}: {e}")

def fetch_feast_from_csv(csv_file, output_folder):
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            uniprot_id = row['uniprot_id']  # 假设CSV文件中UniProt ID列名为'uniprot_id'
            output_file = os.path.join(output_folder, f"{uniprot_id}.fasta")
            fetch_feast(uniprot_id, output_file)

# 主程序
if __name__ == '__main__':
    csv_file = '/home/liang/test_ddg.csv'  # 替换为你的CSV文件路径
    output_folder = 'feast_files'  # 存放FEAST文件的目录，如果目录不存在则会自动创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    fetch_feast_from_csv(csv_file, output_folder)
