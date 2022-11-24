# 文件

# 从文件中读取数据
# 要使用文本文件中的信息，首先需要将信息读取到内存中。为此，你可以一次性读取文件的全部内容，也可以以每次一行的方式逐步读取。

# 读取整个文件
# open() 用于打开一个文件，参数为文件的路径。
# 关键字 with 在不再需要访问文件后将其关闭。有了 with 你只管打开文件，并在需要时使用它，Python自会 在合适的时候自动将其关闭。
# 相比于原始文件，该输出唯一不同的地方是末尾多了一个空ge。为何会多出这个空ge呢?因为 read() 到达文件末尾时返回一个空字符串' '，而将这个空字符串显示出来时就是一个空ge。要删除多出来的空ge，可在print语句中使用 rstrip()。
# 文件路径可以是相对路径，也可以是绝对路径。
with open('test.txt') as file_obj:
    contents = file_obj.read()
    print(contents)

# 逐行读取
print('++++++++++++')
with open('test.txt') as file_obj:
    for line in file_obj:
        print(line.rstrip())

# 写入文件
# 在这个示例中，调用open()时提供了两个实参，第一个实参也是要打开的文件的名称；第二个实参('w')告诉Python，我们要以写入模式打开这个文件。
# 可选模式：
# r ：只读。 默认
# w : 只写。如果文件不存在则创建，如果文件存在则先清空，再写入。
# a ：附加模式，写入的内容追加到原始文件后面。如果文件不存在则创建。
# r+ ：可读可写。

with open('test.txt', 'r+') as file_obj:
    file_obj.write('rewrite all contents')
    print(file_obj.read())

with open('test.txt', 'a') as file_obj:
    file_obj.write('\nadd a new line')
