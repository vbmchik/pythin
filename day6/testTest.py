import unittest
from equation_good import roots

class TestFromLists(unittest.TestCase):

    def setUp(self) -> None:
        self.questions = [[1,1,1],[1,0,1],[0,1,1],[1,-2,1],[1,2,-8]]
        self.answers = [[],[],[-1],[1],[-4,2]]
    
    def test1(self):
        for i in range(0, len(self.questions)):
            with self.subTest():
                self.assertEqual(self.answers[i],
                    roots(self.questions[i][0],self.questions[i][1],self.questions[i][2]))

unittest.main()