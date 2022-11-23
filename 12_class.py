### 类

## 创建和使用类
# 类中的函数称为方法。__init__() 是函数的构造方法，每档创建新实例时 Python 都会自动运行它。注意构造方法名字必须是这个，是规定好的。
# 上面的例子中__init__(self, name, color) 有三个形参，第一个形参 self 必不可少，还必须位于其他形参的前面。其他的形参可以根据需要调整。self 是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
# 还可以通过实例直接访问属性：my_cat.name。但在其他语言中并不建议这样做。
class Cat():
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def eat(self):
        print('I am eating' + self.name)
    def run(self):
        print('I am ' + self.color)

my_cat = Cat('duoduo', 'white')
print(my_cat.name)
print(my_cat.color)
my_cat.eat()
my_cat.run()

## 类的展性

# 给属性设置默认值
# 类中的每个属性都必须有初始值，哪怕这个值是0或空字符串。在有些情况下，如设置默认值时，在方法__init__() 内指定这种初始值是可行的;如果你对某个属性这样做了，就无需包含为它提供初始值的形参。
class Dog():
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.age = 3 # initiate value 
    def eat(self):
        print('I am eating' + self.name)
    def run(self):
        print('I am ' + self.color)
    def print_age(self):
        print('my age is ' + str(self.age))
    def update_age(self,new_age):
        self.age = new_age

my_dog = Dog('violin','red')
print(my_dog.age)

# 修改属性的值

# 1. 直接修改属性的值
my_dog.age = 4
my_dog.print_age()

# 2. 通过方法修改属性的值
# 加入 update_age() 方法来修改 age 的属性。
my_dog.update_age(99)
my_dog.print_age()

## 继承
# 一个类继承另一个类时，它将自动获得另一个类的所有属性和方法;原有的类称为父类，而新类称为子类。子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。
class Labuldo(Dog):
    def __init__(self,name,color):
        super().__init__(name,color)    # 子类的构造方法中要先实现父类的构造方法：super().__init__(name, age)。
    def play(self):
        print('I am playing')
    def run(self):
        print('I am running')

my_labuldo = Labuldo('violet','golden')
my_labuldo.eat()
my_labuldo.run()

# 还可以给子类定义自己的方法，或者重写父类的方法。
my_labuldo.play()
my_labuldo.run()

## 导入类

# 当一个文件过长时，可以将其中一部分代码抽离出去，然后导入到主文件中。导入方式有多种：

# 导入单个类
from cat_module import British_cat

# 从一个模块中导入多个类.导入多个类，中间用逗号隔开：
from cat_module import British_cat, American_cat

# 导入整个模块
# 还可以导入整个模块，再使用句点表示法访问需要的类。这种导入方法很简单，代码也易于阅读。由于创建类实例的代码都包含模块名，因此不会与当前文件使用的任何名称发生冲突。
import cat_module 
my_british_cat = cat_module.British_cat()

# 导入模块中的所有类
from dog_module import * 
# 不推荐使用这种导入方式，其原因有二。
# 首先，如果只要看一下文件开头的import语句，就 能清楚地知道程序使用了哪些类，将大有裨益;但这种导入方式没有明确地指出你使用了模块中 的哪些类。这种导入方式还可能引发名称方面的困惑。如果你不小心导入了一个与程序文件中其 他东西同名的类，将引发难以诊断的错误。这里之所以介绍这种导入方式，是因为虽然不推荐使 用这种方式，但你可能会在别人编写的代码中见到它。
# 需要从一个模块中导入很多类时，最好导入整个模块，并使用module_name.class_name语法 来访问类。这样做时，虽然文件开头并没有列出用到的所有类，但你清楚地知道在程序的哪些地 方使用了导入的模块;你还避免了导入模块中的每个类可能引发的名称冲突。


