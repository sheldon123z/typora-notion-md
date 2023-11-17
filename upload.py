import os
import subprocess

# 指定文件夹路径
folder_path = "/Users/xiaodongzheng/Desktop/文章写作"

# 获取文件夹中的所有文件路径
file_paths = [
    os.path.join(folder_path, filename)
    for filename in os.listdir(folder_path)
    if os.path.isfile(os.path.join(folder_path, filename))
]

# 填写你的连接密钥和数据库 ID
connection_key = "secret_6ikHA0LbsyzJctXpW4lIfbslKeld11m6OPOzE1Nc5vU"
database_id = "d6b36b40-9d2d-49fb-abef-9bc0e9526200"

# 循环处理每个文件路径
for file_path in file_paths:
    # 构建命令
    command = f"python main.py -f '{file_path}' --connection_key {connection_key} --database_id {database_id}"

    # 调用命令
    subprocess.call(command, shell=True)
