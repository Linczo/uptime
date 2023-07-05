import os
import random
import string
import sys

def generate_random_code():
    # 生成随机的代码
    code_type = random.choice(["html", "css", "js"])
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    if code_type == "html":
        return f"<html><body>{code}</body></html>"
    elif code_type == "css":
        return f"body {{ color: {code}; }}"
    elif code_type == "js":
        return f"console.log('{code}');"

def generate_code_file(directory):
    # 在指定目录中随机生成代码文件
    code = generate_random_code()
    code_type = random.choice(["html", "css", "js"])
    filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    filepath = os.path.join(directory, f"{filename}.{code_type}")
    with open(filepath, 'w') as file:
        file.write(code)
    print(f"生成文件：{filename}.{code_type}")

def count_files_in_directory(directory):
    # 统计目录中的文件数
    file_count = sum(1 for _ in os.scandir(directory) if _.is_file())
    return file_count

def clear_directory(directory):
    # 清空目录中的文件
    for file in os.scandir(directory):
        if file.is_file():
            os.remove(file.path)

# 通过命令行参数获取目录和文件数阈值
if len(sys.argv) < 3:
    print("请提供目录和文件数阈值作为命令行参数")
    sys.exit(1)

target_directory = sys.argv[1]
threshold = int(sys.argv[2])

# 如果目录不存在，则创建目录
if not os.path.exists(target_directory):
    os.makedirs(target_directory)
    print(f"目录 {target_directory} 创建成功")

# 生成代码文件
generate_code_file(target_directory)

# 统计文件数并清空目录
num_files = count_files_in_directory(target_directory)
print(f"当前文件数：{num_files}")

if num_files > threshold:
    clear_directory(target_directory)
    print("目录已清空")
