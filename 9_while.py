## while 循环
num =1 
while num <= 5:
    print(num)
    num +=1
print('num=',num)

# break
# 要立即退出while循环，不再运行循环中余下的代码，也不管条件测试的结果如何，可使用break语句。break语句用于控制程序流程，可使用它来控制哪些代码行将执行，哪些代码行不执行，从而让程序按你的要求执行你要执行的代码。

# continue
# 要返回到循环开头，并根据条件测试结果决定是否继续执行循环，可使用continue语句，它不像 break 语句那样不再执行余下的代码并退出整个循环。