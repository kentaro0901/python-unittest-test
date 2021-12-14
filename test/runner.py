import unittest
import test.test_fizzbuzz
 
# python -m unittest test/runner.py
# python -m unittest でプロジェクト全体のテストを自動探索してくれる

class TestRunner(unittest.TestCase):
 
    def test_runner(self):
        test_suite = unittest.TestSuite()

        # 手動で追加
        # test_suite.addTest(unittest.makeSuite(test.test_fizzbuzz.TestFizzBuzz))
        # test_suite.addTest(unittest.makeSuite(test.test_mod2.TestMod2))

        # 自動で追加をカスタマイズ
        # tests = unittest.defaultTestLoader.discover("test", pattern="test_*.py")
        # test_suite.addTest(tests)

        unittest.TextTestRunner().run(test_suite)