from day5_3 import Team
from day5_2 import Dog
import unittest
class testTeam(unittest.TestCase):

    def setUp(self):
        self.team = Team('Bob Jhones')
        self.team.addDog(Dog('Snoop', 9))
        self.team.addDog(Dog('Richie', 4))
        self.team.addDog(Dog('Fluf', 6))
        self.team2 = Team('Pamela Travers')
        self.team2.addDog(Dog('Cobo', 11))
        self.team2.addDog(Dog('Plut', 2))
        self.team2.addDog(Dog('Tailor', 6))

    def test1(self):
        self.team.mixTeam(self.team2,2)
        self.assertEqual(len(self.team2.dogs),1)
    
    def test2(self):
        self.team.mixTeam(self.team2, 1)
        self.assertEqual(len(self.team.dogs),4)

    def test3(self):
        self.team.joinTeam(self.team2)
        self.assertEqual(len(self.team.dogs), 6)

unittest.main(exit=False)


