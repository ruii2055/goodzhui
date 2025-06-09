# 定义类
class Student:
    def __init__(self, name, age):
        self.name = name  # 实例属性：姓名
        self.age = age  # 实例属性：年龄

    def introduce(self):
        return f"I am {self.name}, {self.age} years old."  # 实例方法：介绍自己

# ✅ 知识点：
# - 使用 `class 类名:` 定义类
# - `__init__` 是构造方法（初始化实例属性）
# - `self` 表示对象自身，用于访问属性和方法
# - 方法属于类内部的函数

# 继承
class GradStudent(Student):  # 继承自 Student 类
    def __init__(self, name, age, major):
        super().__init__(name, age)  # 调用父类构造方法
        self.major = major  # 新增属性：专业

    def introduce(self):  # 重写父类方法（方法重载）
        return f"I am {self.name}, a {self.major} student."

# 使用
student = Student("Alice", 20)
grad = GradStudent("Bob", 22, "CS")
print(student.introduce())  # I am Alice, 20 years old.
print(grad.introduce())     # I am Bob, a CS student.
