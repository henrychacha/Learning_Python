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

