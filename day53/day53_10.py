class Exemple:
    counter = 0
    
    def __init__(self, value) -> None:
        Exemple.counter +=1
        
    @classmethod
    def get_internal(cls):
        cls.a = 4
        return cls.counter
    
print(Exemple.get_internal())
e1 = Exemple(10)
print(Exemple.get_internal())
e2 = Exemple(99)
print(Exemple.get_internal())
print(e2.a, e1.a)
print(e1.__dict__)
print(e2.__dict__)
print(Exemple.__dict__)