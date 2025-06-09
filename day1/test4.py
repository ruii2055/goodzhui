# 函数定义
def greet(name, greeting="Hello"):  # 默认参数 greeting="Hello" → 输出：Hello, Alice!
    return f"{greeting}, {name}!"  # 提供 greeting="Hi" → 输出：Hi, Bob!

print(greet("Alice"))  # Hello, Alice!
print(greet("Bob", "Hi"))  # Hi, Bob!

# 可变参数
def sum_numbers(*args):
    return sum(args)
print(sum_numbers(1, 2, 3, 4))  # 输出：10（1+2+3+4）

# 匿名函数
double = lambda x: x * 2
print(double(5))  # 10

# 高阶函数
def apply_func(func, value):
    return func(value)
print(apply_func(lambda x: x ** 2, 4))  # 输出：16（4 的平方）
