# 创建模块 mymodule.py
# mymodule.py
def say_hello():
    return "Hello from module!"

# 主程序
import mymodule  # 导入自定义模块 mymodule.py（必须与当前文件同目录或在路径中）
print(mymodule.say_hello())  # 调用模块中的函数 → 输出："Hello from module!"

# 导入第三方模块
import requests
response = requests.get("https://api.github.com")
print(response.status_code)  # 打印响应状态码 → 200 表示成功

# 包使用示例
from mypackage import mymodule  # 从包 mypackage 中导入 mymodule 模块


# 可以在文件夹下创建一个 __init__.py 的文件，又是一种导包方式