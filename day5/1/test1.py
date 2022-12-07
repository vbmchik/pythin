import unittest
from MEQ import roots

class MEqTest(unittest.TestCase):
    def setUp(self):
        self.questions = [[1,1,1],[1,0,1],[0,1,1],[1,-2,1],[1,2,-8]]
        self.answers = [[], [], [-1.0], [1.0], [-4.0, 2.0]]
    
    def testEq(self):
        print('sd')
        for i in range(0, 5):
            self.assertEqual(self.answers[i], roots(
                self.questions[i][0], self.questions[i][1], self.questions[i][2]), f"shoud be {self.answers[i]}" )



unittest.main()
