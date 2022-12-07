import json


class Animal():
    def __init__(self, age, name, color, npaws):
        self.age = age
        self.name = name
        self.color = color
        self.npaws = npaws

    def voice(self):
        print('Animal say ...')


class Cat(Animal):
    def __repr__(self) -> str:
        return f'This is cat its name is {self.name} it is {self.age} y/old'

    def voice(self):
        print('Cat say "Meow!"')


class Fish(Animal):
    def __repr__(self) -> str:
        return f'This is fish its name is {self.name} it is {self.age} y/old'

    def __init__(self, age, name, color):
        super().__init__(age, name, color, 0)

    def desc(self):
        print(self)


fish = Fish(2, 'Flaunder', 'Red')
cat = Cat(3, 'Linda', 'White', 4)
l = [cat, fish]



