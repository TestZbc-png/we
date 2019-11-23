import unittest
# 初始化TextTestRunner套件并调用方法
suite = unittest.defaultTestLoader.discover('./case', pattern='test*.py')

# 初始化执行对象
runner= unittest.TextTestRunner()
# 初始化执行对象
runner.run(suite)
