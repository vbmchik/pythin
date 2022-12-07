from figure import Figure


class Rectangle(Figure):
    def __init__(self, a: float, b: float):
        super().__init__(4)
        self.a = a
        self.b = b

    def square(self):
        return self.a*self.b

    def length(self):
        return 2*(self.a+self.b)

r = Rectangle(2,2)
print(r.square())
r.print()