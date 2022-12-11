import unittest
from pifagor import pifagor


class testPifagor(unittest.TestCase):

    def test_1(self):
        self.assertTrue(pifagor(3, 4, 5))

    def test_2(self):
        self.assertFalse(pifagor(1, 1, 1))

    def test_3(self):
        self.assertTrue(pifagor(4, 5, 3))

    def test_4(self):
        self.assertTrue(pifagor(5, 4, 3))

    def test_5(self):
        self.assertFalse(pifagor(-3, -4, -5))

    def test_6(self):
        self.assertFalse(pifagor('Maria', -4, -5))

    def test_7(self):
        self.assertFalse(pifagor('Maria', [2,3,4], -5))


unittest.main(exit=False)
