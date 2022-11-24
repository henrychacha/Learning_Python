# 单元测试
# 测试类要继承 unittest.TestCase ，通过 self.assertEqual 断言是否得到的结果和预期相等。
import unittest
from test_name_function import got_formatted_name


class NameTestCase(unittest.TestCase):
    def test_name_function(self):
        full_name = got_formatted_name('henry', 'tam')
        self.assertEqual(full_name, 'Henry Tam')


unittest.main()

# 常见的断言方法
# assertEqual(a, b) 	核实a == b
# assertNotEqual(a, b) 	核实a != b
# assertTrue(x) 	核实x为True
# assertFalse(x) 	核实x为False
# assertIn(item, list) 	核实item在list中
# assertNotIn(item, list) 	核实item不在list中


# setUp() 方法
# 如果你在TestCase类中包含了方法 setUp() ，Python将先运行它，再运行各个以test_打头的方法。通常用于做一些初始化操作。
