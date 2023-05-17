import random
class Tomato():
    __states = ["ABSENT", "BLOOM", "GREEN", "YELLOW", "RED"]
    random = random.Random()
    
    @property
    def laststate(self):
        return self.__states[-1]
    
    def __init__(self):
        self.__stategen = self.__stateget()
        self.state = next(self.__stategen)

    def __stateget(self):
        for state in self.__states:
            yield state
        while(True):
            yield self.__states[-1]

    def grow(self):
        if self.random.randint(0,1):
            self.state = next(self.__stategen)
         

    def __str__(self) -> str:
        return f"Tomato: {self.state}"


