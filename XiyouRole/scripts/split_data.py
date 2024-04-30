import os
import json
import shutil

# 原始数据目录
source_dir = '../datasets'
# 目标目录，用于存放前1000行数据
target_dir = '../datasets/d10k'

# 如果目标目录不存在，则创建它
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# 列出所有JSON文件
for filename in os.listdir(source_dir):
    if filename.endswith('.jsonl'):
        file_path = os.path.join(source_dir, filename)
        # 打开并读取JSON文件
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            # 确保文件至少有1000行
            if len(lines) >= 1000:
                # 创建一个新文件用于保存前1000行
                target_path = os.path.join(target_dir, filename)
                with open(target_path, 'w', encoding='utf-8') as target_file:
                    # 将前1000行写入新文件
                    target_file.writelines(lines[:1000])
                    print(f'{filename} has been processed.')
            else:
                print(f'{filename} does not have 1000 lines.')

