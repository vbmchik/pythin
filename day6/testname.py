import unittest
from namer import makename

# есть метод получает имя и фамилию 
# и возвращает их в красивом виде одной строкой

class Testnamer(unittest.TestCase):

    def test1(self):
        self.assertEqual(makename("miChael", "jaCKSon"),"Michael Jackson")

unittest.main(exit=False)