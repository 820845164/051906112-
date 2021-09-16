import unittest
from main import test

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(test("./words1.txt", "./org1.txt")[0], "Line1: <好人> 好技术的蚕丝@@@人")

    def test2(self):
        self.assertEqual(test("./words1.txt", "./org2.txt")[0], "Line1: <时间> 时间")

    def test3(self):
        self.assertEqual(test("./words1.txt", "./org3.txt")[0], "Line1: <时间> 试件")

    def test4(self):

        self.assertEqual(test("./words1.txt", "./org4.txt")[0], "Line1: <时间> 时jian")

    def test5(self):
        self.assertEqual(test("./words1.txt", "./org5.txt")[0], "Line1: <时间> shi剑")

    def test6(self):
        self.assertEqual(test("./words1.txt", "./org6.txt")[0], "Line1: <时间> 时…………键")

    def test7(self):
        self.assertEqual(test("./words1.txt", "./org7.txt")[0], "Line1: <时间> sj")

    def test8(self):
        self.assertEqual(test("./words1.txt", "./org8.txt")[0], "Line1: <时间> 日寸jian")

    def test9(self):
        self.assertEqual(test("./words1.txt", "./org9.txt")[0], "Line1: <时间> shi*&^捡")

    def test10(self):
        self.assertEqual(test("./words1.txt", "./org10.txt")[0], "Line1: <时间> 時間")


if __name__ == '__main__':
    unittest.main()