# 🐍 Python 与 Git 个人学习笔记

---

## 1. 🛠 环境准备

```bash
# 查看 Python 版本
python --version

# 创建并激活虚拟环境
python -m venv myenv
# Windows
myenv\Scripts\activate
# Linux / macOS
source myenv/bin/activate

# 安装第三方库（例如 requests）
pip install requests
```

---

## 2. 🧠 变量、变量类型与作用域

* **变量是用来存储数据的名字**，同一个变量名可以指向不同类型的值

* **常见类型**:

  * `int` (integer): 整数
  * `float`: 浮点数
  * `str`: 字符串
  * `bool`: 布尔值 True / False
  * `list`: 列表（可变序列）
  * `tuple`: 元组（不可变序列）
  * `dict`: 字典（键值对）
  * `set`: 集合（不允许重复元素）

* **作用域概念**:

  * 全局变量：在函数外部声明，全文有效
  * 局部变量：在函数内部声明，只在该函数中有效
  * `global` 可以在函数中修改全局变量
  * `nonlocal` 用于内嵌函数中修改外层的局部变量

* **类型转换**:

  * 从字符串转换成数值：`int("123")`
  * 从数值转成字符串：`str(456)`

💡 **学习经验提示**:

* Python 是动态类型，同一个变量可以在进程中切换类型
* 更好的变量名称能提高代码可读性
* 为了避免作用域问题，建议避免在函数内部直接修改全局变量

```python
name = "Alice"
age = 20
info = {"name": name, "age": age}  # dict

def my_function():
    global age
    age += 1
    print(age)
```

---

## 3. ➕ 运算符与表达式

* **算术运算**:

  * `+` 加
  * `-` 减
  * `*` 乘
  * `/` 除 (return float)
  * `//` 整除 (return int)
  * `%` 模运算 (modulus)
  * `**` 指数 (幂)

* **比较运算**:

  * `==` 等于
  * `!=` 不等于
  * `>`, `<`, `>=`, `<=`

* **逻辑运算**:

  * `and` 两条件均为 True 时返回 True
  * `or` 其中一个为 True 即为 True
  * `not` 取反

* **表达式示例**:

  * 例如: `a + b > c and d != 0`

💡 **学习经验提示**:

* Python 中 `/` 和 `//` 区别很重要：`/` 给浮点，`//` 给整数
* `and`, `or`, `not` 常用于 if 条件表达式中
* `==` 是值等于，`is` 是引用等式，不能混用
* 常用 `print(type(x))` 来检查值的类型

```python
a, b = 10, 3
print(a + b)      # 13
print(a // b)     # 3
print(a ** b)     # 1000
print(a > b)      # True
print(True and False)  # False
print(True or False)   # True
```

---

## 4. 🔁 条件语句、循环语句与异常处理

* **条件语句**：根据条件控制程序流程：`if` / `elif` / `else`
* **循环结构**：

  * `for`：适用于遍历序列（字符串、列表、range）
  * `while`：基于条件判断反复执行
  * `break`：提前退出循环
  * `continue`：跳过当前循环，继续下一轮
* **异常处理**：

  * `try`：尝试执行可能出错的语句
  * `except`：捕获指定错误类型并处理
  * `finally`：无论是否出错都执行

💡 **学习经验提示**:

* 在循环内部合理使用 `break` 和 `continue` 可优化流程
* 使用 `finally` 保证文件关闭、资源释放等操作执行
* 不建议使用 `except:` 捕获所有异常，应明确异常类型

```python
# 条件语句
score = 85
if score >= 90:
    print("A")
elif score >= 60:
    print("Pass")
else:
    print("Fail")

# for 循环
for i in range(5):
    if i == 3:
        continue
    print(i)

# 异常处理
try:
    num = int(input("Enter number: "))
    print(100 / num)
except ZeroDivisionError:
    print("Zero error")
except ValueError:
    print("Value error")
finally:
    print("Done")
```

---

## 5. 🧩 函数定义、参数与高阶函数

* **函数定义**：使用 `def` 关键字定义函数
* **参数类型**：

  * 默认参数（具有默认值）
  * 可变参数 `*args`（接收任意数量的位置参数）
  * 关键字参数 `**kwargs`
* **匿名函数**：`lambda` 表达式定义临时函数
* **高阶函数**：可以接收函数作为参数，或返回函数

💡 **学习经验提示**:

* 将重复代码封装成函数，提高可维护性
* `lambda` 适用于临时、简单的函数逻辑（如排序、filter）
* 高阶函数让 Python 更具表现力，可结合 map、filter、sorted 使用

