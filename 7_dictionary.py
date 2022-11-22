# 字典

# 字典的增删改查

# 使用字典
# 字典用放在花括号{}中的一系列键-值对表示
usr = {'name': 'henry', 'age': 25, 'gender': 'binary'}
print(usr)  # {'name': 'henry', 'age': 25, 'gender': 'binary'}

# 访问字典中的值
print(usr['name'], usr['age'])

# 添加键值对
usr['city'] = 'shanghai'
print(usr)

# 修改字典中的值
cat = {}
cat['color'] = 'white'
cat['type'] = 'read'
print(cat)
cat['color'] = 'black'
print(cat)

# 删除键值对
del cat['type']
print(cat)


# 遍历字典

# 遍历所有键值对 items()
# k 代表键，v 代表值。
# 注意：即便遍历字典时，键—值对的返回顺序也与存储顺序不同。Python不关心键—值对的存储顺序，而只跟踪键和值之间的关联关系。
dic = {'name': 'henry', 'age': 25, 'gender': 'binary'}
for k, v in dic.items():
    print(k+'-'+str(v))

# 遍历所有键 keys()
# 遍历字典时会默认遍历所有的键，for k in cat.keys() 和 for k in cat 的效果一样。
for k in dic.keys():
    print(k)
    # print(k.title()) # 用字符串的 title() 方法使每个单词的首字母大写。

# 按顺序遍历所有键，可用 sorted() 排序，这让Python列出字典中的所有键，并在遍历前对这个列表进行排序。
print(12,dic.keys()) # 12 dict_keys(['name', 'age', 'gender'])
for k in sorted(dic.keys()):
    print(1,k.title())

# 遍历所有值 values()
for v in dic.values():
    print(2,v,str(v))

# 如果需要剔除重复项，可以使用 set()
dic['gender2'] = 'binary'
for v in set(dic.values()):
    print(3,str(v))

# 嵌套
# 可以在列表中嵌套字典、在字典中嵌套列表以及在字典中嵌套字典。