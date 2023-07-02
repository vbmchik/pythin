class Duck:
    
    def __init__(self, height, weight, sex) -> None:
        self.height = height
        self.weight = weight
        self.sex = sex
    
    def walk(self):
        pass

    def quack(self):
        return print("Quack")
    
duckling = Duck(10, 3.4, "male")
drake = Duck(30, 3.7, "male")
hen = Duck(20, 3.4, "female")

drake.quack()
print(duckling.height)
print(Duck.__class__)
print(duckling.__class__)
print(duckling.sex.__class__)
print(duckling.quack.__class__)
