def bark(self):
    print('boof boof!')
    
class Animal:
    def feed(self):
        print("Nyam nyam!")
        
Dog = type("Dog", (Animal, ), {"age": 0, "bark": bark})

doggy = Dog()
doggy.feed()
doggy.bark()