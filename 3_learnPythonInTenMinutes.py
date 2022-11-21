#https://juejin.cn/post/6844903765410070535

## variables and data types

name = "henry tam"
a = name.title()
b = name.upper()
c = name.lower()
print(a,b,c) # Henry Tam HENRY TAM henry tam

first = 'henry'
second = 'tam'
full = first + " " + second
print(full) #henry tam

# 要在字符串中添加制表符，可使用字符组合 \t，要在字符串中添加换行符，可使用字符组合 \n 
print("henry\ttam")
print("henry\ntam")

# 删除空白
msg=" henry tam "
print(msg.rstrip()) #strip right emptiness 
print(msg.lstrip()) #strip left emptiness 
print(msg.strip()) #strip both emptiness 

# perform calculations
print(1 + 2)
print(1 * 2)
print(1 - 2)
print(1 / 2)
print(1 + 2*4)
print((1+1)*5)

# 浮点数
print(0.1 + 0.2) # 0.30000000000000004
print(0.1 + 0.1) # 0.2
print(3 * 0.1) # 0.30000000000000004

# str()
# print("age" + 123) # 如果用数字跟字符串拼接，就会出现类型错误。
print("age" + str(123))


## 列表

list1 = []
list1.append(1)
list1.append(2)
list1.append(3)
list2 =[1,2,3,4]
print(list2[-1],list2[-2]) # 4 3 
print(list1,list2,list2[0]) #[1, 2, 3] [1, 2, 3, 4] 1
# 获取最后一个元素可以用 -1，如 list[-1] 是获取最后一个元素，list[-2] 是获取倒数第二个元素。

# 修改元素
list2[1] = 'change'
print(list2) # [1, 'change', 3, 4]


# 添加元素
list2.append('last')
list2.insert(1,'insert')
print(list2) # [1, 'insert', 'change', 3, 4, 'last']

# 删除元素
# del：按索引删除
# pop()：删除列表最后一个元素并返回最后一个元素的值。也可以传索引删除任意位置的值。
# remove()：按值删除
## 方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值。
## 如果你不确定该使用del语句还是pop()方法，下面是一个简单的判断标准:如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用del语句;如果你要在删除元素后还能继续使用它，就使用方法pop()。
list3 = [1,2,3,4,5]
del list3[1]
print(list3) # [1, 3, 4, 5]
print(list3.pop()) # 5
print(list3.pop(0)) # 1 // 给 pop() 传索引删除其他位置的值
list3.remove(4) 
print(list3) # [1, 3]

## 组织列表

# sort()对列表进行永久性排序
#使用 sort() 方法将改变原列表。如果要反转排序，只需向sort()方法传递参数 reverse=True。
list4 = [1,123,23,5,25]
list4.sort()
print(list4) # [1, 5, 23, 25, 123]
list4.sort(reverse=True)
print(list4)  # [123, 25, 23, 5, 1]

# 函数sorted()对列表进行临时排序
# 让你能够按特定顺序显示列表元素，同时不影响它们在列表中的原始排列顺序。
print(sorted(list4))  # [1, 5, 23, 25, 123]
print(list4) # [123, 25, 23, 5, 1]
print(sorted(list4, reverse=True)) # [123, 25, 23, 5, 1]


# 反转列表
# 使用方法 reverse()。 reverse() 也会改变原始列表。
# reverse() 只会按原来的顺序反转，不会进行额外的按字母排序。
list4.reverse()
print(list4) # [1, 5, 23, 25, 123]

# 确定列表的长度
# 函数len()可快速获悉列表的长度。
print(len(list4)) # 5

## 操作列表

# 循环
# 使用 for…in 循环。 
# python 以缩进来区分代码块，所以需要正确的缩进
list5 = ['1','2','3','4']
for val in list5:
    print(val)


# range()
# Python函数range()让你能够轻松地生成一系列的数字。
print(range(1,5)) #range(1,5)
for val in range(1,5): 
    print(val) # 注意：range() 会产生包含第一个参数但不包含第二个参数的一系列数值。

# 使用 range() 创建列表
print(list(range(1,6))) # [1, 2, 3, 4, 5]

# range() 还可以指定步长
print(list(range(1,11,3))) # [1, 4, 7, 10]


# 对列表简单的计算
list6 =[1,2,3,4,523,123,23,21]
print(max(list6)) #523
print(min(list6)) #1
print(sum(list6)) #700

#  列表解析
# 列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素。
print([value**2 for value in range(1,11)]) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 切片
# 要创建切片，可指定要使用的第一个元素和最后一个元素的索引。与函数range()一样，Python在到达你指定的第二个索引前面的元素后停止。要输出列表中的前三个元素，需要指定索引0~3，这将输出分别为0、1和2的元素
name = ['aa','bb','cc','dd']
print(name[1:4]) 
# ['bb', 'cc', 'dd']

# 如果你没有指定第一个索引，Python将自动从列表开头开始:
print(name[:4]) 
# ['aa', 'bb', 'cc', 'dd']

# 如果没有指定终止索引，将自动取到列表末尾
print(name[1:])
# ['bb', 'cc', 'dd']

# 也可以使用负数索引，比如返回最后三个元素
print(name[-3:])
# ['bb', 'cc', 'dd']
print(name[-3:-1])
# ['bb', 'cc']

# 遍历切片
for val in name[1:3]:
    print(val)


## 复制列表
# 可以使用切片来快速复制列表，不指定开始索引和结束索引。
name2 = name[:]
print(name2)

# 用切片复制出来的新列表，跟原来的列表是完全不同的列表，改变其实一个不会影响另一个列表。
name.append('ee')
print(name)
print(name2)

# 而如果简单的通过赋值将 names 赋值给 names2，就不能得到两个列表，实际上它们都指向了同一个列表。如果改变其中一个，另一个也将被改变
name3 = name
name.append('ff')
print(name3)
print(name)