#  元组
## Python将不能修改的值称为不可变的，而不可变的列表被称为元组; 元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。

tuple1 = ("aa","bb","cc")
print(tuple1)
print(tuple1[0],tuple1[1])
# tuple1[0]='kk' # error 

# 遍历用法跟列表一致。
for val in tuple1:
    print(val)