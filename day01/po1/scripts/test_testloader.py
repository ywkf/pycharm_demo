import time
import unittest

from unittestreport import TestRunner

from po1.scripts.test_check import TestCheck
from po1.scripts.test_check_fin import TestCheckFin
from po1.scripts.test_copy_prog_to_check import TestCopyProgToCheck
from po1.scripts.test_login import TestLogin

# class Test1(unittest.TestCase):
#
#     def test1(self):
#         suite = unittest.defaultTestLoader.discover('./', '**login.py')
#         # suite = unittest.defaultTestLoader.discover('./', '**to_check.py')
#         unittest.TextTestRunner().run(suite)


suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin)
# suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCopyProgToCheck)
# suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCheck)
# suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCheckFin)

# runner = TestRunner(suite, 'report_{}.html'.format(time.strftime('%Y_%m_%d_%H_%M_%S')), '..\\report', '测试报告', 'wyf',
#                     '全台网')
testdefname = suite.__str__().split('testMethod=')[1].split('>')[0]
print('suite: ', suite.__str__().split('testMethod=')[1].split('>')[0])
runner = TestRunner(suite=suite,
                    tester='wyf',
                    filename='report_{}_{}.html'.format(testdefname, time.strftime('%Y_%m_%d_%H_%M_%S')),
                    report_dir='..\\report',
                    title='测试报告',
                    desc='项目场景测试',
                    templates=1)

runner.run()
