from tomato import Tomato
class TomatoBush():
    
    def __init__(self, numberOfTomatoes) -> None:
        self.tomatoes = [ Tomato() for _ in range(numberOfTomatoes) ]
        
    def growall(self):
        for tomato in self.tomatoes:
            tomato.grow()
    
    def all_are_ripe(self):
        return any(map(lambda x: x.state == x.laststate, self.tomatoes))
            
    def give_away_all(self):
        self.tomatoes.clear()
        
    def number_of_tomatoes(self):
        return len(self.tomatoes)
    



