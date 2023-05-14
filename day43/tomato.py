import random
class Tomato():
    __states = ["ABSENT", "BLOOM", "GREEN", "YELLOW", "RED"]
    _random = random.Random()
    
    @property
    def laststate(self):
        return self.__states[-1]
    
    def __init__(self):
        self._stategen = self._stateget()
        self.state = next(self._stategen)

    def _stateget(self):
        for state in self.__states:
            yield state
        while(True):
            yield self.__states[-1]

    def grow(self):
        if self._random.randint(0,1):
            self.state = next(self._stategen)
         

