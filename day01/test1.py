# 1. 导包
import unittest


# 2. 自定义测试类（继承TestCase）
class Test1(unittest.TestCase):

    # 3. 测试方法 必须以 test 开头
    def test_method1(self):
        print('1')

    def test_method2(self):
        print('2')


# 4. 执行用例（方法）