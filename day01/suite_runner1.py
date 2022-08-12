import unittest

from test1 import Test1

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(Test1))

runner = unittest.TextTestRunner()

runner.run(suite)