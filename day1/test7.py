# 简单装饰器
def my_decorator(func):  # 装饰器函数，接收一个函数作为参数
    def wrapper():  # 内部函数：在被装饰函数前后加逻辑
        print("Before function")
        func()  # 调用原始函数
        print("After function")
    return wrapper  # 返回包装后的新函数

@my_decorator  # 等价于：say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello!")

say_hello()
# 输出：
# Before function
# Hello!
# After function

# ✅ 知识点：
# - 装饰器本质是一个函数 → 接收函数，返回函数
# - 使用 `@装饰器名` 语法糖自动套用装饰器
# - 可以在不修改原函数代码的前提下增强其功能

# 带参数的装饰器
def repeat(n):  # 外层函数：接收参数 n
    def decorator(func):  # 中层函数：接收原函数
        def wrapper(*args, **kwargs):  # 内层函数：实际包装逻辑（支持传参）
            for _ in range(n):  # 重复执行 n 次
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)  # 装饰器带参数：将 greet 包装成执行 3 次
def greet(name):
    print(f"Hi, {name}!")

greet("Alice")
# 输出：
# Hi, Alice!
# Hi, Alice!
# Hi, Alice!

# ✅ 知识点：
# - 多层嵌套结构：外层接收参数，中层接收函数，内层执行包装
# - 使用 *args, **kwargs 可以兼容任意函数签名
# - 可用于实现日志记录、重复执行、权限校验等功能