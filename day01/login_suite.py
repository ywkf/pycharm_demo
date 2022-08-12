import unittest

from login_test import TestLogin

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(TestLogin))

runner = unittest.TextTestRunner()

runner.run(suite)