# 变量类型
name = "Alice"  # 字符串类型 str，用于存储文本
age = 20        # 整数类型 int，用于存储整数数值
grades = [90, 85, 88]  # 列表类型 list，用于存储一组数据（可变）
info = {"name": "Alice", "age": 20}  # 字典类型 dict，用于键值对存储（键：值）

# 类型转换
age_str = str(age)  # 将整数转换为字符串："20"
number = int("123")  # 将字符串转换为整数：123

# 变量作用域
x = 10  # 全局变量，函数内外都能访问
def my_function():
    y = 5  # 局部变量，只在函数内部有效
    global x  # 声明使用全局变量 x，而不是创建一个新的局部变量
    x += 1  # 修改全局变量 x 的值
    print(f"Inside function: x={x}, y={y}")  # 输出函数内部的变量值

my_function()  # 调用函数，执行上面的语句
print(f"Outside function: x={x}")  # 输出函数外部的变量值
