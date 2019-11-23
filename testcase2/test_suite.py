
import unittest

# 初始化测试套件
from testcase1.test1 import Test1
from testcase2.test2 import Test2

suite = unittest.TestSuite()
# 方法一: 逐类逐个方法添加 suite.addTest(测试类名('测试方法名'))
suite.addTest(Test1('test_func1'))
# 调用方法组装测试用例
# 方法一：逐类逐个方法添加 suite.addTest(测试类名（'测试方法名'）)

suite.addTest(unittest.makeSuite(Test2))

runner = unittest.TextTestRunner()

runner.run(suite)