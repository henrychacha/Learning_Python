# 异常
# 异常是使用try-except代码块处理的。try-except代码块让Python执行指定的操作，同时告诉Python发生异常时怎么办。
try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide it by zero!")

# else 代码块
# 如果 try 中的代码运行成功，没有出现异常，则执行 else 代码块中的代码。
try:
    print(5/1)
except ZeroDivisionError:
    print('division error')
else:
    print('it is OK!')


