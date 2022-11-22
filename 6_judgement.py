a = 10

# 检查是否相等，用 ==
if a == 10:
    print('a==10')

# 检查是否不相等，用 !=
if a != 1:
    print('a != 1')
if not a: ## if ! a: incorret 
    print("not a")
    
# 数字比较 >、 <、 >=、 <=
if a > 6:
    print("a > 6")

# 多个条件与 and
if a > 6 and a < 12:
    print("a > 6 and a < 12:")
# 多个条件或 or
if a < 6 or a <12:
    print("a < 6 or a <12")

li1=[1,23,4523,]

# 判断列表是否包含某元素 in
if 23 in li1:
    print(" 23 in li1")

# 判断列表是否不包含某元素
if "23" not in li1:
    print('"23" not in li1')