```python
# 普通函数
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# 可变参数
def sum_numbers(*args):
    return sum(args)

# 匿名函数
double = lambda x: x * 2

# 高阶函数
def apply_func(func, value):
    return func(value)

# 示例
print(greet("Alice"))  # Hello, Alice!
print(sum_numbers(1, 2, 3))  # 6
print(double(5))  # 10
print(apply_func(lambda x: x ** 2, 4))  # 16
```

---

## 6. 📦 包与模块（Module & Package）

* **模块**：一个 `.py` 文件即为一个模块，可使用 `import` 引入使用
* **包**：带有 `__init__.py` 文件的文件夹，允许结构化管理多个模块
* **导入方式**：

  * `import module`
  * `from package import module`
  * `from module import func`
* **第三方模块**：如 `requests`, `numpy`, 通过 `pip` 安装

💡 **学习经验提示**:

* 模块名应简短且有意义，避免与标准库同名
* 使用虚拟环境隔离项目依赖
* 善用 `__name__ == '__main__'` 控制模块执行入口

```python
# mymodule.py

def say_hello():
    return "Hello from module!"

# 主程序
import mymodule
print(mymodule.say_hello())

# 使用 requests 获取数据
import requests
response = requests.get("https://api.github.com")
print(response.status_code)

# 包结构示例
# mypackage/
# ├── __init__.py
# └── mymodule.py
from mypackage import mymodule
```

---

## 7. 👥 类与对象（面向对象编程）

* **类（Class）** 是对象的蓝图，使用 `class` 关键字定义
* **对象（Object）** 是类的实例，具有属性和方法
* **构造方法 `__init__`**：用于初始化对象属性
* **继承（Inheritance）**：子类继承父类的属性和方法
* **方法重写（Override）**：子类可以重写父类方法实现自定义行为

💡 **学习经验提示**:

* 命名使用驼峰命名法（如：`MyClass`）提升代码规范
* 使用 `super()` 调用父类构造器
* 一个类只负责一类职责，遵守“单一职责原则”有助于扩展

```python
# 定义类
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"I am {self.name}, {self.age} years old."

# 子类继承
class GradStudent(Student):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def introduce(self):
        return f"I am {self.name}, a {self.major} student."

# 使用
student = Student("Alice", 20)
grad = GradStudent("Bob", 22, "CS")
print(student.introduce())
print(grad.introduce())
```

---

## 8. 🎀 装饰器（Decorator）

* **装饰器本质** 是一个高阶函数：接受函数作为参数并返回新的函数
* 使用 `@decorator_name` 语法简化函数包裹逻辑
* 常用于日志记录、函数缓存、权限验证等场景
* **带参数的装饰器** 是通过多层嵌套实现

💡 **学习经验提示**:

* 装饰器能增强已有函数而不修改其代码，符合“开放-封闭原则”
* 使用 `functools.wraps(func)` 保留原函数元信息（建议）
* 区分“无参数”和“带参数”装饰器结构

```python
# 简单装饰器
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# 带参数装饰器
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hi, {name}!")

greet("Alice")
```

---

## 9. 📂 文件操作（文本、CSV）

* **文件读写** 使用 `open()` 函数
* `with open(...)` 语法自动管理资源（上下文管理器）
* **常见模式**：

  * `'r'`：读取
  * `'w'`：写入（覆盖）
  * `'a'`：追加
* **CSV 文件处理**：使用标准库 `csv`

💡 **学习经验提示**:

* `with` 块可避免忘记关闭文件
* 文件操作要注意编码，建议使用 `encoding="utf-8"`
* 写 CSV 时加 `newline=""` 避免 Windows 下空行问题

```python
# 写文件
with open("example.txt", "w") as f:
    f.write("Hello, Python!\n")

# 读文件
with open("example.txt", "r") as f:
    content = f.read()
    print(content)

# 写 CSV
import csv
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 20])
```

---

## 🔧 Git 操作常用命令总结

```bash
# 初始化 Git 仓库
git init

# 添加所有文件到暂存区
git add .

# 提交更改
git commit -m "提交说明"

# 添加远程仓库地址
git remote add origin <远程仓库URL>

# 拉取远程并合并（避免冲突）
git pull --rebase origin main

# 推送提交到远程仓库
git push origin main

# 设置全局用户信息
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱"
```

💡 **学习经验提示**:

* GitHub 与 Gitee 的上传命令完全相同，差别只在远程仓库地址
* 第一次推送若远程已有内容（如 README）需使用 `git pull --rebase` 合并
* `git status` 和 `git log --oneline` 是排查问题的好帮手
* 推荐使用 `.gitignore` 忽略缓存、环境和日志等无关文件

---
