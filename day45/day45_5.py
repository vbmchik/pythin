MyClass = type("MyClass", (), {'a':5,'b':12})

class M:
    def __init__(self) -> None:
        self.a = 5
        self.b = 12
        
a = MyClass()
print(a.a)
print(a.b)