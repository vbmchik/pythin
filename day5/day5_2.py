class Dog():
   
    def __init__(self, name, age) :
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} barks - bow, bow, bow!")
    
    # спец метод у каждого класса он возвращает строку 
    def __str__(self):
        return f"dog {self.name} of age {self.age}"

#dog = Dog('Snoopy', 12)

#s = str(dog)
#dog.bark()
#print(s)