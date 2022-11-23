## 导入导出

# 导入整个模块
import cat_module
cat_module.cat('fish')


# 导入特定的函数
# 你还可以导入模块中的特定函数，这种导入方法的语法如下:
from cat_module import cat

# 通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数:
from dog_module import wang, sleep
sleep()

# 使用 as 给函数指定别名
from dog_module import wang as bark

# 使用 as 给模块指定别名
import dog_module as dog
print(dog.name)

# 导入模块中的所有函数
# 由于导入 了每个函数，可通过名称来调用每个函数，而无需使用句点表示法。然而，使用并非自己编写的 大型模块时，最好不要采用这种导入方法:如果模块中有函数的名称与你的项目中使用的名称相 同，可能导致意想不到的结果: Python 可能遇到多个名称相同的函数或变量，进而覆盖函数，而 不是分别导入所有的函数。
# 最佳的做法是，要么只导入你需要使用的函数，要么导入整个模块并使用句点表示法。这能 让代码更清晰，更容易阅读和理解。
from dog_module import *
