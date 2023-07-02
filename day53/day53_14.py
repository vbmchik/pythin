class Car:
    def __init__(self, engine) -> None:
        self.engine = engine
     
    def start(self):
        self.engine.start()
           
class GasEngine:
    def __init__(self, hp) -> None:
        self.hp = hp
    
    def start(self):
        print(f'Gas engine {self.hp} hp')
        
class DieselEngine:
    def __init__(self, hp) -> None:
        self.hp = hp
    
    def start(self):
        print(f'Diesel engine {self.hp} hp')
        
myCar = Car(GasEngine(4))
myCar.engine.start()
myCar = Car(DieselEngine(12))
myCar.start()