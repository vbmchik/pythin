class Duck:
    counter = 0
    species = "duck"
    def __init__(self, height, weight, sex) -> None:
        self.height = height
        self.weight = weight
        self.sex = sex
        Duck.counter +=1
        
    def walk(self):
        pass

    def quack(self):
        return print("Quack")    
    
class Chicken:
    species = "chicken"
      
    def walk(self):
        pass

    def cluck(self):
        return print("Clucks")
    
duckling = Duck(10, 3.4, "male")
drake = Duck(30, 3.7, "male")
hen = Duck(20, 3.4, "female")
chicker = Chicken()

for bird in duckling, drake, hen, chicker:
    print(bird.species, end = " ")
    if bird.species == 'duck':
        bird.quack()
    elif bird.species == 'chicken':
        bird.cluck()


print(Duck.counter)