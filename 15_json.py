# 用json 存储数据
# Python 中使用 json.dump() 和 json.load() 来存储和读取 json 文件。
# 注意使用前先导入 json 模块。
import json
usr = {'name':'henry','age':24}
with open('json.txt','w') as obj:
    json.dump(usr,obj)
    print('finish dumping')

with open('json.txt') as obj:
    contents = json.load(obj)
    print(contents)
