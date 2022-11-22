# 用户输入
# 函数input()让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在一个变量中，以方便你使用。
msg = input('plese input your name')
print('your name is %s'%msg)

# 如果想将输入的内容转换为数字，可以用 int() 来转换。
age = input('please input your age')
age2 = int(age) + 2
print('you will be %s in two years' % age2)