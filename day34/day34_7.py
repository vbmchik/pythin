def decorator(something):
    
    def wrapper(self, lie):
        lie +=3
        return something(self, lie)
    return wrapper

class Madam:
    def __init__(self) -> None:
        self.age=28
    
    @decorator
    def sayMyAge(self, lie):
        print(f"Мне {self.age - lie}")


l = Madam()
l.sayMyAge(5)