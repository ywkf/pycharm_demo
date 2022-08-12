import unittest
from parameterized import parameterized
from login import login

data = [
    ('admin', '123456', 'success'),
    ('root', '123456', 'failed'),
    ('admin', '123123', 'failed'),
    ('root', '123123', 'failed')
]


class TestLogin(unittest.TestCase):

    @parameterized.expand(data)
    def test_login(self, username, password, expect):
        self.assertEqual(expect, login(username, password))

    # def test_1(self):
    #     if login('admin', '123456') == 'success':
    #         print('pass')
    #     else:
    #         print('fail')
    #
    # def test_2(self):
    #     if login('root', '123456') == 'failed':
    #         print('pass')
    #     else:
    #         print('fail')
    #
    # def test_3(self):
    #     if login('admin', '123123') == 'failed':
    #         print('pass')
    #     else:
    #         print('fail')
    #
    # def test_4(self):
    #     if login('aaa', '123123') == 'failed':
    #         print('pass')
    #     else:
    #         print('fail')