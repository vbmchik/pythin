import unittest
from equation_good import roots

class eqtest(unittest.TestCase):

    def testEq(self):
        self.assertEqual(roots(0, 0, 0), [0, 0, -1])

    def testEd1(self):
        self.assertEqual(roots(0, 0, 1), [])

    def testEd2(self):
        self.assertEqual(roots(1, 1, 1), [])
    
    def testEd3(self):
        self.assertEqual(roots(1, -2, 1), [1.00])
    
    def testEd4(self):
        self.assertEqual(roots(1, 0, -4), [-2,2.00])

    def testEd5(self):
        self.assertEqual(roots(2, 5, 2), [-2, -0.5])
    
    def testNew(self):
        self.assertEqual(roots(1,-4,3), [1,3])
   

unittest.main(exit=False)
