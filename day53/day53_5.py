class Human:
    def __init__(self, weight, age, salary) -> None:
        self.weight = weight
        self.age = age
        self.salary = salary
        
    def __add__(self, other):
        return self.weight + other.weight
    
    def __eq__(self, __value: object) -> bool:
        return self.salary == __value.salary
    
a = Human(30,40,56)
b = Human(31,43,56)

print(a==b)


number = 10
print(number+20)
print(number.__add__(20))