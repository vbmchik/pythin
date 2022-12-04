from day5_2 import Dog

class Team():
    def __init__(self, trainer):
        self.trainer = trainer
        self.dogs = list()
    def addDog( self, dog ):
        self.dogs.append(dog)
    def joinTeam(self,team):
        self.dogs.extend(team.dogs)
        team.dogs.clear()
    def printTeam(self):
        print(self.trainer)
        for dog in self.dogs:
            print(dog)


#horde = [str(Dog('Snoop', 9)), str(Dog('Richhie', 4)), str(Dog('Fluf', 6))]
#print(horde)


