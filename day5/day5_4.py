from day5_3 import Team
from day5_2 import Dog

team = Team('Bob Jhones')
team.addDog(Dog('Snoop', 9))
team.addDog(Dog('Richie', 4))
team.addDog(Dog('Fluf', 6))
team.printTeam()
team2 = Team('Pamela Travers')
team2.addDog(Dog('Cobo', 11))
team2.addDog(Dog('Plut', 2))
team2.addDog(Dog('Tailor', 6))
team2.printTeam()
team2.mixTeam(team,2)
#team.dogs.remove(team.dogs[1])
print(team2.trainer)
print(len(team2.dogs))
print(len(team.dogs))
team2.printTeam()
team.printTeam()

print([x.name for x in  team2.dogs])
#print([ x+y for x in range(1,10) for y in range(1,10) ])
#print([str(x)+str(y)+str(z) for x in range(1,10) for y in range(1,10) for z in range(1,10)] )