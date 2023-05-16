from time import sleep
from tomatobush import TomatoBush, Tomato


class Gardener():
    def __init__(self, name, number_of_bushes) -> None:
        self.name = name
        self.__plants = [ TomatoBush(Tomato._random.randint(1,35)) for _ in range(number_of_bushes)]
        
    def work(self):
        for plant in self.__plants:
            plant.growall()
            
    def if_not_bushes_harvested(self):
        return any(map(lambda x: x.number_of_tomatoes() ,self.__plants))
    
    def harvest(self):
        if len(self.__plants) == 0:
            print("All is done")
            return
        ready = list(filter(lambda p: p.all_are_ripe() ,self.__plants))
        if len(ready) == 0:
            print('Nothing is ready!')
            return
        print("We have bushes to harvest!")
        for bush in ready:
            print(f'bush with {bush.number_of_tomatoes()} tomatoes is ready and will be harvested')
            self.__plants.remove(bush)
            bush.give_away_all()
            
g = Gardener("Samuel", 120)

while(g.if_not_bushes_harvested()):
    g.work()
    g.harvest()
    sleep(0.5)
    
g.harvest()
