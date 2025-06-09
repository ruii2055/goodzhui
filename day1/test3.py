# 条件语句
score = 85
if score >= 90:
    print("A")  # 如果分数 ≥ 90，输出 A
elif score >= 60:
    print("Pass")  # 如果分数 ≥ 60 且 < 90，输出 Pass
else:
    print("Fail")  # 否则输出 Fail（即分数 < 60）

# 循环语句
for i in range(5):  # 生成 0 到 4（共 5 个数）
    if i == 3:
        continue  # 当 i==3 时跳过本次循环，不执行 print
    print(i)

# 异常处理
try:
    num = int(input("Enter a number: "))  # 输入转为整数，可能出错
    print(100 / num)  # 尝试除法，除以 0 会报错
except ZeroDivisionError:
    print("Cannot divide by zero!")  # 捕捉除 0 错误
except ValueError:
    print("Invalid input!")  # 捕捉输入不能转换为整数的错误
finally:
    print("Execution completed.")  # 无论是否出错都会执行
