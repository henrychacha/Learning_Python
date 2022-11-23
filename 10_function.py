# function
# Python 用关键字 def 来定义函数，函数名以冒号 : 结尾，冒号之后的缩进里的内容都是函数体。
def func(name='none'):
    print('this is a function' + name)
func()

# 函数參数
func('hello')

# 向函数传递实参的方式很多，可使用位置实参，这要求实参的顺序与形参的顺序相同;也可使用关键字实参，其 中每个实参都由变量名和值组成;还可使用列表和字典。
# 位置实參
def func2(name, age):
    print('my name is ' + name + 'and my age is ' + str(age))
func2('henry', 25)

# 关键字实參
# 关键字实参是传递给函数的名称—值对。关键字实参让你无需考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。
func2(age=12, name='henrytam')

# 默认值
def func3(name='henry', age=22):
    print('name=' + name + 'age=' + str(age))
func3('ultramarine')
# 注意：使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。这让Python依然能够正确地解读位置实参。

# 返回值
def func4():
    return 3
print(func4())

# 返回字典
# 函数可返回任何类型的值，包括列表和字典等较复杂的数据结构
def func5():
    return {'name': 'henry', 'age': 123}
print(func5())

# 传递任意数量的实參
# 形参名 *args 中的星号让 Python 创建一个名为 args 的空元组，并将收到的所有值都封装到这个元组中。
def person(*args):
    print(args)  # ('henry', 'tam', 'shuhong', 'ultramarine')
person('henry', 'tam', 'shuhong', 'ultramarine')


# 结合使用位置实參和任意数量实參
# 如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。Python 先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
def person2(city, *args):
    print('city: ' + city + 'the other args are: ')
    for v in args:
        print(v)
person2('beijing','shanghai','hangzhou','shenzhen')

# 使用任意数量的关键字实參
# 有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。在这种情况下，可将函数编写成能够接受任意数量的键—值对——调用语句提供了多少就接受多少。
# 一个这样的示例是创建用户简介:你知道你将收到有关用户的信息，但不确定会是什么样的信息。
def person3(a, b, c, **user_profile):
    usr = {}
    usr['first'] = a
    usr['second'] = b
    usr['third'] = c
    print(user_profile)
    for k,v in user_profile.items():
        usr[k] = v
    print(usr)
person3('henry', 'tam', 'hong', city='shanghai', age = 18)


## 函数编写指南
# 应给函数指定描述性名称
# 函数名应只包含小写字母和下划线
# 每个函数都应包含简要地阐述其功能的注释，该注释应紧跟在函数定义后面，并采用文档字符串格式。
# 给形参指定默认值时，等号两边不要有空格: 对于函数调用中的关键字实参，也应遵循这种约定:
# 如果程序或模块包含多个函数，可使用两个空行将相邻的函数分开，这样将更容易知道前一个函数在什么地方结束，下一个函数从什么地方开始。
# 所有的import语句都应放在文件开头，唯一例外的情形是，在文件开头使用了注释来描述整个程序。
