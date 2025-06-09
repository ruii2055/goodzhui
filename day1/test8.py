# 写文件
with open("example.txt", "w") as f:  # "w" 模式：写入（会覆盖原文件）
    f.write("Hello, Python!\n")  # 写入一行文本，记得加换行符 \n

# ✅ 知识点：
# - `open(filename, mode)` 打开文件
# - `"w"` 模式表示写入（write），若文件不存在则创建
# - 使用 `with` 可以自动关闭文件，推荐写法

# 读文件
with open("example.txt", "r") as f:  # "r" 模式：读取文件内容
    content = f.read()  # 一次性读取全部内容为字符串
    print(content)  # 输出内容：Hello, Python!

# ✅ 其他读取方法：
# - `f.readline()` 读取一行
# - `f.readlines()` 按行返回列表
# - 读取时需注意文件是否存在，否则可能报错

# 处理CSV
import csv
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)  # 创建 CSV 写入器
    writer.writerow(["Name", "Age"])  # 写入表头
    writer.writerow(["Alice", 20])  # 写入一行数据

# ✅ 知识点：
# - `csv.writer()` 用于将数据写入 CSV 格式文件
# - `newline=""` 是防止 Windows 下多出空行的技巧
# - `writerow()` 写入一行（列表形式）