import unittest

import fizzbuzz as fb

class TestFizzBuzz(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(cls.__name__)
 
    # @classmethod
    # def tearDownClass(cls):
    #     print('*** 全体後処理 ***')
 
    # def setUp(self):
    #     print('+ テスト前処理')
 
    # def tearDown(self):
    #     print('+ テスト後処理')

    def test_normal(self):
        self.assertEqual(1, fb.fizzbuzz(1))

    def test_fizz(self):
        self.assertEqual("Fizz", fb.fizzbuzz(3))

    def test_buzz(self):
        self.assertEqual("Buzz", fb.fizzbuzz(5))

    def test_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fb.fizzbuzz(15))

    @unittest.skip('スキップ')
    def test_skip(self):
        self.assertEqual("FizzBuzz", fb.fizzbuzz(15))
