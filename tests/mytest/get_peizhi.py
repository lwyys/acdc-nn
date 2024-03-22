import os

def run_hhblits(input_folder, output_folder, database_path, cpu=4, num_iterations=2):
    # 获取输入文件夹中的所有fasta文件
    fasta_files = [f for f in os.listdir(input_folder) if f.endswith('.fasta')]

    # 遍历每个fasta文件
    for fasta_file in fasta_files:
        input_path = os.path.join(input_folder, fasta_file)
        output_path = os.path.join(output_folder, os.path.splitext(fasta_file)[0] + '.psi')

        # 构建HHblits命令
        hhblits_command = f"/home/liang/programs/hhsuite/bin/hhblits -d {database_path} -i {input_path} -cpu {cpu} -n {num_iterations} -opsi {output_path}"

        # 执行HHblits命令
        os.system(hhblits_command)

if __name__ == "__main__":
    # 输入文件夹路径
    input_folder = "./"

    # 输出文件夹路径
    output_folder = "./output"

    # 数据库路径
    database_path = "/home/liang/databases/uniclust30/uniclust30_2018_08/uniclust30_2018_08"

    # CPU数量
    cpu = 4

    # 迭代次数
    num_iterations = 2

    # 如果输出文件夹不存在，则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 运行HHblits
    run_hhblits(input_folder, output_folder, database_path, cpu, num_iterations)
