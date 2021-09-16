import unittest
from main import test

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(test("./words1.txt", "./org1.txt")[0], "Line1: <好人> 女子人")

    def test2(self):
        self.assertEqual(test("./words1.txt", "./org2.txt")[0], "Line1: <好人> 好人")

    def test3(self):
        self.assertEqual(test("./words1.txt", "./org3.txt")[0], "Line1: <好人> 好@人")

    def test4(self):

        self.assertEqual(test("./words1.txt", "./org4.txt")[0], "Line1: <好人> 好忍")

    def test5(self):
        self.assertEqual(test("./words1.txt", "./org5.txt")[0], "Line1: <好人> 号认")

    def test6(self):
        self.assertEqual(test("./words1.txt", "./org6.txt")[0], "Line1: <好人> haoren")

    def test7(self):
        self.assertEqual(test("./words1.txt", "./org7.txt")[0], "Line1: <好人> hr")

    def test8(self):
        self.assertEqual(test("./words1.txt", "./org8.txt")[0], "Line1: <好人> 好时代城对话词人")

    def test9(self):
        self.assertEqual(test("./words1.txt", "./org9.txt")[0], "Line1: <好人> 好技术的蚕丝@@@人")

    def test10(self):
        self.assertEqual(test("./words1.txt", "./org10.txt")[0], "Line1: <好人> hao@@24人")


if __name__ == '__main__':
    unittest.main()
