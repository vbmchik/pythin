# Импорт модуля для тестировщиков
import unittest
# импорт метода который тесируется
from equations import MEQn
# класс теста
class eqTest(unittest.TestCase):

    def testEQ(self):
        # сравниваем результаты вывода 
        # MEQn(1,-3,2) и эталонный ответ [1.0, 2.0]
        self.assertEqual(MEQn(1,-3,2),[1.0,2.0])

    def testEQ1(self):
        self.assertEqual(MEQn(1, 0, -1), [-1.0, 1.0])

    

unittest.main(exit=False)